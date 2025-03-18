import pytest

from poetry_analysis import rhyme_detection as rt


@pytest.mark.parametrize(
    "syllable1, syllable2",
    [
        [["EE1", "N"], ["EE1", "N"]],
        [["T", "UH1"], ["T", "UH1"]],
    ],
)
def test_returns_True_when_syllable_sequences_are_identical(syllable1, syllable2):
    result = rt.do_syll_seqs_rhyme(syllable1, syllable2)
    assert result


@pytest.mark.parametrize(
    "syllable1, syllable2",
    [
        [
            ["S", "T", "A1", "V", "E2", "L", "S", "E0"],
            ["S", "T", "A2", "V", "E3", "L", "S", "E1"],
        ],
        [["L", "IH3", "K"], ["L", "IH2", "K"]],
        [["AX0", "N"], ["AX1", "N"]],
    ],
)
def test_returns_True_when_same_vowels_have_different_stress_marker(
    syllable1, syllable2
):
    result = rt.do_syll_seqs_rhyme(syllable1, syllable2)
    assert result


@pytest.mark.parametrize(
    "syllable1, syllable2",
    [
        [["S", "T", "A1", "V", "E2", "L", "S", "E0"], ["U", "L", "I1", "K"]],
        [["N", "EH1", "S", "T", "AX0", "N"], ["N", "EE1", "S", "T", "EE0", "N"]],
    ],
)
def test_returns_false_when_syllable_sequences_are_different(syllable1, syllable2):
    result = rt.do_syll_seqs_rhyme(syllable1, syllable2)
    assert not result
