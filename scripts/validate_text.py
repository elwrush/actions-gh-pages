import sys
import os
import re

if len(sys.argv) < 2:
    print("Usage: python validate_text.py <file.typ>")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
    sys.exit(1)

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# Remove Typst comments
clean_text = re.sub(r'//.*', '', text)
clean_text = re.sub(r'/\*.*?\*/', '', clean_text, flags=re.DOTALL)

# Basic removal of Typst commands
clean_text = re.sub(r'#[a-zA-Z0-9_-]+', '', clean_text)
clean_text = re.sub(r'[*_=+]', '', clean_text)
clean_text = re.sub(r'\[|\]|\(|\)', ' ', clean_text)

def count_words(text):
    words = re.findall(r'\b\w+\b', text)
    return len(words)

print(f"Word Count (Approximate): {count_words(clean_text)}")
print("---TEXT START---")
print(clean_text.strip())
print("---TEXT END---")
