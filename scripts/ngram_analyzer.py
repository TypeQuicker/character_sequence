"""
Main script to analyze n-grams in Project Gutenberg books.
This script reads a book, finds character patterns (n-grams),
and saves the results to CSV files.
"""

from datasets import load_dataset
from utils import clean_text, get_words_from_text, save_ngram_results, get_ngrams_from_text
import os

def analyze_book():
    """Analyze n-grams in a Project Gutenberg book."""
    # Create output folder if it doesn't exist
    os.makedirs('data/ngrams', exist_ok=True)
    
    dataset = load_dataset("manu/project_gutenberg", split="en", streaming=True)
    book = next(iter(dataset))
    
    # Clean the text
    clean_book_text = clean_text(book['text'])
    
    # Analyze different lengths of character patterns
    for n in [2, 3, 4]:
        print(f"\nLooking for {n}-letter patterns...")
        
        # Find n-grams and their source words
        ngram_data = get_ngrams_from_text(clean_book_text, n)
        
        # Save what we found
        output_file = f"data/ngrams/{n}grams.csv"
        save_ngram_results(ngram_data, output_file)
        print(f"Results saved to {output_file}")

if __name__ == "__main__":
    analyze_book()