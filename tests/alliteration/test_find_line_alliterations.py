from poetry_analysis.alliteration import find_line_alliterations


def test_find_line_alliterations_vowels_only(poem_with_vowel_alliteration):
    result = find_line_alliterations(poem_with_vowel_alliteration, letter_type="vowel")

    assert not any(word.startswith("h") for line in result for word in line)
    assert all(word.startswith("a") for word in result[0])
    assert all(word.startswith("o") for word in result[1])
    assert all(word.startswith("i") for word in result[2])


def test_find_line_alliterations_consonants_only(poem_with_vowel_alliteration):
    result = find_line_alliterations(poem_with_vowel_alliteration, letter_type="consonant")

    assert all(word.startswith("h") for word in result[0])
    assert not any(word.startswith("a") for line in result for word in line)
    assert len(result) == 1


def test_find_all_letters(poem_with_vowel_alliteration):
    result = find_line_alliterations(poem_with_vowel_alliteration, letter_type="both")

    assert all(word.startswith("a") for word in result[0])
    assert all(word.startswith("h") for word in result[1])
    assert all(word.startswith("o") for word in result[2])
    assert all(word.startswith("i") for word in result[3])


def test_find_all_letters_with_invalid_letter_type(poem_with_vowel_alliteration):
    result_invalid = find_line_alliterations(poem_with_vowel_alliteration, letter_type="invalid_type")
    result_both = find_line_alliterations(poem_with_vowel_alliteration, letter_type="both")

    assert result_invalid == result_both


def test_find_line_alliterations_default_behavior(poem_with_vowel_alliteration):
    # When letter_type is not specified, the function should behave as if "both" were selected,
    # preserving backward-compatible behavior.
    result = find_line_alliterations(poem_with_vowel_alliteration)

    assert all(word.startswith("a") for word in result[0])
    assert all(word.startswith("h") for word in result[1])
    assert all(word.startswith("o") for word in result[2])
    assert all(word.startswith("i") for word in result[3])
