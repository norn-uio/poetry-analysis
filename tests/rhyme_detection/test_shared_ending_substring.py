from poetry_analysis import rhyme_detection as rd


def test_shared_ending_substring():
    string1 = "skamfuld"
    string2 = "skamguld"

    result = rd.shared_ending_substring(string1, string2)
    
    assert result == "uld"

def test_shared_ending_substring_no_match():
    string1 = "skamfullt"
    string2 = "skammen"

    result = rd.shared_ending_substring(string1, string2)
    
    assert result == ""


def test_shared_ending_substring_transcription():
    string1 = "S T OO D"
    string2 = "B OO D"

    result = rd.shared_ending_substring(string1, string2).strip()
    
    assert result == "OO D"

