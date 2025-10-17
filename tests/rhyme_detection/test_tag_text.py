from poetry_analysis.rhyme_detection import tag_text


def test_full_text_gets_stanzaic_rhyme_schemes(example_poem_landsmaal):
    result = list(tag_text(example_poem_landsmaal))
    assert result[0]["stanza_id"] == 0
    assert result[0]["rhyme_scheme"] == "abcb"
