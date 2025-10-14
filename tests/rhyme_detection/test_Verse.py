from poetry_analysis import rhyme_detection as rd


def test_verse_returns_attributes_as_dict():
    verse = rd.Verse(1)
    result = verse.dict
    assert isinstance(result, dict)


def test_verse_dict_renames_initial_id_key():
    verse = rd.Verse(1)
    result = verse.dict
    assert result["verse_id"] == 1
    assert "id_" not in result


def test_verse_also_contains_unset_attributes():
    verse = rd.Verse(1)
    result = verse.dict

    assert "text" in result.keys()
    assert "rhyme_score" in result.keys()
    assert result["last_token"] is None
