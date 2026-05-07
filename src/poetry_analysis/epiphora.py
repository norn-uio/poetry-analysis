"""Epiphora, or epistrophe, is the repetition of the same word or phrase at the end
of successive clauses in a line, or of successive lines in a stanza.
"""

from typing import Counter

from poetry_analysis import utils


def extract_epiphora(text_sequence: list[str]) -> dict:
    """Extract overlapping substrings in the end of each text in the `text_sequence`."""
    return utils.extract_repeated_substrings(text_sequence, overlap_position="final")


def extract_line_epiphora(text: str) -> dict:
    """Extract final word sequences that are repeated at least twice in the same text string."""
    initial_phrases = utils.count_phrases(text, position="final")
    phrase, count = utils.find_longest_most_frequent_phrase(initial_phrases)
    return {"phrase": phrase, "count": count} if count > 1 and phrase else {}
