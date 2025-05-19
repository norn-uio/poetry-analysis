import pytest

from poetry_analysis.anaphora import extract_stanza_anaphora


def test_extract_stanza_anaphora_returns_dict_with_single_element_list():
    text = [
        "hello world" + "\n",
        "here we are" + "\n\n",
        "nothing to find here" + "\n",
        "only words that don't repeat",
    ]
    result = extract_stanza_anaphora(text)
    assert len(result.keys()) == len(text)
    assert all(len(repetitions) == 1 for repetitions in result.values())


@pytest.mark.parametrize(
    "phrase_length, phrase",
    [(1, "jeg"), (2, "jeg ser"), (3, "jeg ser på"), (4, "jeg ser på den")],
)
def test_extract_stanza_anaphora_returns_indices_of_all_occurrences(
    phrase_length, phrase
):
    text = [
        "jeg ser på den hvite himmel,\n",
        "jeg ser på den hvite himmel,\n",
        "jeg ser på den hvite himmel,\n",
        "jeg ser på den hvite himmel,\n",
    ]
    result = extract_stanza_anaphora(text, n_words=phrase_length)
    assert len(result[phrase]) == len(text)
    assert all(i == j for i, j in zip(result[phrase], range(len(text))))


def test_extract_stanza_anaphora_skips_empty_line():
    text = [
        "",
        "du ser på den hvite himmel,\n",
        "",
        "jeg ser på den hvite himmel,\n",
        "jeg ser på den hvite himmel,\n",
    ]
    result = extract_stanza_anaphora(text)
    assert len(result["jeg"]) == 2
    assert result["jeg"] == [3, 4], result["jeg"]
