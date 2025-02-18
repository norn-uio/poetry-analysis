import pytest
from poetry_analysis.anaphora import extract_stanza_anaphora


@pytest.mark.parametrize("text, expected", [
    (
        (
            "Hei på deg" + "\n"
            "Hei og hå" + "\n"
            "Hei sann" + "\n\n"
            "Hei hvor det går" +"\n"
            "Hei og hallo" + "\n"
        ),[{
            "stanza_id": [0,1], 
            "line_id": [0,1,2,3,4],
            "phrase": "Hei",
            "count": 5
            },
        ]
    ), (
        (
            "jeg ser verden"+"\n"
            "jeg ser sola" + "\n"
            "jeg myser mot skyene" + "\n"
            "jeg ser havet" + "\n"
        ),{"stanza_id": 0, "line_id": [0,1,3], "phrase": "jeg ser", "count": 3}
    ), (
        (
            "hello world hello world hello world"+"\n"
            "hello world hello world" + "\n\n"
            "hello world"+ "\n"
            "hello world"
        ),{"stanza_id": 0, "line_id": [0,1,2,3], "phrase": "hello world", "count": 4}
    )
])
def test_extract_stanza_anaphora_finds_longest_repeated_word_sequence(text, expected):
    """Check that the longest repeating line initial word sequences are extracted.
    The count should be the number of lines the sequence is repeated in the stanza.
    """
    result = extract_stanza_anaphora(text)

    assert len(result) == 1
    assert result[0]["line_id"] == expected["line_id"]
    assert result[0]["phrase"] == expected["phrase"]
    assert result[0]["count"] == expected["count"]


def test_extract_stanza_anaphora_returns_empty_list():
    text = (
        "hello world" + "\n"
        "here we are" + "\n"
        "\n"
        "nothing to find here" + "\n"
        "only words that don't repeat"
    )
    result = extract_stanza_anaphora(text)
    assert result == []
