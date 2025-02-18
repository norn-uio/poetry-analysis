from poetry_analysis.anaphora import extract_line_anaphora


def test_extract_line_anaphora_extracts_longest_repeating_sequence():
    text = "hello hello world\nhello world hello world hello world"
    expected = [{
        "line":0,
        "phrase": "hello",
        "count": 2,
    }, {
        "line":1,
        "phrase": "hello world",
        "count": 3,
    }]
    result = extract_line_anaphora(text)
    assert result == expected


def test_line_final_word_sequences_return_empty_list():
    text = (
        "Hei hello world hello world" + "\n"
        "Hey hello hello" + "\n\n"
        "hallo world world"+ "\n"
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
