from poetry_analysis.utils import shared_final_substring, shared_initial_substring


def test_shared_initial_substring():
    """Test that the longest shared initial substring is correctly identified."""
    assert shared_initial_substring("abc", "abd") == "ab"
    assert shared_initial_substring("abc", "xyz") == ""
    assert shared_initial_substring("abc", "abc") == "abc"
    assert shared_initial_substring("abcde", "abc") == "abc"


def test_shared_final_substring():
    """Test that the longest shared final substring is correctly identified."""
    assert shared_final_substring("abc", "xbc") == "bc"
    assert shared_final_substring("abc", "xyz") == ""
    assert shared_final_substring("abc", "abc") == "abc"
    assert shared_final_substring("abcde", "cde") == "cde"
