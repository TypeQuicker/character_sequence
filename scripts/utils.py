import re
from collections import Counter

def clean_text(text):
    """Make text lowercase and remove special characters."""
    text = text.lower()
    text = re.sub(r'\\[nrt]', ' ', text)
    text = re.sub(r'http[s]?://\S+', ' ', text)
    text = re.sub(r'www\.\S+', ' ', text)
    text = re.sub(r'/\S+', ' ', text)
    text = re.sub(r'&[a-z]+;', ' ', text)
    text = re.sub(r'[^a-z\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def get_words_from_text(text):
    """Get all valid words from text."""
    words = text.split()
    good_words = []
    for word in words:
        clean_word = re.sub(r'[^a-z]', '', word.lower())
        if clean_word:
            good_words.append(clean_word)
    word_counts = Counter(good_words)
    return word_counts

def get_ngrams_from_text(text, n):
    """Get n-grams and their source words."""
    word_counts = get_words_from_text(text)
    results = {}
    for word, word_freq in word_counts.items():
        if len(word) < n:
            continue
        for i in range(len(word) - n + 1):
            ngram = word[i:i+n]
            if ngram not in results:
                results[ngram] = {
                    'count': 0,
                    'words': {}
                }
            results[ngram]['count'] += word_freq
            results[ngram]['words'][word] = word_freq
    return results

def count_items(items):
    """Count how many times each item appears."""
    counts = {}
    for item in items:
        if item not in counts:
            counts[item] = 0
        counts[item] += 1
    return counts

def sort_by_count(item):
    """Sort items by count (highest first)."""
    data = item[1]
    if isinstance(data, dict):
        count = data['count']
    else:
        count = data
    return -count 

def save_results(ngram_data, output_file):
    """Save results to a CSV file."""
    with open(output_file, 'w') as f:
        f.write("sequence,count,common_words\n")
        # Sort n-grams by count (highest first)
        sorted_ngrams = sorted(ngram_data.items(), key=sort_by_count)
        for ngram, data in sorted_ngrams:
            count = data['count']
            sorted_words = sorted(data['words'].items(), key=sort_by_count)
            sample_words = []
            for word, _ in sorted_words[:3]: # Only look at first 3 words
                if word not in sample_words: # Avoid duplicating sample_words. E.g. Incorrect 4-gram: that,771,that, that, that Correct 4-gram: that,771,that
                    sample_words.append(word)
            common_words = ", ".join(sample_words)
            f.write(f"{ngram},{count},{common_words}\n")