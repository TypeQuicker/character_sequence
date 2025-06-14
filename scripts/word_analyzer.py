"""
Main script to analyze word occurences in Project Gutenberg books.
This script reads a book, counts word occurrences,
and saves the results to a CSV file.
"""

from datasets import load_dataset
from utils import clean_text, get_words_from_text, save_word_results
import os

def analyze_words():
    """Analyze word frequencies in a Project Gutenberg book."""
    # Create output folder if it doesn't exist
    os.makedirs('data/words', exist_ok=True)
    
    # First row of the dataset only
    dataset = load_dataset("manu/project_gutenberg", split="en", streaming=True)
    book = next(iter(dataset))
    clean_book_text = clean_text(book['text'])

    # All rows of the dataset
    # dataset = load_dataset("manu/project_gutenberg", split="en")
    # text = " ".join(book['text'] for book in dataset)
    # clean_book_text = clean_text(text)
    
    # Get word frequencies
    word_counts = get_words_from_text(clean_book_text)
    
    # Save to CSV
    output_file = "data/words/words.csv"
    save_word_results(word_counts, output_file)
    print(f"Word frequency results saved to {output_file}")

if __name__ == "__main__":
    analyze_words()
