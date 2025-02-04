# %%
# rhyme_detection main module!

import re
import string
import logging
import json
from pathlib import Path

from dataclasses import dataclass
from convert_pa import convert_nofabet

from poetry_analysis import utils


@dataclass
class Poem:
    _id: str
    text: str
    stanzas: list


@dataclass
class Verse:
    _id: str
    text: str
    tokens: list
    transcription: str
    syllables: list
    rhyme_tag: str


def is_stressed(syllable: str | list) -> bool:
    """Check if a syllable is stressed by searching for stress markers.

    Stress markers:
        0 - Vowel/syllable nucleus without stress
        1 - Primary stress with toneme 1
        2 - Primary stress with toneme 2
        3 - Secondary stress
    """
    if isinstance(syllable, list):
        syllable = " ".join(syllable)
    result = re.search(r"[123]", syllable)
    return True if result else False


def strip_stress(phoneme: str) -> str:
    """Strip the stress marker from a phoneme."""
    return phoneme.strip("0123")


def is_nucleus(phoneme: str) -> bool:
    """Check if a phoneme is a vowel."""
    syll_nuclei = convert_nofabet.PHONES_NOFABET.get("nuclei")
    return True if strip_stress(phoneme) in syll_nuclei else False


def find_last_stressed_syllable(syllables: list) -> list:
    for idx, syll in reversed(list(enumerate(syllables))):
        if is_stressed(syll):
            # flatten the rhyming syllable sequence
            stressed = [s for rhyme in syllables[idx:] for s in rhyme]
            return stressed


def find_syllable_rhyme(syllables: list) -> list:
    """Identify the rhyming part of a verse.

    Args:
        syllables: nested list of lists of phonemes
    """
    stressed = find_last_stressed_syllable(syllables)
    return remove_syllable_onset(stressed)


def remove_syllable_onset(syllable: list) -> list:
    """Split a syllable nucleus and coda from the onset to find the rhyming part of the syllable."""
    for idx, phone in enumerate(syllable):
        if is_nucleus(phone):
            return syllable[idx:]
    logging.debug("No nucleus found in %s", syllable)


"""
TODO: Fiks feil med NoneType

Traceback (most recent call last):
  File "/home/ingeridd/prosjekter/NORN-poems/src/poetry_analysis/rhyme_detection.py", line 264, in <module>
    main(args.jsonfile)
  File "/home/ingeridd/prosjekter/NORN-poems/src/poetry_analysis/rhyme_detection.py", line 229, in main
    tagged = tag_rhyming_verses(stanza)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ingeridd/prosjekter/NORN-poems/src/poetry_analysis/rhyme_detection.py", line 144, in tag_rhyming_verses
    rhyme_score = score_rhyme(previous_syll, current_syllables)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ingeridd/prosjekter/NORN-poems/src/poetry_analysis/rhyme_detection.py", line 102, in score_rhyme
    if do_syll_seqs_rhyme(last_syll1, last_syll2):
       ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/ingeridd/prosjekter/NORN-poems/src/poetry_analysis/rhyme_detection.py", line 87, in do_syll_seqs_rhyme
    if all(strip_stress(s1) == strip_stress(s2) for s1, s2 in zip(syll1, syll2)):
                                                              ^^^^^^^^^^^^^^^^^
TypeError: 'NoneType' object is not iterable
"""


def do_syll_seqs_rhyme(syll1: list, syll2: list):
    """Check  if each syllable in two syllable sequences are identical, apart from the stress marker."""
    if all(strip_stress(s1) == strip_stress(s2) for s1, s2 in zip(syll1, syll2)):
        return True
    return False


def score_rhyme(syllable1: list, syllable2: list) -> int:
    """Check if two syllable sequences rhyme, and return a rhyming score.

    If the onset, nucleus and coda of two different syllable sequences are the same,
        the score is 0.5. (Nødrim, e.g. "fryd" and "fryd")
    If the rhyming parts (without onsets) of two syllable sequences have the same phonemes, the score is 1.
    If they don't match at all, the score is 0.
    """
    last_syll1 = find_last_stressed_syllable(syllable1)
    last_syll2 = find_last_stressed_syllable(syllable2)
    try:
        is_rhyming = do_syll_seqs_rhyme(last_syll1, last_syll2)
    except TypeError:
        logging.error("Error in syllable comparison: %s and %s", last_syll1, last_syll2)
        return 0
    if is_rhyming:
        logging.debug("NØDRIM: %s and %s", last_syll1, last_syll2)
        return 0.5

    rhyme1 = find_syllable_rhyme(syllable1)
    rhyme2 = find_syllable_rhyme(syllable2)
    try:
        is_rhyming = do_syll_seqs_rhyme(rhyme1, rhyme2)
    except TypeError:
        logging.error("Error in syllable comparison: %s and %s", rhyme1, rhyme2)
        return 0
    if is_rhyming:
        logging.debug("Rhyme: %s and %s", rhyme1, rhyme2)
        rhyme_score = 1
    else:
        # logging.debug("No rhyme: %s and %s", rhyme1, rhyme2)
        rhyme_score = 0
    return rhyme_score


def split_stanzas(text: str) -> list:
    """Split a poem into stanzas and stanzas into verses."""
    return [
        [verse.rstrip() for verse in stanza.rstrip().splitlines()]
        for stanza in re.split("\n{2,}", text)
        if stanza
    ]


