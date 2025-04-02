from poetry_analysis import rhyme_detection as rd


def test_noedrim_scores_half():
    word1 = "tusenfryd"
    word2 = "fryd"
    result = rd.score_orthographic_rhyme(word1, word2)
    assert result == 0.5

def test_proper_rhyme_scores_full():
    word1 = "klangen"
    word2 = "sangen"
    result = rd.score_orthographic_rhyme(word1, word2)
    assert result == 1.0


def test_no_rhyme_scores_zero():
    word1 = "klangen"
    word2 = "fryd"
    result = rd.score_orthographic_rhyme(word1, word2)
    assert result == 0.0
