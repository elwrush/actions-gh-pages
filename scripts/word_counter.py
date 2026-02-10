import sys
import re

def count_words(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
            # Remove punctuation and split by whitespace
            words = re.findall(r'\b\w+\b', text.lower())
            count = len(words)
            print(f"Word count for {file_path}: {count}")
            return count
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return 0

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python word_counter.py <file_path>")
        sys.exit(1)
    
    file_path = sys.argv[1]
    count_words(file_path)