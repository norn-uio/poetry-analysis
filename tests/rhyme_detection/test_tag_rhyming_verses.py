import pytest

from poetry_analysis import rhyme_detection as rd


def test_transcriptions_return_correct_rhyme_tags(transcribed_poem_lines):
    # Given
    result = rd.tag_rhyming_verses(transcribed_poem_lines, orthographic=False)
    assert result[0].rhyme_tag == result[1].rhyme_tag
    assert result[2].rhyme_tag == result[3].rhyme_tag


def test_orthographic_verses_return_correct_rhyme_tag():
    # Given

    verses = [
        "Der var Ufred i Landet Paa Torvet stod",
        "En vandrende Svend med sin Kjøbmandsbod",
        "Af skinnende Smykker laa Disken fuld",
        "Der var Bælter af Silke og Ringer af Guld",
    ]
    result = rd.tag_rhyming_verses(verses, orthographic=True)
    assert result[0].rhyme_tag == result[1].rhyme_tag
    assert result[2].rhyme_tag == result[3].rhyme_tag


def test_tag_rhyming_verses_scores_proper_rhymes_more_than_0():
    # Given
    verses = [
        ["L OH2 K AX0 S"],
        ["S K R UH2 M P AX0 R", "IH3 N"],
        ["SJ L OH2 K AX0 S"],
        ["OEH1 R K AX0 N V IH3 N"],
    ]
    result = rd.tag_rhyming_verses(verses, orthographic=False)
    assert result[2].rhyme_score > 0
    assert result[3].rhyme_score > 0
