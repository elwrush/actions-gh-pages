import re
import sys
import os
from pathlib import Path

def validate_worksheet_layout(file_path):
    """
    Validates the layout of a Typst worksheet based on strict project rules.
    This acts as a programmatic "test" in a TDD-style workflow.
    """
    print(f"🔬 Running Layout Validation Test on: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ [FAIL] File not found: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    errors = []

    # 1. RED: Test for Task & Content Integrity
    tasks = re.split(r'(#task_header\(.*?\))', content)
    if len(tasks) > 1:
        for i in range(1, len(tasks), 2):
            header = tasks[i]
            body = tasks[i+1] if (i+1) < len(tasks) else ""
            if not body.strip().startswith("#block(breakable: false"):
                task_name_match = re.search(r'"(.*?)"', header)
                task_name = task_name_match.group(1) if task_name_match else "Unknown"
                errors.append(
                    f"[FAIL] Task Integrity Violation: Task '{task_name}' is not wrapped in a non-breakable block."
                )

    # 2. RED: Test for Aligned Answer Lines
    # Look for grid blocks that contain enums
    grid_pattern = re.compile(r'#grid\(.*?\[(.*?)\]', re.DOTALL)
    for grid_match in grid_pattern.finditer(content):
        grid_content = grid_match.group(1)
        if "#set enum" in grid_content:
            # Extract the enum items - match '+' at start of line or after newline+spaces
            items = re.findall(r'(?:^|\n)\s*\+ (.*?)(?=\n\s*\+ |$)', grid_content, re.DOTALL)
            for item in items:
                clean_item = item.strip()
                if clean_item and not (clean_item.startswith('#box') and '[#hide[a]]' in clean_item):
                     errors.append(
                        f"[FAIL] Line Alignment Violation: Found an answer line not using the standard '#box...[#hide[a]]' method. Content: '{clean_item}'"
                     )

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
