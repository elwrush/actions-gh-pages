import re
import argparse
import os
import sys

def sync_url(typ_path, live_url):
    """
    Updates the #slideshow_link("...") in a Typst file with the provided live URL.
    """
    if not os.path.exists(typ_path):
        print(f"Error: File not found: {typ_path}")
        sys.exit(1)

    print(f"Reading {typ_path}...")
    with open(typ_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find #slideshow_link("...") or #slideshow_link("...") with spaces
    # Supports single or double quotes
    pattern = r'(#slideshow_link\s*\(\s*["\'])(.*?)(["\']\s*\))'
    
    if not re.search(pattern, content):
        print(f"Warning: No #slideshow_link macro found in {typ_path}. Skipping update.")
        return

    new_content = re.sub(pattern, rf'\1{live_url}\3', content)

    if new_content == content:
        print(f"URL is already up to date: {live_url}")
    else:
        with open(typ_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Successfully updated live URL in {typ_path}")
        print(f"URL: {live_url}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sync live slideshow URL to Typst lesson plan.")
    parser.add_argument("typ_path", help="Path to the .typ lesson plan file")
    parser.add_argument("live_url", help="The direct live URL of the slideshow (GitHub Pages)")
    
    args = parser.parse_args()
    
    sync_url(args.typ_path, args.live_url)
