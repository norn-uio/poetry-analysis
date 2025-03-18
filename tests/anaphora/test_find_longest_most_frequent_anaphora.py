from collections import Counter

from poetry_analysis.anaphora import find_longest_most_frequent_anaphora


def test_find_most_repeating_sequence():
    # Given
    phrases = Counter({"hello": 3, "hello world": 2, "world": 1})
    expected_phrase = "hello"
    expected_count = 3

    # When
    actual_phrase, actual_count = find_longest_most_frequent_anaphora(phrases)

    # Then
    assert actual_phrase == expected_phrase
    assert actual_count == expected_count


def test_find_longest_repeating_sequence():
    # Given
    phrases = Counter({"hello": 2, "hello world": 2, "world": 1})
    expected_phrase = "hello world"
    expected_count = 2

    # When
    actual_phrase, actual_count = find_longest_most_frequent_anaphora(phrases)

    # Then
    assert actual_phrase == expected_phrase
    assert actual_count == expected_count


def test_find_longest_most_repeating_sequence():
    # Given
    phrases = Counter({"hello": 3, "hello world": 3, "world": 1})
    expected_phrase = "hello world"
    expected_count = 3

    # When
    actual_phrase, actual_count = find_longest_most_frequent_anaphora(phrases)

    # Then
    assert actual_phrase == expected_phrase
    assert actual_count == expected_count


def test_ignores_longer_sequence_with_lower_count():
    # Given
    phrases = Counter({"hello": 3, "hello world": 3, "hello world hello world": 1})
    expected_phrase = "hello world"
    expected_count = 3

    # When
    actual_phrase, actual_count = find_longest_most_frequent_anaphora(phrases)

    # Then
    assert actual_phrase == expected_phrase
    assert actual_count == expected_count


def test_find_longest_repeating_sequence_returns_None_with_empty_counter():
    # Given
    phrases = Counter()

    # When
    actual_phrase, actual_count = find_longest_most_frequent_anaphora(phrases)
    # Then
    assert actual_phrase is None
    assert actual_count == 0


def test_find_longest_most_frequent_anaphora_returns_most_frequent_count_instead_of_longest():
    # Given
    phrases = Counter({"hello": 5, "hello world": 3, "world": 2})
    expected_phrase = "hello"
    expected_count = 5

    # When
    actual_phrase, actual_count = find_longest_most_frequent_anaphora(phrases)

    # Then
    assert actual_phrase == expected_phrase
    assert actual_count == expected_count
