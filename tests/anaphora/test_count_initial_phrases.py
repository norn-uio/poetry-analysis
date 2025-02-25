from collections import Counter
from poetry_analysis.anaphora import count_initial_phrases


def test_count_initial_phrases_returns_increasing_phrases_with_single_counts(): 
    text = "ett ord blir flere til en hel linje"
    expected = Counter({
        "ett": 1,
        "ett ord": 1,
        "ett ord blir": 1,
        "ett ord blir flere": 1,
        "ett ord blir flere til": 1,
        "ett ord blir flere til en": 1,
        "ett ord blir flere til en hel": 1,
        "ett ord blir flere til en hel linje": 1,
    })
    result = count_initial_phrases(text)
    assert all(count == 1 for count in result.values())
    assert all(actual_phrase == expected_phrase for actual_phrase, expected_phrase in zip(result.keys(), expected.keys()))


def test_repeated_phrases_are_counted():
    text = "ett ord i en frase, ett ord i en linje, ett ord i en setning"
    result = count_initial_phrases(text)

    assert result["ett"] == 3
    assert result["ett ord"] == 3
    assert result["ett ord i"] == 3
    assert result["ett ord i en"] == 3
    assert result["ett ord i en frase"] == 1
    assert result.most_common(1) == [("ett", 3)]
