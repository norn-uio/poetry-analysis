import pytest
from poetry_analysis import rhyme_detection as rd


def test_shared_ending_substring():
    string1 = "skamfuld"
    string2 = "skamguld"

    result = rd.shared_ending_substring(string1, string2)
    
    assert result == "uld"


def test_shared_ending_substring_no_match():
    string1 = "skamfullt"
    string2 = "skammen"

    result = rd.shared_ending_substring(string1, string2)
    
    assert result == ""


def test_shared_ending_substring_transcription():
    string1 = "S T OO D"
    string2 = "B OO D"

    result = rd.shared_ending_substring(string1, string2).strip()
    
    assert result == "OO D"


@pytest.mark.parametrize(
    "sequence1, sequence2",
    [
        ("klangen", "klang"),
        ("klang", "klangen"),
        ("arbeider", "arbeidene"),
        ("klangen", "sang"),
        ("sang", "klangen"),
    ],
)
def test_no_shared_ending_substring_is_found(sequence1, sequence2):
    result = rd.shared_ending_substring(sequence1, sequence2)
    assert not result


@pytest.mark.parametrize(
    "sequence1, sequence2",
    [
        (["F", "R", "YY1", "D"], ["S", "YY1", "D"]),
        (["S", "II1", "N"], ["D", "II2", "N"]),
        ("F R YY D", "S YY D"),
        ("S II N", "D II N"),
        ("G UH L", "J UH L"),
        ("G UH2 L", "F UH2 L"),
        ("B OO D", "S T OO D"),
])
def test_shared_ending_substring_phonemic(sequence1, sequence2):
    result = rd.shared_ending_substring(sequence1, sequence2)
    assert result
