#!/usr/bin/env python3
"""
Fast Edit Script - Streamlines presentation editing workflow

This script eliminates the need for manual multi-file edits by:
1. Focusing on presentation.json as single source of truth
2. Automatically regenerating published HTML
3. Rebuilding dist version

Usage: python scripts/fast_edit.py <lesson_name> [--no-rebuild]
Example: python scripts/fast_edit.py 05-02-2026-Gold-Infographic-B1
"""

import os
import sys
import subprocess
import argparse
import webbrowser
import time

def main():
    # Ensure server is running
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(scripts_dir)
    ensure_server_script = os.path.join(project_root, '.gemini', 'hooks', 'ensure-server.py')
    if os.path.exists(ensure_server_script):
        subprocess.run([sys.executable, ensure_server_script])

    parser = argparse.ArgumentParser(description='Fast edit presentation')
    parser.add_argument('lesson_name', help='Name of the lesson folder')
    parser.add_argument('--no-rebuild', action='store_true', help='Skip rebuilding dist')
    parser.add_argument('--open', action='store_true', help='Open the presentation in the browser')
    
    args = parser.parse_args()
    
    lesson_name = args.lesson_name
    # Correctly identify project root (parent of scripts folder)
    scripts_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(scripts_dir)
    
    inputs_dir = os.path.join(project_root, 'inputs', lesson_name)
    json_path = os.path.join(inputs_dir, 'presentation.json')
    
    if not os.path.exists(json_path):
        print(f"[X] Presentation not found: {json_path}")
        print(f"Available presentations in inputs/:")
        for folder in os.listdir(os.path.join(project_root, 'inputs')):
            if os.path.isdir(os.path.join(project_root, 'inputs', folder)):
                print(f"  - {folder}")
        return False
    
    print(f"[!] Fast Edit starting for: {lesson_name}")
    
    # Step 1: Generate HTML from JSON
    print("\n[*] Generating HTML from presentation.json...")
    generate_cmd = [
        sys.executable, 
        os.path.join(project_root, 'skills', 'creating-html-presentation', 'scripts', 'generate_presentation.py'),
        json_path
    ]
    
    try:
        result = subprocess.run(generate_cmd, check=True, capture_output=True, text=True, encoding='utf-8')
        if result.stdout:
            print(result.stdout.strip())
    except subprocess.CalledProcessError as e:
        print(f"[X] Error generating HTML: {e}")
        if e.stderr:
            print(e.stderr.strip())
        return False
    
    if args.no_rebuild:
        print("\n[*] Fast Edit complete! Skipping dist rebuild.")
        print(f"[*] Published HTML: {os.path.join(inputs_dir, 'published', 'index.html')}")
        return True
    
    # Step 2: Rebuild dist
    print("\n[*] Rebuilding dist...")
    build_cmd = [
        sys.executable,
        os.path.join(project_root, 'build.py'),
        lesson_name
    ]
    
    try:
        result = subprocess.run(build_cmd, check=True, capture_output=True, text=True, encoding='utf-8')
        if result.stdout:
            try:
                print(result.stdout.strip())
            except UnicodeEncodeError:
                print("[Build output with emojis - skipping display]")
    except subprocess.CalledProcessError as e:
        print(f"[X] Error building dist: {e}")
        if e.stderr:
            print(e.stderr.strip())
        return False
    
    print("\n[*] Fast Edit complete!")
    print(f"[*] Dist location: {os.path.join(project_root, 'dist', lesson_name)}")
    
    url = f"http://127.0.0.1:8000/{lesson_name}/"
    print(f"[*] URL: {url}")
    
    if args.open:
        print(f"[*] Opening browser: {url}")
        webbrowser.open(url)
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
