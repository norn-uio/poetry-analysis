import pytest

from poetry_analysis.anaphora import extract_anaphora


@pytest.mark.parametrize(
    "text_sequence,expected_overlap",
    (
        (["jeg ser på den hvite himmel", "jeg ser på de gråblå skyer", "jeg ser på denne blodige sol."], "jeg ser på"),
        (
            ["dette er altså verden.", "dette er altså klodernes hjem.", "Dette er altså et kjent dikt."],
            "dette er altså",
        ),
        (["Her er vi i Norge.", "Her er vi på berget.", "Her er vi."], "her er vi"),
        (
            [
                "Så gjør vi så når vi vasker vårt tøy",
                "så gjør vi så når vi henger opp vårt tøy",
                "Så gjør vi så når vi skyller vårt tøy",
            ],
            "så gjør vi så når vi",
        ),
    ),
)
def test_extract_anaphora_detects_repeated_words(text_sequence, expected_overlap):
    result = extract_anaphora(text_sequence)

    assert expected_overlap in result[1]["overlap"]
    assert expected_overlap in result[2]["overlap"]


def test_extract_anaphora_ignores_identical_punctuation():
    input_texts = ["Hello world!", "This is a different line!", "Another line with the same punctuation!"]

    result = extract_anaphora(input_texts)

    # The result should be an empty dict
    assert result == {}


def test_extract_anaphora_ignores_case():
    input_texts = [
        "This line starts with a word",
        "ThIs LINE  has the same words in mixed case",
        "- This line begins with a dash.",
    ]
    # when
    result = extract_anaphora(input_texts)

    assert result[1]["overlap"] == result[2]["overlap"] == "this line"


def test_extract_anaphora_empty_input_returns_empty_dict():
    # given
    input_texts = []

    # when
    result = extract_anaphora(input_texts)

    # then
    assert result == {}


def test_extract_anaphora_single_line_returns_empty_dict():
    # given
    input_texts = ["Only one line here."]

    # when
    result = extract_anaphora(input_texts)

    # then
    assert result == {}


def test_extract_anaphora_no_overlapping_endings_returns_empty_dict():
    # given
    input_texts = [
        "This line ends with apple",
        "Another one ends with banana",
        "Here is a third line ending with cherry",
    ]

    # when
    result = extract_anaphora(input_texts)

    # then
    assert result == {}


def test_extract_anaphora_ignores_whitespace_only_overlap():
    # given: lines share only trailing whitespace as a common ending
    input_texts = [
        "   First line with spaces   ",
        "   Second different content   ",
        "   Third line also padded   ",
    ]

    # when
    result = extract_anaphora(input_texts)

    # then: whitespace-only overlap should not be treated as anaphora
    assert result == {}


def test_extract_anaphora_full_stanza_initial_lines():
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
    result = extract_anaphora(input_texts)
    assert result[1]["overlap"] == "så gjør vi så når vi"
    assert result[2]["overlap"] == "så gjør vi så når vi"
