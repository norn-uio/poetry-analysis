"""Test the transcriber module."""

import pytest

from poetry_analysis import utils


@pytest.mark.parametrize(
    "indata, expected",
    [(",", True), (".", True), ("a", False), ("-", True), ("!", True), ("–", True)],
)
def test_is_punctuation(indata, expected):
    """Test that punctuation is correctly identified."""
    # when
    result = utils.is_punctuation(indata)
    # then
    assert result == expected


def test_strip_punctuation():
    """Test that punctuation and additional white space is stripped from a text."""
    text = "De; mumler, dæmpet – og: suger paa Piben,"
    expected = "De mumler dæmpet og suger paa Piben"
    result = utils.strip_punctuation(text)
    assert result == expected


@pytest.mark.parametrize(
    "indata, expected",
    [
        ([["Kvass", "K V AH2 S"], ["som", "S OAH0 M"], ["kniv", "K N II1 V"]], 3),
        (
            [
                ["i", "IH0"],
                ["daudkjøt", "D AEW2 KJ OE3 T"],
                ["flengjande", "F L EH2 N J AH0 N D AX0"],
            ],
            6,
        ),
        ([["Sanningstyrst", "S AH2 N IH0 NG S T YY0 RS RT"]], 3),
        (
            [
                ["mot", "M OO1 T"],
                ["ljoset", "J OO1 S AX0"],
                ["trengjande", "T R EH2 N J AH0 N D AX0"],
            ],
            6,
        ),
    ],
)
def test_syllabify_returns_list_of_syllables(indata, expected):
    """Test that text gets split into syllables"""
    # when
    result = utils.syllabify(indata)
    # then
    assert len(result) == expected
