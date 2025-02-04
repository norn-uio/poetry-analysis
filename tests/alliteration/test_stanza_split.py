import pytest
from poetry_analysis.alliteration import gather_stanza_annotations


def print_line_number(text:str): 
    lines = []
    for i, line in enumerate(text.split('\n'), 1):
        lines.append(f"{i}: {line}")
    return lines


def test_gather_stanza_annotations_splits_double_newlines():
    text = "Stanza 1\nLine 1\nLine 2\n\nStanza 2\nLine 1\nLine 2"
    result_whole_text = print_line_number(text)
    result_stanza_annotations = gather_stanza_annotations(print_line_number)(text)

    assert len(result_whole_text) == 7
    assert result_whole_text == pytest.approx(["1: Stanza 1", "2: Line 1", "3: Line 2", "4: ", "5: Stanza 2", "6: Line 1", "7: Line 2"])
    assert len(result_stanza_annotations) == 2
    assert result_stanza_annotations == pytest.approx({"stanza_1": ["1: Stanza 1", "2: Line 1", "3: Line 2"], "stanza_2": ["1: Stanza 2","2: Line 1", "3: Line 2"]})
