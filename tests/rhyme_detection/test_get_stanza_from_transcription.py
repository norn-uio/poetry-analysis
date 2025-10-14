import pytest

from poetry_analysis import rhyme_detection as rd


def test_get_stanza_from_transcription_returns_only_orthogtraphic_words():
    # Given
    poem = {
        "text_id": "test_1",
        "line_0": [["E", "E2"], ["m", "M"]],
        "line_1": [["Det", "D AX0"]],
    }
    # When
    result = rd.get_stanzas_from_transcription(poem, orthographic=True)
    # Then
    assert result[0][0] == ["E", "m"]
    assert result[0][1] == ["Det"]


def test_get_stanza_from_transcription_returns_only_pronunciation():
    # Given
    poem = {
        "text_id": "test_2",
        "line_0": [["Ensom", "EE2 N S AH0 M"]],
        "line_1": [["Det", "D AX0"]],
    }
    # When
    result = rd.get_stanzas_from_transcription(poem, orthographic=False)
    # Then
    assert result[0][0] == ["EE2 N S AH0 M"]
    assert result[0][1] == ["D AX0"]


@pytest.fixture
def transcription_output():
    return {
        "X": "bla",
        "Y": "di",
        "z": "da",
        "line_0": [(1, "line")],
        "line_1": [(2, "line")],
    }


def test_extracting_only_first_elements_in_tuples(transcription_output):
    stanzas = rd.get_stanzas_from_transcription(transcription_output, orthographic=True)
    verses = stanzas[0]
    verse1 = verses[0][0]
    verse2 = verses[1][0]
    assert verse1 == 1
    assert verse2 == 2


def test_extracting_second(transcription_output):
    stanzas = rd.get_stanzas_from_transcription(transcription_output, orthographic=False)
    verses = stanzas[0]
    assert all(obj == "line" for line in verses for obj in line)
