import pytest

from poetry_analysis.rhyme_detection import remove_syllable_onset


@pytest.mark.parametrize(
    "syllable, expected",
    [
        (["H", "AH2", "L", "OUH0"], ["AH2", "L", "OUH0"]),
        (["V", "AE1", "RD", "RNX0"], ["AE1", "RD", "RNX0"]),
        (["D", "UU1"], ["UU1"]),
    ],
)
def test_onset_is_removed_for_syllables(syllable, expected):
    result = remove_syllable_onset(syllable)
    assert result == expected


@pytest.mark.parametrize("syllable", ["hello world", "H A L L O", "H EI", ["B", "P", "K", "L"]])
def test_returns_none_when_no_nucleus_is_found(syllable):
    result = remove_syllable_onset(syllable)
    assert result is None
