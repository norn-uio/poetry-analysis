from poetry_analysis.anaphora import extract_line_anaphora


def test_extract_line_anaphora():
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
