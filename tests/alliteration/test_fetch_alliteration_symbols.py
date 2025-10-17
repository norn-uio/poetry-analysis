from poetry_analysis.alliteration import fetch_alliteration_symbols


def test_fetch_alliteration_symbols_returns_multiple_letters():
    test_input = [["group1", "group1-word2", "g"], ["word1", "word2"], ["last1"]]
    result = fetch_alliteration_symbols(test_input)
    assert result[0] == "g"
    assert result[1] == "w"
    assert result[2] == "l"


def test_fetch_alliteration_symbols_returns_empty_list_for_empty_input():
    test_input = []

    result = fetch_alliteration_symbols(test_input)
    assert result == []
