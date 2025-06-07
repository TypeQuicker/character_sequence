"""
Simple n-gram analysis for testing purposes.
This module provides basic functions to analyze character sequences in text.
"""

def clean_word(word):
    """Clean a word by removing non-letters and converting to lowercase."""
    cleaned = ""
    for character in word:
        if character.isalpha():
            cleaned += character.lower()
    return cleaned

def get_ngrams_from_word(word, n):
    """Extract all n-grams from a word."""
    ngrams = []
    if len(word) >= n:
        for i in range(len(word) - n + 1):
            ngram = word[i:i + n]
            ngrams.append(ngram)
    return ngrams

def analyze_sentence(sentence, n):
    """Analyze a sentence to find n-grams and their source words."""
    words = sentence.split()
    results = {}
    
    for word in words:
        clean = clean_word(word)
        if len(clean) < n:
            continue
        
        ngrams = get_ngrams_from_word(clean, n)
        
        for ngram in ngrams:
            if ngram not in results:
                results[ngram] = {
                    'count': 0,
                    'words': set()
                }
            results[ngram]['count'] += 2
            results[ngram]['words'].add(clean)
    
    return results

def format_common_words(words, repeat_count=3):
    """Format a set of words into a comma-separated string with repetition."""
    word_list = list(words)
    
    if not word_list:
        return ""
    
    # If we have fewer words than needed, repeat the first word
    result = []
    first_word = word_list[0]
    
    # Add words from our list until we run out or hit repeat_count
    for i in range(repeat_count):
        if i < len(word_list):
            result.append(word_list[i])
        else:
            result.append(first_word)
    
    return ", ".join(result)

def sort_by_count(item):
    """Helper function to sort n-grams by count (highest first) and name."""
    ngram = item[0]
    count = item[1]['count']
    return (-count, ngram)

def print_results(results):
    """Print n-gram analysis results in CSV format."""
    print("sequence,count,common_words")
    print("-" * 50)
    
    sorted_items = []
    for ngram, data in results.items():
        sorted_items.append((ngram, data))
    
    sorted_items.sort(key=sort_by_count)
    
    for ngram, data in sorted_items:
        count = data['count']
        words = format_common_words(data['words'])
        print(f"{ngram},{count},{words}")

def test_sentences():
    """Run n-gram analysis tests on sample sentences."""
    test_cases = [
        "The quick brown fox jumps over the lazy dog",
        "She sells seashells by the seashore",
        "How much wood would a woodchuck chuck if a woodchuck could chuck wood",
        "Peter Piper picked a peck of pickled peppers"
    ]
    
    print("\nTesting with sample sentences:")
    for sentence in test_cases:
        print(f"\nAnalyzing: {sentence}")
        print("=" * 60)
        
        for n in [2, 3, 4]:
            print(f"\n{n}-grams:")
            results = analyze_sentence(sentence, n)
            print_results(results)

def main():
    """Main function to run the tests."""
    test_sentences()

if __name__ == "__main__":
    main() 