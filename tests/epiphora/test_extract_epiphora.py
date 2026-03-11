from poetry_analysis.epiphora import extract_epiphora


def test_extract_epiphora_detects_repeated_words():
    # given
    input_texts = ["Så gjør vi så når vi vasker vårt tøy", "vasker vårt tøy", "vasker vårt tøy"]
    # when
    result = extract_epiphora(input_texts)

    assert result[1]["overlap"] == result[2]["overlap"] == "vasker vårt tøy"


def test_extract_epiphora_ignores_identical_punctuation():
    input_texts = ["Hello world!", "This is a different line!", "Another line with the same punctuation!"]

    result = extract_epiphora(input_texts)

    # The result should be an empty dict
    assert result == {}


def test_extract_epiphora_ignores_case():
    input_texts = ["This line ends in a word", "Here is a line with a WORD", "This one ends in a WoRd."]
    # when
    result = extract_epiphora(input_texts)

    assert result[1]["overlap"] == result[2]["overlap"] == "a word"


def test_extract_epiphora_empty_input_returns_empty_dict():
    # given
    input_texts = []

    # when
    result = extract_epiphora(input_texts)

    # then
    assert result == {}


def test_extract_epiphora_single_line_returns_empty_dict():
    # given
    input_texts = ["Only one line here."]

    # when
    result = extract_epiphora(input_texts)

    # then
    assert result == {}


def test_extract_epiphora_no_overlapping_endings_returns_empty_dict():
    # given
    input_texts = [
        "This line ends with apple",
        "Another one ends with banana",
        "Here is a third line ending with cherry",
    ]

    # when
    result = extract_epiphora(input_texts)

    # then
    assert result == {}


def test_extract_epiphora_ignores_whitespace_only_overlap():
    # given: lines share only trailing whitespace as a common ending
    input_texts = [
        "First line with spaces   ",
        "Second different content   ",
        "Third line also padded   ",
    ]

    # when
    result = extract_epiphora(input_texts)

    # then: whitespace-only overlap should not be treated as epiphora
    assert result == {}


def test_extract_epiphora_full_stanza_final_lines():
    input_texts = [
        """Så gjør vi så når vi vasker vårt tøy,
        vasker vårt tøy,
        vasker vårt tøy,
        tidlig en mandags morgen""",
        """Så gjør vi så når vi skyller vårt tøy,
        skyller vårt tøy,
        skyller vårt tøy,
        tidlig en tirsdags morgen""",
        """Så gjør vi så når vi henger opp vårt tøy,
        henger opp vårt tøy,
        henger opp vårt tøy,
        tidlig en onsdags morgen""",
    ]
    result = extract_epiphora(input_texts)
    assert "dags morgen" in result[1]["overlap"]
    assert "dags morgen" in result[2]["overlap"]


def test_extract_epiphora_full_text_only_catches_successive_overlaps():
    input_texts = [
        "Så gjør vi så når vi vasker vårt tøy,",
        "vasker vårt tøy, ",
        "vasker vårt tøy,",
        "tidlig en mandags morgen",
        "Så gjør vi så når vi skyller vårt tøy",
        "skyller vårt tøy",
        "skyller vårt tøy",
        "tidlig en tirsdags morgen",
        "Så gjør vi så når vi henger opp vårt tøy",
        "henger opp vårt tøy",
        "henger opp vårt tøy",
        "tidlig en onsdags morgen",
    ]
    result = extract_epiphora(input_texts)
    overlaps = [item["overlap"] for k, item in result.items()]
    assert overlaps, "Expected at least one epiphora overlap to be detected"
    assert result[1]["overlap"] == result[2]["overlap"] == "vasker vårt tøy"
    assert result[5]["overlap"] == result[6]["overlap"] == "skyller vårt tøy"
    assert result[9]["overlap"] == result[10]["overlap"] == "henger opp vårt tøy"
