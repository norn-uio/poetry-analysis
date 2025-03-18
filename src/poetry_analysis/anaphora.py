"""Anaphora is the repetition of the same line-initial word or phrase
in a verse, or across consecutive verses in a stanza.

TODO: It can also refer to the repetition of a whole stanza-initial verse line
in consecutive stanzas.
> NOTE: This has not been implemented yet. 
This anaphora detection process is based on the repetition of the first word in each line. We will continue with implementing a grading system for how effective the figure is in each poem.
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


def find_longest_most_frequent_anaphora(phrases: Counter) -> dict:
    """Find the longest and most repeated word sequence in a line."""
    if not phrases:
        return None, 0

    _, highest_count = phrases.most_common()[0]
    top_phrases = [
        phrase
        for phrase, _ in phrases.most_common()
        if phrases[phrase] == highest_count
    ]

    longest_phrase = max(top_phrases, key=len)
    longest_count = phrases[longest_phrase]

    annotation = (longest_phrase, longest_count)
    return annotation


def extract_line_anaphora(text: str) -> list:
    """Extract line initial word sequences that are repeated at least twice on the same line."""
    anaphora = []
    lines = text.strip().lower().split("\n")
    for i, line in enumerate(lines):
        line_initial_phrases = count_initial_phrases(line)
        phrase, count = find_longest_most_frequent_anaphora(line_initial_phrases)
        if count > 1:
            annotation = {"line_id": i, "phrase": phrase, "count": count}
            anaphora.append(annotation)
    return anaphora


def is_successive(items:list): 
    return [items[i] == items[i-1] + 1 for i, item in enumerate(items)][1:]


def extract_poem_anaphora(text: str) -> list:
    """Extract line-initial word sequences that are repeated at least twice in each stanza."""
    anaphora = []

    stanzas = split_stanzas(text)
    for i, stanza in enumerate(stanzas):
        stanza_anaphora = extract_stanza_anaphora(stanza)
        for phrase, indeces in stanza_anaphora.items():
            if len(indeces) <= 1:
                continue
            if all(is_successive(indeces)):
                annotation = {"stanza_id": i, "line_id": indeces, "phrase": phrase, "count": len(indeces)}
                anaphora.append(annotation)
    return anaphora


def extract_stanza_anaphora(stanza: list[str]) -> dict:
    stanza_anaphora = {}

    for line_index, line in enumerate(stanza):
        if not line: 
            continue
        first_word = line.split()[0].lower()
        previous_line = stanza[line_index -1].lower().split()
        try:
            previous_first_word = previous_line[0]
        except IndexError:
            previous_first_word = None
        
        if (line_index > 0 and previous_first_word == first_word): 
            stanza_anaphora[first_word].append(line_index)
        else:
            stanza_anaphora[first_word] = [line_index]
    
    return stanza_anaphora


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
    annotate(
        extract_anaphora, text, stanzaic=args.split_stanzas, outputfile=output_file
    )
    print(f"Anaphora saved to file: {output_file}")
