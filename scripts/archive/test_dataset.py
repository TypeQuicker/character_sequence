from datasets import load_dataset
import sys

def test_dataset_connection():
    """Test connection to the HuggingFace dataset and print first book sample."""
    try:
        ds = load_dataset("manu/project_gutenberg", split="en", streaming=True) 
        first_row = next(iter(ds))
        content = first_row.get('text', '')[:5000] # First 5000 characted of the text
        print(content)
        # Below method prints the entire first row
#       print(first_row)
        return True
        
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        return False

if __name__ == "__main__":
    success = test_dataset_connection()
    sys.exit(0 if success else 1) 