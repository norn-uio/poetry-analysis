"""The definition of alliteration that we use here is the repetition
of word-initial consonants or consonant clusters.
"""

from pathlib import Path

from poetry_analysis.utils import annotate


def count_alliteration(text: str) -> dict:
    """Count the number of times the same word-initial letter occurs in a text.

    Examples:
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

    alliteration_count = {letter: count for letter, count in initial_counts.items() if count > 1}

    return alliteration_count


def extract_alliteration(text: list[str]) -> list[dict]:
    """Extract words that start with the same letter from a text.

    NB! This function is case-insensitive and compares e.g. S to s as the same letter.

    Args:
        text (list): A list of strings, where each string is a line of text.

    Examples:
        >>> text = ['Stjerneklare Septembernat Sees Sirius', 'Sydhimlens smukkeste Stjerne']
        >>> extract_alliteration(text)
        [{'line': 0, 'symbol': 's', 'count': 4, 'words': ['Stjerneklare', 'Septembernat', 'Sees', 'Sirius']}, {'line': 1, 'symbol': 's', 'count': 3, 'words': ['Sydhimlens', 'smukkeste', 'Stjerne']}]
    """

    alliterations = []

    for i, line in enumerate(text):
        words = line.split() if isinstance(line, str) else line
        seen = {}
        for j, word in enumerate(words):
            initial_letter = word[0].lower()
            if not initial_letter.isalpha():
                continue

            if initial_letter in seen:
                seen[initial_letter].append(word)
            else:
                seen[initial_letter] = [word]

            if (j == len(words) - 1) and any(len(v) > 1 for v in seen.values()):
                alliteration_symbols = [k for k, v in seen.items() if len(v) > 1]
                for symbol in alliteration_symbols:
                    alliterations.append(
                        {
                            "line": i,
                            "symbol": symbol,
                            "count": len(seen[symbol]),
                            "words": seen[symbol],
                        }
                    )

    return alliterations


if __name__ == "__main__":
    # Test the functions with doctest
    import doctest

    doctest.testmod()

    # Parse user arguments
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("textfile", help="Filepath to the text to analyze.")
    parser.add_argument("--split_stanzas", action="store_true", help="Split the text into stanzas.")
    parser.add_argument(
        "-o",
        "--outputfile",
        type=Path,
        help="File path to store results in. Defaults to the same file path and name as the input file, with the additional suffix `_alliteration.json`.",
    )
    args = parser.parse_args()

    # Analyze the text
    filepath = Path(args.textfile)
    text = filepath.read_text()

    if not args.outputfile:
        args.outputfile = Path(filepath.parent / f"{filepath.stem}_alliteration.json")
    annotate(
        extract_alliteration,
        text,
        stanzaic=args.split_stanzas,
        outputfile=args.outputfile,
    )
