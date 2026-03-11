import pytest

from poetry_analysis.anaphora import extract_line_anaphora


@pytest.mark.parametrize(
    "text, expected_phrase, expected_count",
    [
        ("hello hello world", "hello", 2),
        ("hello world hello world hello world", "hello world", 3),
        ("Hei og hopp, hei og hallo, hei og hå", "hei og", 3),
        ("Hei hei hei hei hei", "hei", 5),
        ("Her kommer sola, her kommer varmen, nå er det sommer", "her kommer", 2),
    ],
)
def test_extract_line_anaphora_extracts_longest_repeating_sequence(text, expected_phrase, expected_count):
    result = extract_line_anaphora(text)

    assert result["phrase"] == expected_phrase
    assert result["count"] == expected_count


def test_line_final_word_sequences_return_empty():
    text = "Hei hello world hello world" + "\nHey hello hello" + "\n\nhallo world world" + "\nAi hello world"
    result = extract_line_anaphora(text)
    assert result == {}


def test_lines_without_anaphora_returns_empty():
    text = "hello world" + "\nhere we are" + "\n\nnothing to find here" + "\nonly words that don't repeat"
    result = extract_line_anaphora(text)
    assert result == {}
