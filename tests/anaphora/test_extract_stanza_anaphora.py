from poetry_analysis.anaphora import extract_stanza_anaphora


def test_extract_stanza_anaphora_merges_counts_across_stanzas():
    """Check that the longest repeating line initial word sequences are extracted.
    The count should be the number of lines the sequence is repeated in the stanza.
    """
    text = (
        "Hei på deg" + "\n"
        "Hei og hå" + "\n"
        "Hei sann" + "\n\n"
        "Hei hvor det går" + "\n"
        "Hei og hallo" + "\n"
    )
    expected = {
        "stanza_id": [0, 1],
        "line_id": [0, 1, 2, 3, 4],
        "phrase": "Hei",
        "count": 5,
    }

    result = extract_stanza_anaphora(text)

    assert len(result) == 2

    assert all(r["stanza_id"] == e for r, e in zip(result, expected["stanza_id"]))
    actual_lineids = [r["line_id"] for r in result]
    assert all(
        actual_id in expected["line_id"] for ids in actual_lineids for actual_id in ids
    ), actual_lineids
    assert all(r["phrase"] == expected["phrase"] for r in result)
    assert sum(r["count"] for r in result) == expected["count"]


def test_stanza_returns_most_repeated_word():
    text = (
        "jeg ser verden" + "\n"
        "jeg ser sola" + "\n"
        "jeg myser mot skyene" + "\n"
        "jeg ser havet" + "\n"
    )
    result = extract_stanza_anaphora(text)

    assert len(result) == 1
    actual = result[0]
    assert actual["stanza_id"] == 0
    assert actual["line_id"] == [0, 1, 2, 3]
    assert actual["phrase"] == "jeg"
    assert actual["count"] == 4


def test_extract_stanza_anaphora_returns_empty_list_no_repeated_line_initial_phrase():
    text = (
        "hello world" + "\n"
        "here we are" + "\n"
        "\n"
        "nothing to find here" + "\n"
        "only words that don't repeat"
    )
    result = extract_stanza_anaphora(text)
    assert result == []
