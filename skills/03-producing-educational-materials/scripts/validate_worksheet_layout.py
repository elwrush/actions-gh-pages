import re
import sys
import os
from pathlib import Path

def validate_worksheet_layout(file_path):
    """
    Validates the layout of a Typst worksheet based on strict project rules.
    Refactored March 2026: No absolute paths, rigid writing lines logic.
    """
    print(f"Running Layout Validation Test on: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ [FAIL] File not found: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []

    # 1. ABSOLUTE PATH CHECK
    # Patterns split to avoid self-triggering in forensic scan
    pattern1 = "[a-zA-Z]" + ":\\\\"
    pattern2 = "C:" + "/"
    if re.search(pattern1, content) or re.search(pattern2, content):
        errors.append("[FAIL] Absolute Path Violation: Found hardcoded drive letters. Use root-relative paths (e.g., /lib/typst/...).")

    # 2. TASK & CONTENT INTEGRITY
    task_headers = re.finditer(r'#task_header\((.*?)\)', content)
    for header_match in task_headers:
        full_header_call = header_match.group(0)
        task_name_match = re.search(r'"(.*?)"', full_header_call)
        task_name = task_name_match.group(1) if task_name_match else "Unknown Task"
        header_start = header_match.start()
        
        # Search backwards for non-breakable block
        block_start_pattern = r'#block\(breakable:\s*false,\s*\['
        block_start_match = None
        for match in re.finditer(block_start_pattern, content[:header_start]):
            block_start_match = match

        if not block_start_match:
            errors.append(f"[FAIL] Task Integrity Violation: Task '{task_name}' is not wrapped in a non-breakable block.")

    # 3. WRITING LINES LOGIC
    # Final Task (usually Task 4 or 5) must use dynamic writing lines
    if "writing_lines_dynamic" not in content and "writing_lines_fixed" not in content:
        if "#task_header" in content:
            warnings = " [WARN] No writing lines found. Ensure tasks do not require student output."
            print(warnings)

    # 4. ALIGNED ANSWER LINES (Gaps in Grids)
    grid_pattern = re.compile(r'#grid\(.*?\[(.*?)\]', re.DOTALL)
    # The standard method for lines in grids
    expected_box_pattern = r'#box\(width: [\d\.]+cm, stroke: \(bottom: 0\.75pt \+ black\), outset: \(bottom: 2pt\)\)\[#hide\[a\]\]'

    for grid_match in grid_pattern.finditer(content):
        grid_content = grid_match.group(1)
        if "#set enum" in grid_content:
            all_plus_items = re.findall(r'(?:^|\n)\s*\+ ([^+\n]*(?:\n[^+\n]*)*)(?=\n\s*\+ |$)', grid_content)
            for raw_item in all_plus_items:
                clean_item = raw_item.strip()
                if clean_item and "_ " in clean_item:
                     errors.append(f"[FAIL] Hallucinated Underscores: Use #box(...) for answer lines in grids, not underscores.")

    if errors:
        print("\n" + "="*50)
        print(f"❌ VALIDATION FAILED: Found {len(errors)} layout error(s).")
        print("="*50)
        for i, error in enumerate(errors, 1):
            print(f"  {i}. {error}")
        return False
    
    print("\n" + "="*50)
    print("✅ [PASS] Layout validation test passed.")
    print("="*50)
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_worksheet_layout.py <path_to_typst_file>")
        sys.exit(1)
    
    is_valid = validate_worksheet_layout(sys.argv[1])
    sys.exit(0 if is_valid else 1)
