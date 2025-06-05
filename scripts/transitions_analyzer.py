"""
Main script to analyze n-gram transitions in Project Gutenberg books.
This script reads a book, finds character pattern transitions between consecutive words (n-gram transitions),
and saves the results to CSV files.
"""

from datasets import load_dataset
from utils import clean_text, get_ngram_transitions_from_text, save_transition_results
import os

def analyze_transitions():
    """Analyze n-gram transitions in a Project Gutenberg book."""
    # Create output folder if it doesn't exist
    os.makedirs('data/transitions', exist_ok=True)
    
    dataset = load_dataset("manu/project_gutenberg", split="en", streaming=True)
    book = next(iter(dataset))
    
    # Clean the text
    clean_book_text = clean_text(book['text'])
    
    # Analyze different lengths of character pattern transitions
    for n in [2, 3, 4]:
        print(f"\nLooking for {n}-gram transitions...")
        
        # Find n-gram transitions and their source words
        transition_data = get_ngram_transitions_from_text(clean_book_text, n)
        
        # Save what we found
        output_file = f"data/transitions/{n}grams_transitions.csv"
        save_transition_results(transition_data, output_file)
        print(f"Results saved to {output_file}")

if __name__ == "__main__":
    analyze_transitions()