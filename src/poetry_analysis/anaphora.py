"""Anaphora is the repetition of the same line-initial word or phrase
in a verse, or across consecutive verses in a stanza.
"""

import warnings
from collections import Counter, defaultdict
from collections.abc import Generator

import pandas as pd

from poetry_analysis import utils


def count_initial_phrases(text: str) -> Counter:
    """Count the number of times string-initial phrases of different lengths occur in a string."""
    phrase_counts = Counter()
    normalized_text = utils.normalize_string(text)
    words = utils.tokenize(normalized_text)
    n_words = len(words)

    for n in range(1, n_words + 1):
        if len(words) >= n:
            phrase = " ".join(words[:n])
            count = normalized_text.count(phrase)
            if count > 0:
                phrase_counts[phrase] += count
    return phrase_counts


def find_longest_most_frequent_anaphora(phrases: Counter) -> tuple:
    """Find the longest and most repeated word sequence in a counter."""
    if phrases:
        _, highest_count = phrases.most_common()[0]
        top_phrases = [phrase for phrase, _ in phrases.most_common() if phrases[phrase] == highest_count]

        longest_phrase = max(top_phrases, key=len)
        longest_count = phrases[longest_phrase]

        return longest_phrase, longest_count
    return ("", 0)


def extract_line_anaphora_old(text: str) -> list:
    """Extract line initial word sequences that are repeated at least twice on the same line.

    Deprecated.
    """
    anaphora = []
    lines = text.strip().splitlines()
    for i, line in enumerate(lines):
        line_initial_phrases = count_initial_phrases(line)
        phrase, count = find_longest_most_frequent_anaphora(line_initial_phrases)
        if count > 1:
            annotation = {"line_id": i, "phrase": phrase, "count": count}
            anaphora.append(annotation)
    return anaphora


def is_successive(items: list[int]) -> list[bool]:
    """Assert whether all numbers in a list are monotonic and incremental."""
    return [items[i] == items[i - 1] + 1 for i, item in enumerate(items)][1:]


def filter_anaphora(stanza_anaphora: dict) -> Generator:
    """Construct and yield an annotation dictionary
    only for stanzas where anaphora are immediately successive."""
    for phrase, indeces in stanza_anaphora.items():
        if len(indeces) <= 1:
            continue
        if all(is_successive(indeces)):
            annotation = {
                "line_id": indeces,
                "phrase": phrase,
                "count": len(indeces),
            }
            yield annotation


def extract_stanza_anaphora(stanza: list[str], n_words: int = 1) -> dict:
    """Gather indeces for all lines that a line-initial word repeats across successively.

    DEPRECATED: This function is deprecated and should not be used in new code. It is only kept for reference.

    Args:
        n_words: Number of words to expect in the anaphora, must be 1 or higher.
            If higher, a single word that is repeated more often than a phrase of
            n_words will be ignored in favour of the less frequent phrase.
    """
    stanza_anaphora = {}
    empty_list = []
    lines = [utils.normalize_tokens(line) if line else empty_list for line in stanza]
    for line_index, words in enumerate(lines):
        if not words:
            continue

        first_phrase = " ".join(words[:n_words])
        if line_index == 0:
            stanza_anaphora[first_phrase] = [line_index]
            continue

        previous_line = lines[line_index - 1]
        try:
            previous_first_phrase = " ".join(previous_line[:n_words])
        except IndexError:
            previous_first_phrase = None

        if line_index > 0 and previous_first_phrase == first_phrase:
            stanza_anaphora[first_phrase].append(line_index)
        else:
            stanza_anaphora[first_phrase] = [line_index]

    return stanza_anaphora


def extract_poem_anaphora(text: str) -> list:
    """Extract line-initial word sequences that are repeated at least twice in each stanza."""
    anaphora = []

    stanzas = utils.split_stanzas(text)
    for i, stanza in enumerate(stanzas):
        stanza_anaphora = extract_stanza_anaphora(stanza)

        for item in filter_anaphora(stanza_anaphora):
            item["stanza_id"] = i
            anaphora.append(item)

    return anaphora


def detect_repeating_lines(text: str) -> list:
    """Detect repeating lines in a poem."""
    stanzas = utils.split_stanzas(text)
    lines = [line.strip() for stanza in stanzas for line in stanza]

    repeating_lines = {}
    for idx, line in enumerate(lines):
        if line in repeating_lines:
            repeating_lines[line].append(idx)
        else:
            total = lines.count(line)
            if total > 1:
                repeating_lines[line] = [idx]

    return [(indeces, line) for line, indeces in repeating_lines.items()]


def extract_anaphora_old(text: str) -> dict:
    """Extract line-initial word sequences that are repeated at least twice.

    Warning:
        This function is deprecated and should not be used in new code. It is only kept for reference.

    Examples:
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
        >>> result = extract_anaphora_old(text)
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
    warnings.warn(
        "extract_anaphora_old is deprecated and will be removed in a future version.", DeprecationWarning, stacklevel=2
    )
    lines = text.strip().lower().splitlines()
    ngram_counts = defaultdict(lambda: defaultdict(int))

    for line in lines:
        text = utils.strip_punctuation(line)
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


def construct_anaphora_df(df: pd.DataFrame, anaphora_length: int = 1) -> pd.DataFrame:
    """Extract anaphora from a stanza in a dataframe"""
    dfs = []

    for (poem_id, stanza_id), df_ in df.groupby(["poem_id", "stanza_id"]):
        text = df_.text.dropna().tolist()
        stanza_anaphora = extract_stanza_anaphora(text, n_words=anaphora_length)
        for phrase, indices in stanza_anaphora.items():
            if len(indices) <= 1:
                continue
            if all(is_successive(indices)):
                annotation = {
                    "poem_id": poem_id,
                    "stanza_id": int(stanza_id),  # type: ignore PGH003
                    "line_id": indices,
                    "phrase": phrase,
                    "count": len(indices),
                    "text": [text[i] for i in indices],
                }

                dfs.append(pd.DataFrame([annotation]))

    if not dfs:
        # Return an empty DataFrame with the expected columns
        columns = ["poem_id", "stanza_id", "line_id", "phrase", "count", "text"]
        return pd.DataFrame(columns=columns)

    anaphora_df = pd.concat(dfs).reset_index(drop=True)
    return anaphora_df


def extract_anaphora(text_sequence: list[str]) -> dict:
    """Extract overlapping substrings in the beginning of each text in the `text_sequence`."""
    return utils.extract_repeated_substrings(text_sequence, overlap_position="initial")


def extract_line_anaphora(text: str) -> dict:
    """Extract initial word sequences that are repeated at least twice in the same text string."""
    initial_phrases = count_initial_phrases(text)
    phrase, count = find_longest_most_frequent_anaphora(initial_phrases)
    return {"phrase": phrase, "count": count} if count > 1 and phrase else {}


if __name__ == "__main__":
    import doctest

    doctest.testmod()
