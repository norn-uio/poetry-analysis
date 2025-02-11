import pytest
from poetry_analysis.alliteration import extract_alliteration


def test_alliteration_returns_initial_consonant_counts():
    # Given
    text = [line.strip() for line in """Stjerneklare Septembernat
    Skaldene som siger sandhetden smukkest
    Ser Samla saga skriver.
    Litt flere ord
    """.splitlines()]

    expected = [
        {"line": 0, "symbol": "s", "count": 2, "words": ["Stjerneklare", "Septembernat"]},
        {"line": 1, "symbol": "s", "count": 5, "words": ["Skaldene", "som", "siger", "sandhetden", "smukkest"]},
        {"line": 2, "symbol": "s", "count": 4, "words": ["Ser", "Samla", "saga", "skriver."]},
        ]
    
    # When
    result = extract_alliteration(text)
    assert pytest.approx(expected) == result
  
