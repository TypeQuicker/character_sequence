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

def clean_word(word):
    """Return a lowercase word stripped of non-alpha characters."""
    return re.sub(r'[^a-z]', '', word.lower())

def extract_clean_words(text):
    """Split and clean words from raw text input."""
    return [clean_word(word) for word in text.split() if clean_word(word)]

def get_words_from_text(text):
    """Get all valid words from text."""
    word_counts = Counter(extract_clean_words(text))
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
                results[ngram] = {'count': 0, 'words': {}}
            results[ngram]['count'] += word_freq
            results[ngram]['words'][word] = word_freq
    return results

def get_ngram_transitions_from_text(text, n):
    """Get n-gram transitions and their source word pairs."""
    clean_words = extract_clean_words(text)
    results = {}

    for i in range(len(clean_words) - 1):
        word1 = clean_words[i]
        word2 = clean_words[i + 1]

        if len(word1) >= n and len(word2) >= n:
            first_ngram = word1[-n:]
            second_ngram = word2[:n]
            transition = f"{first_ngram} {second_ngram}"
            pair = f"{word1} {word2}"

            if transition not in results:
                results[transition] = {'count': 0, 'words': {}}
            results[transition]['count'] += 1
            results[transition]['words'][pair] = results[transition]['words'].get(pair, 0) + 1

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

def get_top_unique_words(sorted_words, limit=3):
    """Return up to `limit #` of unique words for the csv output."""
    sample_words = []
    for word, _ in sorted_words:
        if word not in sample_words:
            sample_words.append(word)
        if len(sample_words) == limit:
            break
    return sample_words

def save_ngram_results(ngram_data, output_file):
    """Save results to a CSV file."""
    with open(output_file, 'w') as f:
        f.write("sequence,count,common_words\n")
        # Sort n-grams by occurence
        sorted_ngrams = sorted(ngram_data.items(), key=sort_by_count)
        for ngram, data in sorted_ngrams:
            count = data['count']
            sorted_words = sorted(data['words'].items(), key=sort_by_count)
            sample_words = []
            
            sample_words = get_top_unique_words(sorted_words, limit=3)
            
            common_words = ", ".join(sample_words)
            f.write(f"{ngram},{count},{common_words}\n")

def save_transition_results(transition_data, output_file):
    """Save transition results to a CSV file."""
    with open(output_file, 'w') as f:
        f.write("transition,count,common_words\n")
        # Sort transitions by occurence
        sorted_transitions = sorted(transition_data.items(), key=sort_by_count)
        
        for transition, data in sorted_transitions:
            count = data['count']
            sorted_words = sorted(data['words'].items(), key=sort_by_count)
            sample_words = []
            
            sample_words = get_top_unique_words(sorted_words, limit=3)

            common_words = ", ".join(sample_words)
            f.write(f"{transition},{count},{common_words}\n")