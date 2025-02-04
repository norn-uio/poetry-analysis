import pytest
from poetry_analysis import rhyme_detection as rt


@pytest.mark.parametrize(
    "phoneme",
    [
        "AE1", 
        "EE3",
        "EH1",
        "IH2",
        "RNX0",
        "AX0",
        "UU1",
    ],
)
def test_vowels_and_syllabic_consonants_are_nuclei(phoneme):
    """Check that phonemes that can be syllable nuclei 
    (vowels and syllabic consonants) are correctly identified.
    """
    result = rt.is_nucleus(phoneme)
    assert result


@pytest.mark.parametrize(
    "phoneme",
    [
        "KJ", 
        "M",
        "P",
        "RN",
        "L",
        "S",
        "X",
    ],
)
def test_consonants_are_not_nuclei(phoneme):
    
    result = rt.is_nucleus(phoneme)
    # then
    assert not result



