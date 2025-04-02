import pytest

from poetry_analysis import rhyme_detection as rd


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("klangen", "klangen"),
        ("tusenfryd", "fryd"),
        ("avisen", "kulturavisen"),
    ],
)
def test_noedrim_scores_half(word1, word2):
    result = rd.score_rhyme(word1, word2, orthographic=True)
    assert result == 0.5


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("klangen", "sangen"),
        ("bjellen", "makrellen"),
        ("syr", "myr"),
        ("hjerte", "smerte"),
    ],
)
def test_orthographic_proper_rhymes(word1, word2):
    result = rd.score_rhyme(word1, word2, orthographic=True)
    assert result == 1.0


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("G UH L", "J UH L"),
        ("G UH L", "F UH L"),
        ("B OO D", "S T OO D"),
    ],
)
def test_phonemic_proper_rhyme(word1, word2):
    result = rd.score_rhyme(word1, word2, orthographic=False)
    assert result == 1.0


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("klangen", "fryd"),
        ("UU2 F R EH3 D", "L AH2 N AX0"),
        ("S V EH1 N", "SJ IH2 N NX0 AX0"),
    ],
)
def test_different_words_score_zero(word1, word2):
    result = rd.score_rhyme(word1, word2)
    assert result == 0.0


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("sang", "seng"),
        ("song", "sing"),
        ("søym", "draum"),
        ("svei", "sved"),
    ],
)
def test_no_common_vowels_scores_zero(word1, word2):
    result = rd.score_rhyme(word1, word2)
    assert result == 0.0


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("sleden", "bilen"),
        ("husene", "byene"),
        # ("spiste", "lyste"), # Can't handle this case yet
        ("gutane", "tankane"),
        ("fester", "blomster"),
        ("diktet", "brevet"),
        ("arbeidet", "jogget"),
    ],
)
def test_common_grammatical_ending_scores_zero(word1, word2):
    result = rd.score_rhyme(word1, word2)
    assert result == 0.0


@pytest.mark.parametrize(
    "word1, word2",
    [
        ("klangen", "klang"),
        ("klang", "klangen"),
        ("arbeider", "arbeidene"),
        ("klangen", "sang"),
        ("sang", "klangen"),
    ],
)
def test_common_substring_in_start_or_middle_scores_zero(word1, word2):
    result = rd.score_rhyme(word1, word2)
    assert result == 0.0
