from poetry_analysis.lyrical_subject import detect_lyrical_subject


def test_detects_explicit_subject():
    poem_text = "Jeg er en poet"
    assert detect_lyrical_subject(poem_text)["explicit_subject"] is True


def test_detects_explicit_object():
    poem_text = "Du sa det til meg."
    assert detect_lyrical_subject(poem_text)["explicit_object"] is True


def test_detects_implicit():
    poem_text = "Vi leser bøker."
    assert detect_lyrical_subject(poem_text)["implicit"] is True


def test_detects_deixis():
    poem_text = "I går var en fin dag."
    assert detect_lyrical_subject(poem_text)["deixis"] is True

