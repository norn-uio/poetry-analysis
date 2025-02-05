import pytest
from poetry_analysis.rhyme_detection import score_rhyme


@pytest.mark.parametrize("syllable1, syllable2",[
    ([["F", "R", "YY1", "D"]], [["S", "YY1", "D"]]),
    ([["S", "II1", "N"]], [["D", "II2", "N"]]),
]) 
def test_score_rhyme_returns_1_when_rhyme_has_different_onsets(syllable1, syllable2): 
    result = score_rhyme(syllable1, syllable2)
    assert result == 1


@pytest.mark.parametrize("syllable1, syllable2",[
    ([["F", "R", "YY1", "D"]], [["F", "R", "YY1", "D"]]),
    ([["S", "II1", "N"]], [["S", "II1", "N"]]),
    ([["IH1"], ["G", "AH1", "NG"]], [["P", "OAH1"], ["G", "AH1", "NG"]])
]) 
def test_score_rhyme_returns_half_score_when_rhyme_has_same_onsets(syllable1, syllable2): 
    result = score_rhyme(syllable1, syllable2)
    assert result == 0.5


@pytest.mark.parametrize("syllable1, syllable2",[
    ([["F", "R", "YH1", "D"]], [["F", "R", "YY1", "D"]]),
    ([["S", "IH1", "N"]], [["S", "II0", "N"]]),
]) 
def test_score_rhyme_returns_0_when_rhyme_has_different_vowels(syllable1, syllable2): 
    result = score_rhyme(syllable1, syllable2)
    assert result == 0
