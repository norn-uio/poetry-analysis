import pytest
from poetry_analysis import rhyme_detection as rd


def test_tag_rhyming_verses_returns_rhyme_tag():
    # Given 
    verses = [
            ['EE2 N S OAH0 M'], 
            ['G R UU1'],
            ['D EE1 N', 'S OAH0 M'], 
            ['G R UU1'],
        ]

    output = rd.tag_rhyming_verses(verses)
    assert output[0].get("rhyme_tag") == "a"
    assert output[1].get("rhyme_tag") == "b"
    assert output[2].get("rhyme_tag") == "a"
    assert output[3].get("rhyme_tag") == "b"

@pytest.mark.skip("Not handled correctly yet")
@pytest.mark.parametrize("rhymepair", [[['G R UU1'], ['G R UU1']], [['S OAH0 M'], ['S OAH0 M']]])
def test_identical_phrases_result_in_noedrim(rhymepair):
    # Given
    output = rd.tag_rhyming_verses(rhymepair)
    assert output[0].get("rhyme_tag") == output[1].get("rhyme_tag")    
    assert output[1].get("rhyme_score") == 0.5


def test_tag_rhyming_verses_scores_proper_rhymes_with_1():
    # Given
    text = [
        ['L OH2 K AX0 S'],
        ['S K R UH2 MP AX0 R', 'IH3 N'],
        ['SJ L OH2 K AX0 S'],
        ['OEH1 R K AX0 N V IH3 N']
    ]
    result = rd.tag_rhyming_verses(text)
    assert result[2]["rhyme_score"] == 1
    assert result[3]["rhyme_score"] == 1



def test_tag_rhyming_verses_orthographic_verses_return_rhyme_tag():
    # Given
    verses = [
        ['Ensom', 'ensom'],
        ['Det', 'ord', 'er', 'fuldt', 'af', 'gru'],
        ['Ve', 've', 'den', 'som'],
        ['ei', 'frygter', 'ordets', 'gru']
    ]
    result = rd.tag_rhyming_verses(verses, orthographic=True)
    assert result[0]["rhyme_tag"] == result[2]["rhyme_tag"]
    assert result[1]["rhyme_tag"] == result[3]["rhyme_tag"]



@pytest.fixture
def orthographic_verses():
    #%%
    poem = { "text_id": "1526_Ensom_no-nb_digibok_2009040303003",
    "line_0": [["Ensom", "EE2 N S OAH3 M"], ["ensom", "EE2 N S OAH0 M"]],
    "line_1": [["Det", "D AX0"], ["ord", "OO1 R"], ["er", "AX0 R"], ["fuldt", "F UH2 L T"], ["af", "AH0 F"], ["gru", "G R UU1"]],
    "line_2": [["Ve", "V EE1"], ["ve", "V AX0"], ["den", "D AX0 N"], ["som", "S OAH0 M"]],
    "line_3": [["ei", "AEJ1"], ["frygter", "F R YY1 G T AX0 R"], ["ordets", "OO2 R AX0 T S"], ["gru", "G R UU1"]],
    "line_4": [],
    "line_5": [],
    "line_6": [["Livets", "L II1 V AX0 T S"], ["mening", "M EE2 N IH0 NG"]],
    "line_7": [["ei", "AEJ1"], ["findes", "F IH2 N D AX0 S"], ["i", "IH0"], ["det", "D AX0"], ["ord", "OO1 R"]],
    "line_8": [["I", "II1"], ["forening", "F OAH0 R EE1 N IH0 NG"]],
    "line_9": [["der", "D AX0 R"], ["leves", "L EE2 V AX0 S"], ["skal", "S K AH1 L"], ["paa", "P OA3"], ["jord", "J OO1 R"]],
    "line_10": [],
    "line_11": [],
    "line_12": [["Ensom", "EE2 N S OAH3 M"], ["ensom", "EE2 N S OAH0 M"]],
    "line_13": [["det", "D AX0"], ["ord", "OO1 R"], ["er", "AX0 R"], ["fuldt", "F UH2 L T"], ["af", "AH0 F"], ["gru", "G R UU1"]],
    "line_14": [["Ve", "V EE1"], ["ve", "V AX0"], ["den", "D AX0 N"], ["som", "S OAH0 M"]],
    "line_15": [["ei", "AEJ1"], ["flyr", "F L YY1 R"], ["for", "F OO1 R"], ["ordets", "OO2 R AX0 T S"], ["gru", "G R UU1"]],
    "line_16": [],
    "line_17": [],
    "line_18": [["Blodet", "B L OAH1 D AX0"], ["banker", "B AH2 NG K AX0 R"]],
    "line_19": [["vel", "V EH1 L"], ["end", "EH1 N"], ["i", "IH0"], ["aarens", "AA1 RNX0 S"], ["v\u00e6v", "V EE1 V"]],
    "line_20": [["D\u00f8de", "D OE2 D AX0"], ["tanker", "T AH2 NG K AX0 R"]],
    "line_21": [["blir", "B L II1 R"], ["frugten", "F R UH0 G T NX0"], ["af", "AH0 F"], ["dets", "D AX0 T S"], ["str\u00e6v", "S T R AE1 V"]],
    "line_22": [],
    "line_23": [],
    "line_24": [["Hjertet", "J AEH2 RT AX0 T"], ["lukkes", "L OH2 K AX0 S"]],
    "line_25": [["og", "OA1"], ["sj\u00e6len", "SJ EH1 L NX0"], ["skrumper", "S K R UH2 M P AX0 R"], ["ind", "IH0 N D"]],
    "line_26": [["Livet", "L II3 V AX0"], ["slukkes", "SJ L OH2 K AX0 S"]],
    "line_27": [["af", "AH0 F"], ["selvets", "S EH2 L V AX0 T S"], ["\u00f8rkenvind", "OEH1 R K AX0 N V IH3 N"]]
} 
    
# %%
