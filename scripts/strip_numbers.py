import re
import os

def clean_source_text(input_path, output_path):
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove paragraph markers like [1], [2], etc.
    # Note: The file has \[1\] because of the view_file escaping, 
    # but the raw file likely has [1]. I'll handle both just in case.
    cleaned_content = re.sub(r'\\?\[\d+\]\s*', '', content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)
    
    print(f"Cleaned text saved to: {output_path}")

if __name__ == "__main__":
    src = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\SORUCE-TEXT2.md"
    dest = r"G:\Other computers\My PC (1)\PROJECTS\LESSONS AND SLIDESHOWS 2\inputs\2026-02-11-B2-READING-AN-ADVENTURE-STORY\CLEAN-TEXT.md"
    clean_source_text(src, dest)
