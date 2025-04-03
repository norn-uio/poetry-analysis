import pytest

from poetry_analysis import rhyme_detection as rt


def test_find_last_stressed_syllable():
    """Check that the last syllable with a stress marker
    higher than 0 in a syllable sequence is the first syllable
    in the output sequence."""
    syllables = [
        "H AA1 R",
        "D UU1",
        "H OE1",
        "RT EE1 N",
        "M EE2 G",
        "T IH0",
        "S T EH2",
        "M AX0",
    ]
    # when
    result = rt.find_last_stressed_syllable(syllables)
    # then
    assert result == ["S T EH2", "M AX0"]
