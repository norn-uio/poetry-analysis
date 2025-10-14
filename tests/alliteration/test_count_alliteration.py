from poetry_analysis.alliteration import count_alliteration


def test_alliteration_returns_initial_consonant_counts():
    """Test that the function returns the count of word-initial consonants."""
    # Given
    text = """Stjerneklare Septembernat
Sees Sirius,
Sydhimlens smukkeste
Stjerne,
Solens skjønneste Søster,
Svæve saa stille,
Straale saa smukt,
Skue sørgmodigt
Slægternes Strid.
"""
    expected = {"s": 20}
    # When
    result = count_alliteration(text)
    # Then
    assert result == expected


def test_count_alliteration_counts_only_words_with_alliteration():
    # Given
    text = "Her er noen ord som ikke gir alliterasjon"
    # When
    result = count_alliteration(text)
    # Then
    assert result == {}
