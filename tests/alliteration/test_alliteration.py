import pytest

from poetry_analysis.alliteration import extract_alliteration


def test_alliteration_returns_initial_consonant_counts():
    # Given
    text = [
        line.strip()
        for line in """Stjerneklare Septembernat
    Skaldene som siger sandhetden smukkest
    Ser Samla saga skriver.
    Litt flere ord
    """.splitlines()
    ]

    expected = [
        {
            "line": 0,
            "symbol": "s",
            "count": 2,
            "words": ["Stjerneklare", "Septembernat"],
        },
        {
            "line": 1,
            "symbol": "s",
            "count": 5,
            "words": ["Skaldene", "som", "siger", "sandhetden", "smukkest"],
        },
        {
            "line": 2,
            "symbol": "s",
            "count": 4,
            "words": ["Ser", "Samla", "saga", "skriver."],
        },
    ]

    # When
    result = extract_alliteration(text)
    assert pytest.approx(expected) == result


def test_extract_alliteration_skips_punctuation():
    text = (
        "her har hun høstet hvaler\n"
        "eller er en eller annen linje\n"
        "... her.. var ... ellipse...\n"
        "- her - er - bindestrek-\n"
        "? hva med? spørsmålstegn ?\n"
    ).splitlines()

    result = extract_alliteration(text)
    assert len(result) == 2
    assert result[0]["symbol"] == "h"
    assert result[1]["symbol"] == "e"
    assert not any(line["symbol"] in ["...", "-", "?"] for line in result)
