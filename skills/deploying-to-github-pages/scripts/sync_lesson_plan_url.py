import os
import sys
import re

def sync_url(folder_name):
    project_root = os.getcwd()
    inputs_dir = os.path.join(project_root, 'inputs', folder_name)
    
    if not os.path.exists(inputs_dir):
        print(f"❌ Error: Folder '{folder_name}' not found in inputs/")
        return

    # Base URL for GitHub Pages
    base_url = f"https://elwrush.github.io/actions-gh-pages/{folder_name}/"
    
    # Search for .typ file in inputs/[folder]/published or inputs/[folder]/
    typ_files = []
    search_paths = [os.path.join(inputs_dir, 'published'), inputs_dir]
    
    for path in search_paths:
        if os.path.exists(path):
            typ_files.extend([os.path.join(path, f) for f in os.listdir(path) if f.endswith('.typ')])
    
    if not typ_files:
        print(f"⚠️  No .typ files found for {folder_name}.")
        return

    pattern = re.compile(r'#slideshow_link\(".*?"\)')
    replacement = f'#slideshow_link("{base_url}")'
    
    for typ_file in typ_files:
        with open(typ_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern.search(content):
            new_content = pattern.sub(replacement, content)
            if new_content != content:
                with open(typ_file, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"✅ Updated URL in: {os.path.relpath(typ_file, project_root)}")
            else:
                print(f"ℹ️  URL already up to date in: {os.path.relpath(typ_file, project_root)}")
        else:
            # If no link exists, we might want to add it, but for now we follow the mandate 
            # to only update existing ones to avoid breaking formatting.
            print(f"ℹ️  No #slideshow_link found in: {os.path.relpath(typ_file, project_root)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python sync_lesson_plan_url.py <folder_name>")
        sys.exit(1)
    
    sync_url(sys.argv[1])
