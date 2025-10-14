import re

WORDBAGS = {
    "explicit_subject": [
        "jeg",
        "eg",
    ],
    "explicit_object": [
        "mig",
        "meg",
        "mine",
        "min",
        "mitt",
        "mit",
        "mi",
    ],
    "implicit": [
        "vi",
        "oss",
        "våre",
        "vår",
        "du",
        "deg",
        "dig",
        "din",
        "dine",
        "ditt",
        "dere",
        "deres",
    ],
    "deixis": [
        "her",
        "hit",
        "nå",
        "nu",
        "herfra",
        "i morgen",
        "i går",
        "i kveld",
        "i fjor",
    ],
}

category_names = {
    "explicit_subject": "Explicit subject",
    "explicit_object": "Explicit object",
    "implicit": "Implicit",
    "deixis": "Deixis",
}


def detect_lyrical_subject(poem_text: str) -> dict:
    """Map the presence of certain words denoting a lyrical subject in a poem to categorical labels."""
    lyrical_subject = {}
    for label, words in WORDBAGS.items():
        regx_pattern = "|".join(words)
        matches = re.findall(regx_pattern, poem_text.lower())
        is_present = bool(any(matches))
        lyrical_subject[label] = is_present
    return lyrical_subject


def process_poems(poems, text_field="textV3"):
    """Annotate whether or not the lyrical subject is a feature in a list of poems."""

    for poem in poems:
        poem_text = poem.get(text_field)
        lyric_features = detect_lyrical_subject(poem_text)
        yield add_metadata(poem, lyric_features)


def add_metadata(poem, lyric_features):
    """Add metadata from the poem to the annotations."""
    lyric_features["ID"] = int(poem.get("ID"))
    lyric_features["URN"] = poem.get("URN")
    lyric_features["Tittel på dikt"] = poem.get("Tittel på dikt")
    return lyric_features


if __name__ == "__main__":
    import doctest

    doctest.testmod()
