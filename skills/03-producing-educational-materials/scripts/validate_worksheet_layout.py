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
    # Find all task_header calls
    task_headers = re.finditer(r'#task_header\((.*?)\)', content)
    for header_match in task_headers:
        full_header_call = header_match.group(0)
        task_name_match = re.search(r'"(.*?)"', full_header_call)
        task_name = task_name_match.group(1) if task_name_match else "Unknown Task"

        # Find the immediately preceding block(breakable: false, [...]) that encloses this task_header
        # This regex looks backwards for the start of the block and forwards for its end, encapsulating the header.
        # This is a challenging regex due to nested structures, so we'll use a multi-step check.
        
        # Step 1: Find the task_header
        header_start = header_match.start()
        
        # Step 2: Search backwards for the nearest #block(breakable: false, [
        block_start_pattern = r'#block\(breakable:\s*false,\s*\['
        block_start_match = None
        for match in re.finditer(block_start_pattern, content[:header_start]):
            block_start_match = match

        if block_start_match:
            block_start_pos = block_start_match.start()
            
            # Step 3: Check if this block also contains the closing bracket after the header
            # This is a heuristic, as true nested parsing is complex with regex.
            # We'll search for the closing `])` after the `block_start_pos`
            block_end_pattern = r'\]\)'
            block_end_match = re.search(block_end_pattern, content[header_start:])
            
            if not block_end_match:
                errors.append(
                    f"[FAIL] Task Integrity Violation: Task '{task_name}' is not correctly enclosed in a non-breakable block (missing closing '}}')."
                )
        else:
            errors.append(
                f"[FAIL] Task Integrity Violation: Task '{task_name}' is not wrapped in a non-breakable block."
            )

    # 2. RED: Test for Aligned Answer Lines
    # Look for grid blocks that contain enums
    grid_pattern = re.compile(r'#grid\(.*?\[(.*?)\]', re.DOTALL)
    expected_box_pattern = r'#box\(width: (\d+cm), stroke: \(bottom: 0\.75pt \+ black\), outset: \(bottom: 2pt\)\)\[#hide\[a\]\]'

    for grid_match in grid_pattern.finditer(content):
        grid_content = grid_match.group(1)
        if "#set enum" in grid_content:
            # Extract the enum items that match the expected box pattern
            items = re.findall(r'\+ (' + expected_box_pattern + r')', grid_content)
            
            # Also find any items that DON'T match the pattern but are preceded by '+'
            all_plus_items = re.findall(r'(?:^|\n)\s*\+ ([^+\n]*(?:\n[^+\n]*)*)(?=\n\s*\+ |$)', grid_content)
            
            for raw_item in all_plus_items:
                clean_item = raw_item.strip()
                if clean_item and not re.fullmatch(expected_box_pattern, clean_item):
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
