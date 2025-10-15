from poetry_analysis.rhyme_detection import Verse, tag_stanzas


def test_tag_stanzas_orthographic_simple():
    # Each stanza is a list of verse lines (strings)
    stanzas = [["rose", "nose", "cat"], ["dog", "fog", "log"]]
    result = list(tag_stanzas(stanzas, orthographic=True))
    assert len(result) == 2
    assert result[0]["stanza_id"] == 0
    assert result[1]["stanza_id"] == 1
    # Check rhyme scheme length matches stanza length
    assert len(result[0]["rhyme_scheme"]) == len(stanzas[0])
    assert len(result[1]["rhyme_scheme"]) == len(stanzas[1])
    # Check verses are annotated
    for stanza in result:
        for verse in stanza["verses"]:
            assert "rhyme_tag" in verse
            assert "rhyme_score" in verse


def test_tag_stanzas_empty_stanza():
    stanzas = [[]]
    result = list(tag_stanzas(stanzas, orthographic=True))
    assert len(result) == 1
    assert result[0]["verses"] == []