def tag_rhyming_verses(transcribed_verses: list) -> list:
    """Annotate end rhyme patterns in a poem stanza.

    Args:
        transcribed_verses: list of phonemically transcribed and syllabified verse lines
    Return:
        list of annotated verses with transcriptions and rhyme tags
    """
    alphabet = iter(string.ascii_letters)

    processed = []  # needs to be a list!
    # iteratively compare previous lines with current line
    for idx, current_syllables in enumerate(transcribed_verses):
        if not current_syllables:  # skip empty lines
            continue
        does_rhyme = False
        for previous_verse in reversed(processed):
            previous_syll = previous_verse.get("syllables")
            rhyme_score = score_rhyme(previous_syll, current_syllables)
            if rhyme_score > 0:
                rhyme_tag = previous_verse.get("rhyme_tag")
                does_rhyme = True
                break

        if not does_rhyme:
            rhyme_score = 0
            try:
                rhyme_tag = next(alphabet)
            except StopIteration:
                logging.error("Ran out of rhyme tags! Initialising new alphabet.")
                alphabet = iter(string.ascii_letters)
                rhyme_tag = next(alphabet)

        processed.append(
            dict(
                verse_id=idx,
                syllables=current_syllables,
                rhyme_score=rhyme_score,
                rhyme_tag=rhyme_tag,
            )
        )
    return processed


def collate_rhyme_scheme(annotated_stanza: list) -> str:
    """Join the rhyme tags rom each tagged verse to form a rhyme scheme."""
    return "".join(verse.get("rhyme_tag") for verse in annotated_stanza)


def get_stanzas_from_transcription(transcription: dict) -> list:
    """Parse a dict of transcribed verse lines and return a list of stanzas."""
    n_lines = len(transcription.keys()) - 1  # subtract the text_id key
    logging.debug("Number of lines in poem: %s", n_lines)
    poem = []
    stanza = []
    for n in range(n_lines):
        verse = transcription.get(f"line_{n}")
        if len(verse) > 0:
            syllables = utils.syllabify(verse)
            stanza.append(syllables)
        else:
            if len(stanza) == 0:
                continue
            poem.append(stanza)
            stanza = []
    if len(poem) == 0 and len(stanza) > 0:
        poem.append(stanza)
    return poem


def format_annotations(annotations: dict) -> dict:
    """Format lists of lists in the innermost dicts to a single line along with the dict key."""
    formatted_annotations = {}
    for stanza_key, stanza_value in annotations.items():
        formatted_stanza = []
        for verse in stanza_value:
            formatted_verse = {
                k: " ".join(map(str, v)) if isinstance(v, list) else v
                for k, v in verse.items()
            }
            formatted_stanza.append(formatted_verse)
        formatted_annotations[stanza_key] = formatted_stanza
    return formatted_annotations


def main(poem_file: str):
    """Annotate rhyming schemes in poems.

    Procedure:
    1. Split a poem into stanzas and verses.
    2. Transcribe the verses phonemically.
    3. Group the verse phonemes into syllables.
    4. Identify the last stressed syllable of a verse.
    5. Compare the syllable sequence of a verse with
        those of all previous verses in the same stanza. (NB! Replace "stanza" with "poem"? )
    6. Extract the rhyming part (i.e. nucleus + coda) of the last stressed syllable
    7. Score the rhyming:
        1="only rhymes match", # perfect match
        0.5="NØDRIM: onset also matches" # lame rhyme: 'tusenfryd' / 'fryd'
        0="No match"
    8. Tag the verse with a letter, depending on which line it rhymes with if at all
    """
    filepath = Path(poem_file)
    poem_text = json.loads(filepath.read_text())
    poem_id = poem_text.get("text_id")
    logging.debug("Tagging poem: %s", poem_id)
    stanzas = get_stanzas_from_transcription(poem_text)
    # print(stanzas)

    file_annotations = {}
    for idx, stanza in enumerate(stanzas):
        tagged = tag_rhyming_verses(stanza)
        rhyme_scheme = collate_rhyme_scheme(tagged)
        tagged.insert(0, {"rhyme_scheme": rhyme_scheme})
        file_annotations[f"stanza_{idx}"] = tagged

    formatted_content = format_annotations(file_annotations)
    outputfile = filepath.parent / f"{filepath.stem}_rhyme_scheme.json"
    with outputfile.open("w") as f:
        f.write(json.dumps(formatted_content, ensure_ascii=False, indent=4))

    logging.debug(
        "Saved rhyme scheme annotations for poem %s to \n\t%s", poem_id, outputfile
    )
    # Assume that the stanzas are independent of each other
    # and that the rhyme scheme is unique to each stanza


# %%

if __name__ == "__main__":
    import argparse
    from datetime import datetime

    parser = argparse.ArgumentParser(description="Tag rhyme schemes in a poem.")
    parser.add_argument(
        "jsonfile", type=str, help="Path to a json file with phonemic transcriptions."
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Set logging level to debug."
    )
    args = parser.parse_args()

    if args.verbose:
        today = datetime.today().date()
        logging_file = f"{__file__.split('.')[0]}_{today}.log"
        logging.basicConfig(level=logging.DEBUG, filename=logging_file, filemode="a")
    main(args.jsonfile)

# %%
