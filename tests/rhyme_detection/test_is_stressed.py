import pytest

from poetry_analysis import rhyme_detection as rt


@pytest.mark.parametrize(
    "syllable",
    [
        "AE1",
        ["H", "EE3", "D"],
        ["H", "EH1", "D"],
        "L IH2 T AX0",
        "K AE2 N",
    ],
)
def test_vowels_with_toneme_or_secondary_stress_markers_are_stressed(syllable):
    """Test that stress markers are correctly identified."""
    # when
    result = rt.is_stressed(syllable)
    # then
    assert result


@pytest.mark.parametrize(
    "vowel",
    [
        "AE",
        "IH",
        "EH",
        "UW",
        "AA",
        "AH",
        "AO",
        "IY",
        "UH",
        "OW",
        "AW",
        "OY",
        "ER",
        "AX",
        "IX",
    ],
)
def test_vowels_without_stress_markers_are_not_stressed(vowel):
    """Test that vowels without stress markers are not stressed."""
    # when
    result = rt.is_stressed(vowel)
    # then
    assert not result


@pytest.mark.parametrize("schwa", ["AX0", "AX0 N", "AX0 N AX0", "AX0 R"])
def test_schwa_is_not_stressed(schwa):
    """Test that schwa is not stressed."""
    # when
    result = rt.is_stressed(schwa)
    # then
    assert not result
