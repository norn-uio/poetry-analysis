import json
import re
import string
from pathlib import Path
from typing import Generator

from convert_pa import convert_nofabet, nofabet_to_ipa

PUNCTUATION_MARKS = str(
    string.punctuation + "‒.,!€«»’”—⁷⁶⁰–‒––!”-?‒"
)  # Note! The three long dashes look identical, but are different unicode characters

VALID_NUCLEI = [
    "aa",
    "ae",
    "oe",
    "ou",
    "ei",
    "øy",
    "ai",
    "oi",
    "au",
    "a",
    "e",
    "i",
    "o",
    "u",
    "y",
    "æ",
    "ø",
    "å",
]

GRAMMATICAL_SUFFIXES = [
    "ene",
    "ane",
    "et",
    "te",
    "er",
    # "ar", # Too common in short words to filter out
    "en",
]


def is_grammatical_suffix(string: str) -> bool:
    return string in GRAMMATICAL_SUFFIXES


def endswith(sequence: str | list[str], suffix: str) -> bool:
    """Check if a sequence ends with a given suffix."""
    if isinstance(sequence, str):
        return sequence.endswith(suffix)
    elif isinstance(sequence, list):
        last_element = sequence.copy().pop()
        if isinstance(last_element, str):
            return last_element.endswith(suffix)
        return False
    return False


def is_punctuation(char: str) -> bool:
    """Check if a character is a punctuation mark."""
    return char in PUNCTUATION_MARKS


def strip_redundant_whitespace(text: str) -> str:
    """Strip redundant whitespace and reduce it to a single space."""
    return re.sub(r"\s+", " ", text).strip()


def strip_punctuation(string: str) -> str:
    """Remove punctuation from a string"""
    alphanumstr = ""
    for char in string:
        if not is_punctuation(char):
            alphanumstr += char
    return strip_redundant_whitespace(alphanumstr)


def make_comparable_string(input: list | str) -> str:
    """Convert a list of strings into a single comparable string."""
    if isinstance(input, list):
        string = " ".join(input)
    else: 
        string = str(input)
    string = strip_punctuation(string)
    string = re.sub(r"[0123]", "", string)  # remove stress markers
    return string.casefold()


def convert_to_syllables(phonemes: str | list, ipa: bool = False) -> list:
    """Turn a sequence of phonemes into syllable groups."""
    transcription = phonemes if isinstance(phonemes, str) else " ".join(phonemes)
    if ipa:
        ipa = nofabet_to_ipa(transcription)
        syllables = ipa.split(".")
    else:
        nofabet_syllables = convert_nofabet.nofabet_to_syllables(transcription)
        syllables = [" ".join(syll) for syll in nofabet_syllables]
    return syllables


def syllabify(transcription: list[list]) -> list:
    """Flatten list of syllables from a list of transcribed words."""
    syllables = [
        syll  # if syll is not None else "NONE"
        for word, pron in transcription
        for syll in convert_to_syllables(pron, ipa=False)
    ]
    return syllables


def annotate_transcriptions(transcription: list) -> Generator:
    for word, pronunciation in transcription:
        nofabet = format_transcription(pronunciation)
        yield dict(
            word=word,
            nofabet=nofabet,
            syllables=convert_nofabet.nofabet_to_syllables(nofabet),
            ipa=nofabet_to_ipa(nofabet),
        )


def split_paragraphs(text: str) -> list:
    """Split a text into paragraphs and paragraphs into lines."""
    return [
        [line.rstrip() for line in paragraph.rstrip().splitlines()]
        for paragraph in re.split("\n{2,}", text)
        if paragraph
    ]


def format_transcription(pronunciation):
    return " ".join(pronunciation)


def gather_stanza_annotations(func) -> callable:
    """Decorator to apply a function to each stanza in a text."""

    def wrapper(text: str) -> dict:
        stanzas = split_stanzas(text)
        stanza_annotations = {}
        for i, stanza in enumerate(stanzas, 1):
            stanza_text = "\n".join(stanza)
            stanza_annotations[f"stanza_{i}"] = func(stanza_text)
        return stanza_annotations

    return wrapper


def split_stanzas(text: str) -> list:
    """Split a poem into stanzas and stanzas into verses."""
    return [
        [verse.rstrip() for verse in stanza.rstrip().splitlines()]
        for stanza in re.split("\n{2,}", text)
        if stanza
    ]


def annotate(func, text: str, stanzaic: bool = False, outputfile: str | Path = None):
    if stanzaic:
        new_func = gather_stanza_annotations(func)
        annotations = new_func(text)
    else:
        annotations = func(text)
    if outputfile is not None:
        Path(outputfile).write_text(
            json.dumps(annotations, indent=4, ensure_ascii=False), encoding="utf-8"
        )
        print(f"Saved annotated data to {outputfile}")
    else:
        return annotations


if __name__ == "__main__":
    import doctest

    doctest.testmod()
