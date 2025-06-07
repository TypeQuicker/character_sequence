# English Character Sequence Analysis

This project analyzes character sequences in English text using the Project Gutenberg dataset from HuggingFace. It identifies and counts various patterns including n-grams, transitions, and words.

## What are we analyzing

- Character sequences and its occurances of the following n-grams: bigrams, trigrams, and quadgrams
- N-gram transitions occurances
- Word occurances analysis

We will processes large text datasets and output the results in CSV format

## Usage

1. Run the scripts and view their respecitive output csv files inside data/

## Output Format

The analysis generates several CSV files:

### N-grams

ngram_analyzer.py is the main script to analyze n-grams.
- `data/ngrams/bigrams.csv`: Two-character sequences
- `data/ngrams/trigrams.csv`: Three-character sequences
- `data/ngramsquadgrams.csv`: Four-character sequences

### Transitions

transitions_analyser is the main script to analyze "n" character sequence transitions between consecutive words.
- `data/transitions/bigram_transitions.csv`: Two-character transition patterns
- `data/transitions/trigram_transitions.csv`: Three-character transition patterns
- `data/transitions/quadgram_transitions.csv`: Four-character transition patterns

### Words

word_analyser is the main script to analyze word counts.
- `data/words/words.csv`: Individual word occurances.

## License

MIT License