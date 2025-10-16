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


# New helper function to group indices considering stop words
def group_alliterating_indices(indices: list, all_words_in_line: list, stop_words: list):
    """
    Groups indices of words that alliterate, allowing specified stop_words in between.
    """
    if not indices:
        return []

    result_groups = []
    current_group_indices = [indices[0]]

    for i in range(1, len(indices)):
        prev_allit_idx = current_group_indices[-1]
        current_potential_idx = indices[i]

        can_extend_group = True
        # Check words between prev_allit_idx and current_potential_idx
        if current_potential_idx > prev_allit_idx + 1:
            for intervening_idx in range(prev_allit_idx + 1, current_potential_idx):
                if (
                    intervening_idx >= len(all_words_in_line)
                    or not all_words_in_line[intervening_idx]
                    or all_words_in_line[intervening_idx].lower() not in stop_words
                ):
                    can_extend_group = False
                    break

        if can_extend_group:
            current_group_indices.append(current_potential_idx)
        else:
            # Store group if it has at least 2 alliterating words
            if len(current_group_indices) >= 2:
                result_groups.append(list(current_group_indices))  # Store a copy
            current_group_indices = [current_potential_idx]

    # Add the last formed group if it's valid
    if len(current_group_indices) >= 2:
        result_groups.append(list(current_group_indices))

    return result_groups


def find_line_alliterations(text: str | list, allowed_intervening_words: list | None = None):
    """Find alliterations on a line."""
    if allowed_intervening_words is None:
        allowed_intervening_words = ["og", "i", "er"]

    if isinstance(text, list):
        words = text
    elif isinstance(text, str):
        words = utils.normalize(text)
    elif text is None:
        words = list()

    # Stores {initial_letter: [indices_of_words_starting_with_this_letter]}
    seen = {}
    for j, word_token in enumerate(words):
        if not word_token:  # Handle potential empty strings from tokenizer
            continue
        # Ensure word_token is not empty before accessing word_token[0]
        if not word_token[0].isalpha():
            continue
        initial_letter = word_token[0].lower()

        if initial_letter in seen:
            seen[initial_letter].append(j)
        else:
            seen[initial_letter] = [j]

    alliteration_annotations = []
    # This part of the logic seems to run only once if the original condition was met.
    # Assuming the goal is to find all alliterations in the line:
    # Check if any letter appears more than once
    if any(len(idx_list) > 1 for idx_list in seen.values()):
        for symbol, positions in seen.items():
            if is_vowel(symbol):  # Only extract consonant alliterations
                continue
            if len(positions) > 1:  # Need at least two words starting with this letter
                # Group indices considering allowed intervening words
                alliterating_groups = group_alliterating_indices(positions, words, allowed_intervening_words)

                for group_indices in alliterating_groups:
                    # group_alliterating_indices already ensures len(group_indices) >= 2
                    alliteration_annotations.append([words[p] for p in group_indices])

    return alliteration_annotations if alliteration_annotations else None


def is_vowel(symbol: str) -> bool:
    vowels = "aeiouyøæå"
    return symbol.casefold() in vowels


# Hent ut antall ord for den lengste rekken med alliterasjoner per verselinje
def count_alliterations(annotations):
    if annotations is None:
        return
    counter = [len(allit) for allit in annotations]
    return max(counter)


def fetch_alliteration_symbol(words: list):
    symbol = ""
    if words is not None:
        for group in words:
            symbol += group[0][0]
    return symbol if symbol else None
