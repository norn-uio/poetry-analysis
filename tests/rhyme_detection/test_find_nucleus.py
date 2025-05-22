import pytest

from poetry_analysis import rhyme_detection as rd


@pytest.mark.parametrize(
    "word, expected",
    [
        ("Der", "e"),
        ("var", "a"),
        ("Bælter", "æ"),
        ("af", "a"),
        ("Silke", "i"),
        ("og", "o"),
        ("Ringer", "i"),
        ("af", "a"),
        ("Guld", "u"),
    ],
)
def test_find_correct_orthographic_nucleus(word, expected):
    nucleus = rd.find_nucleus(word, orthographic=True)
    assert nucleus
    result = nucleus.group(1)
    assert result == expected


@pytest.mark.parametrize(
    "word, expected",
    [
        ("EE1 N", "EE"),
        ("V AH2 N D R AX0 N AX0", "AH"),
        ("S V EH1 N", "EH"),
        ("M EE1", "EE"),
        ("S II1 N", "II"),
        ("KJ OE2 P M AH0 N S B OO3 D", "OE"),
    ],
)
def test_find_correct_phonemic_nucleus(word, expected):
    nucleus = rd.find_nucleus(word, orthographic=False)
    assert nucleus
    result = nucleus.group(1)
    assert result == expected
