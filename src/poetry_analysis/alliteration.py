"""Alliteration is the repetition of word-initial
consonants or consonant clusters.
"""

from pathlib import Path

from poetry_analysis.utils import annotate, gather_stanza_annotations


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


if __name__ == "__main__":
    # Test the functions with doctest
    import doctest
    doctest.testmod()

    # Parse user arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("textfile", help="Filepath to the text to analyze.")
    parser.add_argument(
        "--split_stanzas", action="store_true", help="Split the text into stanzas."
    )
    parser.add_argument(
        "-o", "--outputfile", type=Path, help="File path to store results in. Defaults to the same file path and name as the input file, with the additional suffix `_alliteration.json`.",
    )
    args = parser.parse_args()

    # Analyze the text
    filepath = Path(args.textfile)
    text = filepath.read_text()

    if not args.outputfile:
        args.outputfile = Path(filepath.parent / f"{filepath.stem}_alliteration.json")
    annotate(extract_alliteration, text, stanzaic=args.split_stanzas, outputfile=args.outputfile)
