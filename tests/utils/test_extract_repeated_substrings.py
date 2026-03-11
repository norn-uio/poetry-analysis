import pytest

from poetry_analysis.utils import extract_repeated_substrings


@pytest.mark.parametrize(
    "text_sequence,expected_overlap",
    (
        (["abcde", "abc", "abcd", "xyz"], "abc"),
        (["a b c d", "a b c", "a b c d", "x y z"], "a b c"),
        (
            [
                """abcd
        blablabla
        something else
        """,
                """abcd
        new stuff
        different content
        """,
                """abcd
        another new line
        and now for something
        completely different
        """,
            ],
            "abcd",
        ),
    ),
)
def test_extract_repeated_substrings_identify_longest_initial_word_overlap(text_sequence, expected_overlap):
    """Test that repeated substrings are correctly extracted."""
    result = extract_repeated_substrings(text_sequence, overlap_position="initial")

    assert result[1]["overlap"] == result[2]["overlap"] == expected_overlap
