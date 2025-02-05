"""Anaphora is the repetition of the same word or phrase
at the beginning of successive clauses or sentences.
"""
from collections import defaultdict
from pathlib import Path

from poetry_analysis.utils import strip_punctuation, annotate


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
