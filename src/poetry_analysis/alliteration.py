"""Alliteration is the repetition of word-initial
consonants or consonant clusters.

Anaphore is the repetition of the same word or phrase
at the beginning of successive clauses or sentences.
"""

import json
from collections import defaultdict
from pathlib import Path

from poetry_analysis.rhyme_detection import split_stanzas
from poetry_analysis.utils import strip_punctuation


# %%
def count_alliteration(text: str) -> dict:
    """Count the number of times the same word-initial letter occurs in a text.

    Example use:
    >>> text = "Sirius som seer"
    >>> count_alliteration(text)
    {'s': 3}
    """
    words = text.split()
    initial_counts = {}

    for word in words:
        initial_letter = word[0].lower()
        if initial_letter in initial_counts:
            initial_counts[initial_letter] += 1
        else:
            initial_counts[initial_letter] = 1

    alliteration_count = {
        letter: count for letter, count in initial_counts.items() if count > 1
    }

    return alliteration_count


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


@gather_stanza_annotations
def extract_alliteration(text: str) -> dict:
    """Extract words that start with the same letter from a text.

    NB! This function is case-insensitive and returns alphabetically sorted lists of unique words.

    Example use:
    >>> text = "Stjerneklare Septembernat Sees Sirius, Sydhimlens smukkeste Stjerne"
    >>> extract_alliteration(text)
    {'s': ['Sees', 'Septembernat', 'Sirius,', 'Stjerne', 'Stjerneklare', 'Sydhimlens', 'smukkeste']}
    """
    words = text.split()
    alliterations = {}

    for i, current_word in enumerate(words):
        for k in range(i + 1, len(words)):
            next_word = words[k]

            initial_letter = current_word[0].lower()
            next_initial_letter = next_word[0].lower()

            if initial_letter.lower() == next_initial_letter.lower():
                if initial_letter in alliterations:
                    alliterations[initial_letter].add(next_word)
                else:
                    alliterations[initial_letter] = {current_word, next_word}
    sorted_alliterations = {
        k: sorted(list(v)) for k, v in alliterations.items() if len(v) > 1
    }

    return sorted_alliterations


def extract_anaphora(text: str) -> dict:
    """Extract line-initial word sequences that are repeated at least twice.

    Example use:
    >>> import json
    >>> text = '''
    ... Jeg ser paa den hvide himmel,
    ... jeg ser paa de graablaa skyer,
    ... jeg ser paa den blodige sol.
    ...
    ... Dette er altsaa verden.
    ... Dette er altsaa klodernes hjem.
    ...
    ... En regndraabe!
    ... '''
    >>> result = extract_anaphora(text)
    >>> print(json.dumps(result, indent=4))
    {
        "1-grams": {
            "jeg": 3,
            "dette": 2
        },
        "2-grams": {
            "jeg ser": 3,
            "dette er": 2
        },
        "3-grams": {
            "jeg ser paa": 3,
            "dette er altsaa": 2
        },
        "4-grams": {
            "jeg ser paa den": 2
        }
    }
    """
    lines = text.strip().lower().split("\n")
    ngram_counts = defaultdict(lambda: defaultdict(int))

    for line in lines:
        text = strip_punctuation(line)
        words = text.split()
        n_words = len(words)
        for n in range(1, n_words + 1):
            if len(words) >= n:
                ngram = " ".join(words[:n])
                ngram_counts[n][ngram] += 1

    anaphora = {}
    for n in range(1, 5):
        ngram_type = f"{n}-grams"
        ngrams = {ngram: count for ngram, count in ngram_counts[n].items() if count > 1}
        if ngrams:
            anaphora[ngram_type] = ngrams
    return anaphora


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
    import argparse

    # Test the functions with doctest
    doctest.testmod()

    # Parse user arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("textfile", help="Filepath to the text to analyze.")
    parser.add_argument(
        "--alliteration",
        action="store_true",
        help="Extract alliteration from the text.",
    )
    parser.add_argument(
        "--anaphora", action="store_true", help="Extract anaphora from the text."
    )
    parser.add_argument(
        "--split_stanzas", action="store_true", help="Split the text into stanzas."
    )
    args = parser.parse_args()

    # Analyze the text
    filepath = Path(args.textfile)
    text = filepath.read_text()

    if args.alliteration:
        output_file = Path(filepath.parent / f"{filepath.stem}_alliteration.json")
        annotate(extract_alliteration, text, outputfile=output_file)
    if args.anaphora:
        output_file = Path(filepath.parent / f"{filepath.stem}_anaphora.json")
        annotate(
            extract_anaphora, text, stanzaic=args.split_stanzas, outputfile=output_file
        )
