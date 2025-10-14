import pytest

from poetry_analysis.utils import split_stanzas


@pytest.mark.parametrize(
    "example_fixture, n_stanzas, n_lines",
    [
        ("example_poem_danish", 3, 8),
        ("example_poem_riksmaal", 4, 4),
        ("example_poem_landsmaal", 3, 4),
    ],
)
def test_multi_stanza_poem_is_split_into_correct_number_of_stanzas(example_fixture, n_stanzas, n_lines, request):
    # given example poems
    example = request.getfixturevalue(example_fixture)
    # when
    result = split_stanzas(example)
    # then
    assert len(result) == n_stanzas  # Number of stanzas in the poem
    assert all(len(stanza) == n_lines for stanza in result)  # Number of lines in each stanza
