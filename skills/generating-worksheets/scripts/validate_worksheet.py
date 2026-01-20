"""
Worksheet Validator for Typst Templates
========================================
Validates worksheets against branding and layout rules.

Usage:
    python validate_worksheet.py <path/to/worksheet.typ> --mode [bell|intensive]
"""

import argparse
import os
import re
import subprocess
import sys

def validate_worksheet(typ_path, mode):
    print(f"[INFO] Validating {typ_path} in '{mode}' mode...")
    
    if not os.path.exists(typ_path):
        print(f"[ERROR] CRITICAL: File not found: {typ_path}")
        return False

    with open(typ_path, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []
    warnings = []

    # =========================================
    # 1. HEADER VALIDATION
    # =========================================
    
    # Check for Bell assets
    has_bell_logo = "Bell.svg" in content or "ACT_transparent.png" in content
    has_bell_text = "BELL LANGUAGE CENTRE" in content
    
    # Check for Intensive header
    has_intensive_header = "intensive-header.jpg" in content
    
    if mode == "bell":
        if not has_bell_logo:
            warnings.append("[WARN] Branding Warning: Bell logos (Bell.svg, ACT_transparent.png) not found.")
        if has_intensive_header:
            issues.append("[ERROR] Branding Violation: 'intensive-header.jpg' found in a BELL worksheet.")
    
    elif mode == "intensive":
        if has_bell_logo or has_bell_text:
            issues.append("[ERROR] Branding Violation: Bell logos or 'BELL LANGUAGE CENTRE' text found in INTENSIVE worksheet. Use intensive-header.jpg instead.")
        if not has_intensive_header:
            warnings.append("[WARN] Branding Warning: 'intensive-header.jpg' not found. Is the header correct?")

    # =========================================
    # 2. WRITING LINES VALIDATION
    # =========================================
    
    # Check for writing_lines calls and their counts
    writing_line_matches = re.findall(r'writing_lines\s*\(\s*count\s*:\s*(\d+)\s*\)', content)
    
    for match in writing_line_matches:
        count = int(match)
        if count > 15:
            issues.append(f"[ERROR] Layout Violation: writing_lines(count: {count}) exceeds the 15-line limit. Risk of spillover.")
        elif count > 12:
            warnings.append(f"[WARN] Layout Warning: writing_lines(count: {count}) is high. Verify it fits on one page.")

    # =========================================
    # 3. IMAGE PATH VALIDATION
    # =========================================
    
    # Find all image paths
    image_matches = re.findall(r'image\s*\(\s*["\']([^"\']+)["\']', content)
    base_dir = os.path.dirname(typ_path)
    project_root = os.path.abspath(os.path.join(base_dir, "..", ".."))  # Assumes standard structure
    # Try looking for project root by checking for common files if the above fails
    if not os.path.exists(os.path.join(project_root, ".agent")):
         # Fallback: Assume we are running from project root or similar
         project_root = os.getcwd()

    for img_path in image_matches:
        # Resolve path
        if img_path.startswith("/"):
            # Absolute from project root - Typst absolute paths are from project root
            # We need to be careful here. In the script, we might need to map "/" to the actual project root on disk.
            # However, for checking file existence, we can try prepending the determined project_root
            full_path = os.path.join(project_root, img_path.lstrip("/"))
        else:
            # Relative to file
            full_path = os.path.normpath(os.path.join(base_dir, img_path))
        
        # Simple existence check
        if not os.path.exists(full_path):
             # Try one more heuristic: sometimes people run from project root, so relative paths might be relative to CWD
             full_path_cwd = os.path.abspath(img_path)
             if not os.path.exists(full_path_cwd):
                issues.append(f"[ERROR] Broken Image: '{img_path}' does not exist at {full_path}")

    # =========================================
    # 4. PAGEBREAK CHECK
    # =========================================
    
    pagebreak_count = content.count("#pagebreak()")
    task_count = len(re.findall(r'task_card|task_header', content))
    
    if task_count > 1 and pagebreak_count < task_count - 1:
        warnings.append(f"[WARN] Pagination Warning: {task_count} tasks found but only {pagebreak_count} pagebreaks. Risk of spillover.")

    # =========================================
    # 5. OPTIONAL: COMPILE CHECK
    # =========================================
    
    # Try to compile and check for errors
    try:
        # We need to set --root to the project root to find absolute image paths
        result = subprocess.run(
            ["typst", "compile", typ_path, "--root", project_root],
            capture_output=True,
            text=True,
            timeout=30
        )
        if result.returncode != 0:
            issues.append(f"[ERROR] Compilation Error: {result.stderr.strip()}")
    except FileNotFoundError:
        warnings.append("[WARN] Typst CLI not found. Skipping compilation check.")
    except subprocess.TimeoutExpired:
        warnings.append("[WARN] Compilation timed out.")

    # =========================================
    # REPORTING
    # =========================================
    
    print("\n--- VALIDATION REPORT ---")
    if warnings:
        for w in warnings:
            print(w)
            
    if issues:
        for i in issues:
            print(i)
        print(f"\n[FAIL] FAILED: {len(issues)} critical issues found.")
        return False
    else:
        print("\n[PASS] PASSED: No critical issues found.")
        return True


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Typst worksheet against branding and layout rules.")
    parser.add_argument("file", help="Path to the .typ worksheet file")
    parser.add_argument("--mode", choices=["bell", "intensive"], required=True, help="Branding mode")
    
    args = parser.parse_args()
    
    success = validate_worksheet(args.file, args.mode)
    if not success:
        sys.exit(1)
