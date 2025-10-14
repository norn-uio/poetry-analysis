import json
import re
import string
from pathlib import Path
from typing import Callable, Generator

from convert_pa import nofabet_to_ipa, nofabet_to_syllables
from nb_tokenizer import tokenize

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


def make_comparable_string(item: list | str) -> str:
    """Convert a list of strings into a single comparable string."""
    string = " ".join(item) if isinstance(item, list) else str(item)
    string = strip_punctuation(string)
    string = re.sub(r"[0123]", "", string)  # remove stress markers
    return string.casefold()


def convert_to_syllables(phonemes: str | list, ipa: bool = False) -> list:
    """Turn a sequence of phonemes into syllable groups."""
    transcription = phonemes if isinstance(phonemes, str) else " ".join(phonemes)
    if ipa:
        ipa_str = nofabet_to_ipa(transcription)
        syllables = ipa_str.split(".")
    else:
        nofabet_syllables = nofabet_to_syllables(transcription)
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


def split_orthographic_text_into_syllables(words: list[str]) -> list:
    """
    WORK IN PROGRESS
    Split orthographic text into syllables using basic rules.
    This is a simplified implementation and may not handle all edge cases.

    Args:
        words (list of str): A list of orthographic words, already tokenized

    Returns:
        list: A list of syllables for each word in the text.
    """
    syllables = []

    for word in words:
        word_syllables = []
        current_syllable = ""

        for i, char in enumerate(word):
            current_syllable += char

            # Check if the character is a vowel
            if char in VALID_NUCLEI:
                # Check if the next character could be part of the same nucleus
                is_not_last = i + 1 < len(word)
                if is_not_last and word[i + 1] in VALID_NUCLEI:
                    continue

                # Check if the next character could be part of a valid onset
                if is_not_last and word[i + 1] not in VALID_NUCLEI:
                    consonant_cluster = char + word[i + 1]
                    if len(consonant_cluster) > 1 and is_valid_onset(consonant_cluster):
                        continue

                # Otherwise, split the syllable
                word_syllables.append(current_syllable)
                current_syllable = ""

        # Add any remaining characters as a syllable
        if current_syllable:
            word_syllables.append(current_syllable)

        syllables.append(word_syllables)

    return syllables


def is_valid_onset(phonelist: str) -> bool:
    """
    WORK IN PROGRESS
    Check if a sequence of characters forms a valid onset in Norwegian orthography.

    Args:
        phonelist (str): A string representing the onset (e.g., "bl", "tr").

    Returns:
        bool: True if the onset is valid, False otherwise.
    """
    # Define valid single consonants and consonant clusters for Norwegian
    valid_single_consonants = set("bcdfghjklmnpqrstvwxyz")
    valid_clusters = {
        "bj",
        "bl",
        "br",
        "dr",
        "dj",
        "fl",
        "fj",
        "fr",
        "gl",
        "gr",
        "gj",
        "kj",
        "kl",
        "kr",
        "kn",
        "kv",
        "pl",
        "pj",
        "pr",
        "mj",
        "nj",
        "sj",
        "sl",
        "sm",
        "sn",
        "sp",
        "st",
        "sv",
        "tr",
        "tj",
        "tl",
        "vr",
        "sk",
        "skr",
        "spr",
        "str",
        "skj",
        "gn",
        "hv",
    }

    if len(phonelist) == 1 and phonelist in valid_single_consonants:
        return True

    return phonelist in valid_clusters


def annotate_transcriptions(transcription: list) -> Generator:
    for word, pronunciation in transcription:
        nofabet = format_transcription(pronunciation)
        yield {
            "word": word,
            "nofabet": nofabet,
            "syllables": nofabet_to_syllables(nofabet),
            "ipa": nofabet_to_ipa(nofabet),
        }


def split_paragraphs(text: str) -> list:
    """Split a text into paragraphs and paragraphs into lines."""
    return [
        [line.rstrip() for line in paragraph.rstrip().splitlines()]
        for paragraph in re.split("\n{2,}", text)
        if paragraph
    ]


def format_transcription(pronunciation):
    return " ".join(pronunciation)


def gather_stanza_annotations(func) -> Callable:
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
    return [[verse.rstrip() for verse in stanza.rstrip().splitlines()] for stanza in re.split("\n{2,}", text) if stanza]


def normalize(text: str) -> list[str]:
    """Lowercase, remove punctuation and tokenize a string of text."""
    lowercase = text.strip().lower()
    alpanumeric_only = strip_punctuation(lowercase)
    words = tokenize(alpanumeric_only)
    return words


def annotate(func, text: str, stanzaic: bool = False, outputfile: str | Path | None = None):
    if stanzaic:
        new_func = gather_stanza_annotations(func)
        annotations = new_func(text)
    else:
        annotations = func(text)
    if outputfile is not None:
        Path(outputfile).write_text(json.dumps(annotations, indent=4, ensure_ascii=False), encoding="utf-8")
        print(f"Saved annotated data to {outputfile}")
    else:
        return annotations


def save_annotations(annotations: dict | list, outputfile: str | Path | None = None):
    if outputfile is None:
        import time

        outputfile = f"annotations_{int(time.time())}.json"

    Path(outputfile).write_text(json.dumps(annotations, indent=4, ensure_ascii=False), encoding="utf-8")


def group_consecutive_numbers(nums: list[int]) -> list[list[int]]:
    """Group consecutive numbers into sublists.

    Examples:
        >>> list_of_numbers = [1, 2, 3, 5, 6, 8, 9, 10]
        >>> result = group_consecutive_numbers(list_of_numbers)
        >>> print(result)
        [[1, 2, 3], [5, 6], [8, 9, 10]]
    """
    if not nums:
        return []

    nums = sorted(nums)
    result = []
    current_group = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1] + 1:
            current_group.append(nums[i])
        else:
            result.append(current_group)
            current_group = [nums[i]]

    result.append(current_group)
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
