import re
import string
from typing import Generator


from convert_pa import nofabet_to_ipa, convert_nofabet


PUNCTUATION_MARKS = str(
    string.punctuation + "‒.,!€«»’”—⁷⁶⁰–‒––!”-?‒"
)  # Note! The three long dashes look identical, but are different unicode characters


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


def convert_to_syllables(phonemes: list, ipa=False) -> list:
    """Turn a sequence of phonemes into syllable groups."""
    transcription = phonemes if isinstance(phonemes, str) else " ".join(phonemes)
    if ipa:
        ipa = nofabet_to_ipa(transcription)
        syllables = ipa.split(".")
    else:
        syllables = convert_nofabet.nofabet_to_syllables(transcription)
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
