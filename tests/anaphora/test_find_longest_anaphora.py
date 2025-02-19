import pytest
from poetry_analysis.anaphora import find_longest_anaphora
from collections import Counter


def test_find_most_repeating_sequence():
    # Given 
    phrases = Counter({"hello": 3, "hello world": 2, "world": 1})
    expected_phrase = "hello"
    expected_count = 3

    # When
    actual_phrase, actual_count = find_longest_anaphora(phrases)

    # Then
    assert actual_phrase == expected_phrase
    assert actual_count == expected_count


def test_find_longest_repeating_sequence():
    # Given 
    phrases = Counter({"hello": 2, "hello world": 2, "world": 1})
    expected_phrase = "hello world"
    expected_count = 2

    # When
    actual_phrase, actual_count = find_longest_anaphora(phrases)

    # Then
    assert actual_phrase == expected_phrase
    assert actual_count == expected_count


def test_find_longest_most_repeating_sequence():
    # Given 
    phrases = Counter({"hello": 3, "hello world": 3, "world": 1})
    expected_phrase = "hello world"
    expected_count = 3

    # When
    actual_phrase, actual_count = find_longest_anaphora(phrases)

    # Then
    assert actual_phrase == expected_phrase
    assert actual_count == expected_count


def test_ignores_longer_sequence_with_lower_count():
    # Given 
    phrases = Counter({"hello": 3, "hello world": 3, "hello world hello world": 1})
    expected_phrase = "hello world"
    expected_count = 3

    # When
    actual_phrase, actual_count = find_longest_anaphora(phrases)

    # Then
    assert actual_phrase == expected_phrase
    assert actual_count == expected_count


def test_find_longest_repeating_sequence_returns_None_with_empty_counter():
    # Given 
    phrases = Counter()

    # When
    actual_phrase, actual_count = find_longest_anaphora(phrases)
    # Then
    assert actual_phrase is None
    assert actual_count == 0

