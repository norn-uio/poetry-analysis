"""Anaphora is the repetition of the same word or phrase
at the beginning of successive clauses or sentences.
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
            if count > 1:
                phrase_counts[phrase] += count
    return phrase_counts


def extract_line_anaphora(text: str) -> list:
    """Extract word sequences that are repeated at least twice on the same line."""
    anaphora = [] 
    lines = text.strip().lower().split("\n")
    for i, line in enumerate(lines):
        
        line_initial_phrases = count_initial_phrases(line)
        if line_initial_phrases: 
            longest_phrase = max(line_initial_phrases, key=len)
            count = line_initial_phrases[longest_phrase]
            # TODO: refactor so when assertion fails, the most common phrase is saved rather than the longest
            assert count == line_initial_phrases.most_common(1)[0][1]

            annotation = {"line_id": i, "phrase": longest_phrase, "count": count}
            anaphora.append(annotation)
    return anaphora



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
