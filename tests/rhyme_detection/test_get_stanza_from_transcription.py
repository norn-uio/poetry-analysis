from poetry_analysis import rhyme_detection as rd



def test_get_stanza_from_transcription():
    # Given 
    poem = {
        "text_id": "test_1",
        "line_0": [["E", "E2"], ["m", "M"]],
        "line_1": [["Det", "D AX0"]]
    }

    # When
    result = rd.get_stanzas_from_transcription(poem)
    # Then
    assert result[0][0] == [["E2"], ["M"]]
    assert result[0][1] == [["D", "AX0"]]