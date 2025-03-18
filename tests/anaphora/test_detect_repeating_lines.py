import pytest

from poetry_analysis.anaphora import detect_repeating_lines


def test_detect_repeating_lines_returns_both_linenumber_and_full_line():
    text = (
        "Idag er en fin dag\n"
        + "Hei på deg\n"
        + "Idag er en fin dag\n"
        + "bladibladibla\n"
    )
    result = detect_repeating_lines(text)
    assert result == [
        ([0, 2], "Idag er en fin dag"),
    ]
