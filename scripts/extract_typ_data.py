import re
import os

def extract_sentences(typ_path):
    if not os.path.exists(typ_path):
        return []
    with open(typ_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for transcription answers in the Answer Key section
    # Pattern: 1. Tom likes writing poetry.
    # Note: Using multiline to find numbered lines
    answers = re.findall(r'^\s*\d+\.\s+([^/\n]+)$', content, re.MULTILINE)
    # Clean up whitespace and potential Typst markup
    cleaned = [a.strip() for p in answers for a in p.split('\n') if a.strip() and not a.startswith('/')]
    return cleaned

def extract_word_bank(typ_path):
    if not os.path.exists(typ_path):
        return []
    with open(typ_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Look for the word bank inside the block
    # Pattern: [w#underline[a]lk], [wr#underline[o]ng]...
    words = re.findall(r'\[([^\]]+)\]', content)
    # Filter for words that look like our vocab (contain underlining or are short strings)
    cleaned = []
    for w in words:
        # Strip underlining syntax: w#underline[a]lk -> walk
        clean_w = re.sub(r'#underline\[([^\]]+)\]', r'\1', w)
        if len(clean_w.split()) == 1 and clean_w.isalpha():
            cleaned.append(clean_w)
    return list(set(cleaned)) # Unique words

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        print("Sentences:", extract_sentences(sys.argv[1]))
        print("Words:", extract_word_bank(sys.argv[1]))
