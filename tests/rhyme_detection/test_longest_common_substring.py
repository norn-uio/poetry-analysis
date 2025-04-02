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
        ("F R YY D", "S YY D"),
        ("S II N", "D II N"),
        ("G UH L", "J UH L"),
        ("G UH2 L", "F UH2 L"),
        ("B OO D", "S T OO D"),
    ],
)
def test_any_common_substring_is_found(sequence1, sequence2):
    result = longest_common_substring(sequence1, sequence2)
    assert result
