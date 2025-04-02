import json
import logging
import re
import string
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from convert_pa import convert_nofabet

from poetry_analysis import utils


@dataclass
class Poem:
    _id: str
    text: str
    stanzas: list


@dataclass
class Verse:
    id_: str | int
    rhyme_score: int = 0
    rhyme_tag: str = ""
    text: str = ""
    transcription: str = ""
    tokens: list | None = None
    syllables: list | None = None
    last_token: str | None = None
    rhymes_with: str | int | None = None

    @property
    def dict(self) -> dict:
        """Return the Verse object as a dictionary."""
        dictionary = self.__dict__
        dictionary["verse_id"] = self.id_
        del dictionary["id_"]
        return dictionary


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
    return bool(result)


def strip_stress(phoneme: str) -> str:
    """Strip the stress marker from a phoneme."""
    return phoneme.strip("0123")


def is_nucleus(symbol: str, orthographic: bool = False) -> bool:
    """Check if a phoneme or a letter is a valid syllable nucleus."""
    if orthographic:
        valid_nuclei = utils.VALID_NUCLEI
    else:
        valid_nuclei = convert_nofabet.PHONES_NOFABET.get("nuclei")
    return strip_stress(symbol) in valid_nuclei


def find_nucleus(word: str) -> re.Match:
    """Check if a word has a valid syllable nucleus."""
    rgx = re.compile(rf"({'|'.join(utils.VALID_NUCLEI)})")
    return rgx.search(word)


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


def score_orthographic_rhyme(sequence1: str | list, sequence2: str | list) -> float:
    """Check if two words rhyme and return a rhyming score.

    1:      Only the syllable nucleus + coda (=rhyme) match # perfect or proper rhyme
    0.5:    NØDRIM or lame rhyme. One of the words is fully contained in the other, e.g. 'tusenfryd' / 'fryd'
    0:      No match
    """
    sequence1 = utils.make_comparable_string(sequence1)
    sequence2 = utils.make_comparable_string(sequence2)

    substring = longest_common_substring(sequence1, sequence2)

    if not substring:
        return 0

    nucleus = find_nucleus(substring)
    if not nucleus:
        return 0
    if utils.is_grammatical_suffix(substring):
        # only the grammatical suffixes match
        # e.g. "arbeidet" / "skrevet"
        return 0
    if utils.is_grammatical_suffix(substring[nucleus.start() :]):
        # the rhyming part is a grammatical suffix
        # e.g. "blomster" / "fester"
        return 0

    if not sequence1.endswith(substring) or not sequence2.endswith(substring):
        # not an end rhyme
        return 0
    if substring == sequence1 or substring == sequence2:
        # one of the words is fully contained in the other
        return 0.5

    if nucleus and (sequence1 != sequence2):
        return 1
    # otherwise, assume that the words do not rhyme
    return 0


def longest_common_substring(string1: str, string2: str) -> str:
    """Find the longest common substring between two strings.

    Implementation based on the pseudocode from:
    https://en.wikipedia.org/wiki/Longest_common_substring#Dynamic_programming
    """
    m = len(string1)
    n = len(string2)
    L = np.zeros((m + 1, n + 1))
    z = 0
    result = ""

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                if L[i][j] > z:
                    z = L[i][j]
                    result = string1[(i - int(z)) : i]
            else:
                L[i][j] = 0
    return result


def find_rhyming_line(current: str, previous_lines: list[str]) -> tuple:
    """Check if the current line rhymes with any of the previous lines."""

    for idx, previous in reversed(list(enumerate(previous_lines))):
        if previous.last_token is None or current.last_token is None:
            continue
        # rhyme_score = score_orthographic_rhyme(previous.last_token, current.last_token)
        rhyme_score = score_rhyme(previous.last_token, current.last_token)
        if rhyme_score > 0:
            return idx, rhyme_score
    return None, 0


def tag_rhyming_verses(verses: list[list[str]], orthographic: bool = False) -> list:
    """Annotate end rhyme patterns in a poem stanza.

    Args:
        verses: list of verselines with words
        orthographic: if True, the words strings are orthographic,
            otherwise assume phonemic nofabet transcriptions
    Return:
        list of annotated verses with rhyme scores and rhyme tags
    """
    alphabet = iter(string.ascii_letters)

    processed = []  # needs to be a list!
    for idx, verseline in enumerate(verses):
        if not verseline:
            continue

        if orthographic:
            current_verse = Verse(
                id_=idx,
                text=" ".join(verseline),
                tokens=verseline,
            )
            current_verse.last_token = current_verse.tokens[-1]
        else:
            current_verse = Verse(
                id_=idx,
                transcription="\t".join(verseline),
                tokens=verseline,
                syllables=utils.convert_to_syllables(verseline, ipa=False),
            )

            last_syll = find_last_stressed_syllable(current_verse.syllables)
            if last_syll is None:
                current_verse.last_token = current_verse.syllables[-1]
            else:
                current_verse.last_token = last_syll[-1]

        idx, rhyme_score = find_rhyming_line(current_verse, processed)
        if idx is not None and rhyme_score > 0:
            rhyming_verse = processed[idx]
            current_verse.rhyme_tag = rhyming_verse.rhyme_tag
            current_verse.rhyme_score = rhyme_score
            current_verse.rhymes_with = rhyming_verse.id_

        else:
            try:
                current_verse.rhyme_tag = next(alphabet)
            except StopIteration:
                logging.info(
                    "Ran out of rhyme tags at %s! Initialising new alphabet.", idx
                )
                alphabet = iter(string.ascii_letters)
                current_verse.rhyme_tag = next(alphabet)

        processed.append(current_verse)
    return processed


def collate_rhyme_scheme(annotated_stanza: list) -> str:
    """Join the rhyme tags rom each tagged verse to form a rhyme scheme."""
    return "".join(verse.rhyme_tag for verse in annotated_stanza)


def get_stanzas_from_transcription(
    transcription: dict, orthographic: bool = False
) -> list:
    """Parse a dict of transcribed verse lines and return a list of stanzas."""
    n_lines = len(transcription.keys()) - 1  # subtract the text_id key
    logging.debug("Number of lines in poem: %s", n_lines)
    poem = []
    stanza = []
    for n in range(n_lines):
        verse = transcription.get(f"line_{n}")
        if len(verse) > 0:
            words, pron = zip(*verse)
            verseline = list(words if orthographic else pron)
            stanza.append(verseline)
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


def tag_poem_file(poem_file: str):
    """Annotate rhyming schemes in a poem.

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
    stanzas = get_stanzas_from_transcription(poem_text, orthographic=False)
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


def main():
    """Main function to run the rhyme detection script."""
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

    tag_poem_file(args.jsonfile)


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    main()
