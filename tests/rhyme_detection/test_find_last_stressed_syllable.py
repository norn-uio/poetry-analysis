import pytest

from poetry_analysis import rhyme_detection as rt


@pytest.mark.parametrize(
    "indata, expected",
    [
        (
            [
                ["KJ", "AE2"],
                ["L", "IH0"],
                ["H", "EE3"],
                ["D", "NX0"],
                ["KJ", "EH2", "N"],
                ["T", "AX0"],
                ["D", "UU1"],
                ["D", "EH1", "N", "S"],
                ["OAH1", "N"],
            ],
            ["OAH1", "N"],
        ),
        (
            [
                ["K", "L", "IH2"],
                ["P", "AX0"],
                ["S", "T", "AEH3", "R"],
                ["K", "AX0"],
                ["KJ", "AE2"],
                ["RL", "IH0"],
                ["H", "EE3"],
                ["D", "NX0", "S"],
                ["B", "OAH1", "N"],
            ],
            ["B", "OAH1", "N"],
        ),
        (
            [
                ["S", "T", "OEH3"],
                ["R", "AX0"],
                ["D", "YY1", "D"],
                ["P", "OAH0"],
                ["J", "OO1", "R"],
                ["AEJ1"],
                ["N", "AE2", "V"],
                ["N", "AX0", "S"],
                ["K", "AH0", "N"],
            ],
            ["N", "AE2", "V", "N", "AX0", "S", "K", "AH0", "N"],
        ),
        (
            [
                ["EH1", "N", "D"],
                ["D", "AX0", "N"],
                ["EE2", "D"],
                ["L", "AX0"],
                ["KJ", "AE2"],
                ["RL", "IH0"],
                ["H", "EE3"],
                ["D", "NX0", "S"],
                ["B", "R", "AH1", "N"],
            ],
            ["B", "R", "AH1", "N"],
        ),
    ],
)
def test_find_last_stressed_syllable(indata, expected):
    """Check that the last syllable with a stress marker
    higher than 0 in a syllable sequence is the first syllable
    in the output sequence."""
    # when
    result = rt.find_last_stressed_syllable(indata)
    # then
    assert result == expected
