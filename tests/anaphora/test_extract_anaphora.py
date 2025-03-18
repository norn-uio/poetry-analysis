import pytest

from poetry_analysis.anaphora import extract_anaphora


@pytest.mark.skip("Deprecated")
@pytest.mark.parametrize(
    "text",
    (
        "jeg ser på den hvite himmel,\njeg ser på de gråblå skyer,\njeg ser på denne blodige sol.",
        "dette er altså verden.\ndette er altså klodernes hjem.\nDette er altså et kjent dikt.",
        "Her er vi i Norge.\nHer er vi på berget.\nHer er vi.\n",
    ),
)
def test_extract_anaphora_returns_3gram_frequencies_of_3_repeating_word_seqs(text):
    result = extract_anaphora(text)
    print(result)
    assert result.keys() == pytest.approx(["1-grams", "2-grams", "3-grams"])
    assert len(result.values()) == 3
    assert result["3-grams"].values() == pytest.approx([3])


@pytest.mark.skip("Deprecated")
def test_extract_anaphora_returns_nothing_if_no_words_repeat():
    text = "Her er noen ord som ikke gir anafora\nFor det er ikke noe som gjentar seg\ni denne teksten."
    result = extract_anaphora(text)
    assert result == {}
