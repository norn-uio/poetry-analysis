import pytest 
from poetry_analysis.rhyme_detection import longest_common_substring

@pytest.mark.parametrize(
    "sequence1, sequence2",
    [
        ("klangen", "klang"),
        ("klang", "klangen"),
        ("arbeider", "arbeidene"),
        ("klangen", "sang"),
        ("sang", "klangen"),
        (["F", "R", "YY1", "D"], ["S", "YY1", "D"]),
        (["S", "II1", "N"], ["D", "II2", "N"]),
        ("F R YY1 D", "S YY1 D"),
        ("S II1 N", "D II2 N"),
    ]
)
def test_any_common_substring_is_found(sequence1, sequence2):

    result = longest_common_substring(sequence1, sequence2)
    assert result

