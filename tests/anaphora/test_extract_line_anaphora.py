import pytest

from poetry_analysis.anaphora import extract_line_anaphora


@pytest.mark.parametrize(
    "text, expected_phrase, expected_count",
    [
        ("hello hello world", "hello", 2),
        ("hello world hello world hello world", "hello world", 3),
        ("Hei og hopp, hei og hallo, hei og hå", "hei og", 3),
        ("Hei hei hei hei hei", "hei", 5),
    ],
)
def test_extract_line_anaphora_extracts_longest_repeating_sequence(
    text, expected_phrase, expected_count
):
    result = extract_line_anaphora(text)
    actual = result[0]

    assert len(result) == 1
    assert actual["line_id"] == 0
    assert actual["phrase"] == expected_phrase
    assert actual["count"] == expected_count


def test_line_final_word_sequences_return_empty_list():
    text = (
        "Hei hello world hello world" + "\n"
        "Hey hello hello" + "\n\n"
        "hallo world world" + "\n"
        "Ai hello world"
    )
    result = extract_line_anaphora(text)
    assert result == []


def test_lines_without_anaphora_returns_empty_list():
    text = (
        "hello world" + "\n"
        "here we are" + "\n"
        "\n"
        "nothing to find here" + "\n"
        "only words that don't repeat"
    )
    result = extract_line_anaphora(text)
    assert result == []
