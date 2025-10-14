import pytest

from poetry_analysis import rhyme_detection as rd


@pytest.fixture
def previous_transcribed_lines(transcribed_poem_lines):
    """Create a list of Verse objects from the transcribed lines"""
    last_tokens = ["S T OO1 D", "B OO3 D", "F UH2 L", "G UH2 L"]
    verselines = [
        rd.Verse(idx, tokens=words, last_token=last)
        for idx, (words, last) in enumerate(zip(transcribed_poem_lines, last_tokens, strict=False))
    ]
    return verselines


@pytest.fixture
def previous_orthographic_lines(orthographic_poem_lines):
    verselines = [
        rd.Verse(idx, tokens=words, last_token=words[-1]) for idx, words in enumerate(orthographic_poem_lines)
    ]
    return verselines


def test_find_rhyming_transcribed_line_returns_None_and_zero_if_not_found(
    previous_transcribed_lines,
):
    # Given
    current_line = rd.Verse("X", last_token="X", tokens=["X"])

    # When
    verse, score = rd.find_rhyming_line(current_line, previous_transcribed_lines)

    # Then
    assert verse is None
    assert score == 0


def test_find_rhyming_transcribed_line_returns_correct_rhyming_line(
    previous_transcribed_lines,
):
    # Given
    current_line = rd.Verse("X", last_token="J UH2 L")

    # When
    verse, score = rd.find_rhyming_line(current_line, previous_transcribed_lines)

    # Then
    # It will return the first rhyming match it finds, i.e. the last line
    assert verse == 3
    assert score == 1
    assert previous_transcribed_lines[verse].last_token == "G UH2 L"


def test_finds_rhyming_orthographic_line(
    previous_orthographic_lines,
):
    # Given
    current_line = rd.Verse("X", last_token="tuld")
    expected_last_token = "Guld"

    # When
    verse, score = rd.find_rhyming_line(current_line, previous_orthographic_lines, orthographic=True)

    # Then
    # It will return the first rhyming match it finds, i.e. the last line
    assert verse == 3
    assert score == 1
    assert previous_orthographic_lines[verse].last_token == expected_last_token
