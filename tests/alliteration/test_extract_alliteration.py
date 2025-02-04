from poetry_analysis import alliteration


def test_alliteration_returns_initial_consonant_words():
    """Test that the function returns words that start with the same letter."""
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
    expected = {
        "stanza_1": {
            "s": [
                "Sees",
                "Septembernat",
                "Sirius,",
                "Skue",
                "Slægternes",
                "Solens",
                "Stjerne,",
                "Stjerneklare",
                "Straale",
                "Strid.",
                "Svæve",
                "Sydhimlens",
                "Søster,",
                "saa",
                "skjønneste",
                "smukkeste",
                "smukt,",
                "stille,",
                "sørgmodigt",
            ]
        }
    }
    # When
    result = alliteration.extract_alliteration(text)
    # Then
    assert result == expected
