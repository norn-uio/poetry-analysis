"""Anaphora is the repetition of the same line-initial word or phrase
in a verse, or across consecutive verses in a stanza. 

It can also refer to the repetition of a whole stanza-initial verse line 
in consecutive stanzas.
"""
from collections import defaultdict, Counter
from pathlib import Path

from poetry_analysis.utils import strip_punctuation, annotate, split_stanzas


def count_initial_phrases(text: str) -> Counter:
    """Count the number of times initial phrases of different lengths occur in a string."""
    phrase_counts = Counter()
    words = strip_punctuation(text).split()
    n_words = len(words)
   
    for n in range(1, n_words + 1):
        if len(words) >= n:
            phrase = " ".join(words[:n])
            count = text.count(phrase)
            if count > 0:
                phrase_counts[phrase] += count
    return phrase_counts


def find_longest_anaphora_in_line(phrases: Counter) -> dict:
    """Find the longest and most repeated word sequence in a line."""
    if not phrases:
        return None, 0

    most_common_phrase, highest_count = phrases.most_common()[0]
    top_phrases = [phrase for phrase, _ in phrases.most_common() if phrases[phrase] == highest_count]

    longest_phrase = max(top_phrases, key=len)
    longest_count = phrases[longest_phrase]

    if highest_count == longest_count:
        annotation = (longest_phrase, longest_count)
    else:
        annotation = (most_common_phrase, highest_count)
    return annotation


def extract_line_anaphora(text: str) -> list:
    """Extract word sequences that are repeated at least twice on the same line."""
    anaphora = [] 
    lines = text.strip().lower().split("\n")
    for i, line in enumerate(lines):
        line_initial_phrases = count_initial_phrases(line)
        phrase, count = find_longest_anaphora_in_line(line_initial_phrases)
        if count > 1:
            annotation = {"line_id": i, "phrase": phrase, "count": count}
            anaphora.append(annotation)
    return anaphora


def extract_stanza_anaphora(text: str) -> list:
    """Extract line-initial word sequences that are repeated at least twice in each stanza."""
    anaphora = []
    
    stanzas = split_stanzas(text)
    for i, stanza in enumerate(stanzas):
        stanza_anaphora = find_anaphora_in_stanza(stanza)
    
        for phrase, count in stanza_anaphora.items():
            line_ids = [l for l, line in enumerate(stanza) if line.startswith(phrase)]
            anaphora.append({
                "stanza_id": i, 
                "line_id": line_ids,
                "phrase": phrase,
                "count": count
            })

    return anaphora


def find_anaphora_in_stanza(lines: list) -> list:
    """Extract line-initial word sequences that are repeated at least twice in the same stanza."""
    phrase_counts = Counter()

    for line in lines:
        line_initial_phrases = count_initial_phrases(line)
        phrase_counts.update(line_initial_phrases)

    return phrase_counts


def extract_anaphora(text: str) -> dict:
    """Extract line-initial word sequences that are repeated at least twice.

    Example use:
    >>> import json
    >>> text = '''
    ... Jeg ser paa den hvide himmel,
    ... jeg ser paa de graablaa skyer,
    ... jeg ser paa den blodige sol.
    ...
    ... Dette er altsaa verden.
    ... Dette er altsaa klodernes hjem.
    ...
    ... En regndraabe!
    ... '''
    >>> result = extract_anaphora(text)
    >>> print(json.dumps(result, indent=4))
    {
        "1-grams": {
            "jeg": 3,
            "dette": 2
        },
        "2-grams": {
            "jeg ser": 3,
            "dette er": 2
        },
        "3-grams": {
            "jeg ser paa": 3,
            "dette er altsaa": 2
        },
        "4-grams": {
            "jeg ser paa den": 2
        }
    }
    """
    lines = text.strip().lower().split("\n")
    ngram_counts = defaultdict(lambda: defaultdict(int))

    for line in lines:
        text = strip_punctuation(line)
        words = text.split()
        n_words = len(words)
        for n in range(1, n_words + 1):
            if len(words) >= n:
                ngram = " ".join(words[:n])
                ngram_counts[n][ngram] += 1

    anaphora = {}
    for n in range(1, 5):
        ngram_type = f"{n}-grams"
        ngrams = {ngram: count for ngram, count in ngram_counts[n].items() if count > 1}
        if ngrams:
            anaphora[ngram_type] = ngrams
    return anaphora


if __name__ == "__main__":
    import doctest
    doctest.testmod()

        # Parse user arguments
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("textfile", help="Filepath to the text to analyze.")
    parser.add_argument(
        "--split_stanzas", action="store_true", help="Split the text into stanzas."
    )
    args = parser.parse_args()

    # Analyze the text
    filepath = Path(args.textfile)
    text = filepath.read_text()

    output_file = Path(filepath.parent / f"{filepath.stem}_anaphora.json")    
    annotate(extract_anaphora, text, stanzaic=args.split_stanzas, outputfile=output_file)    
    print(f"Anaphora saved to file: {output_file}")
