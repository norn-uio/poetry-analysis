import pytest

from poetry_analysis import rhyme_detection as rd
from poetry_analysis import utils


@pytest.mark.skip("Skipping test for now")
def test_rhyme_scheme_gets_tagged_for_multiple_stanzas(example_poem_landsmaal):
    stanzas = utils.split_stanzas(example_poem_landsmaal)

    tagged_stanzas = list(rd.tag_stanzas(stanzas))

    assert len(tagged_stanzas) == 3

    for stanza in tagged_stanzas:
        assert stanza[0].get("rhyme_scheme") == "abcb"
