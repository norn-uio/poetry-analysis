from poetry_analysis import rhyme_detection as rd



def test_get_stanza_from_transcription_returns_only_orthogtraphic_words():
    # Given 
    poem = {
        "text_id": "test_1",
        "line_0": [["E", "E2"], ["m", "M"]],
        "line_1": [["Det", "D AX0"]]
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
        "line_1": [["Det", "D AX0"]]
    }
    # When
    result = rd.get_stanzas_from_transcription(poem, orthographic=False)
    # Then
    assert result[0][0] == ["EE2 N S AH0 M"]
    assert result[0][1] == ["D AX0"]