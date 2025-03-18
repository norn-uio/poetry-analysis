import pytest

from poetry_analysis import rhyme_detection as rt


@pytest.mark.parametrize(
    "phoneme, expected",
    [
        ("KJ", "KJ"),
        ("AE2", "AE"),
        ("RL", "RL"),
        ("IH1", "IH"),
        ("H", "H"),
        ("EE3", "EE"),
        ("D", "D"),
        ("AX0", "AX"),
        ("N", "N"),
    ],
)
def test_stress_markers_are_removed(phoneme, expected):
    result = rt.strip_stress(phoneme)
    assert result == expected
