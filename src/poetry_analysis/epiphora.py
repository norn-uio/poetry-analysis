"""Epiphora, or epistrophe, is the repetition of the same word or phrase at the end
of successive clauses in a line, or of successive lines in a stanza.
"""

from poetry_analysis import utils


def extract_epiphora(text_sequence: list[str]) -> dict:
    """Extract overlapping substrings in the end of each text in the `text_sequence`."""
    return utils.extract_repeated_substrings(text_sequence, overlap_position="final")
