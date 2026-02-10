import argparse
import os
import sys
import re

def validate_typst_structure(file_path):
    print(f"🛡️  Validating Typst Structure: {file_path}")
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    issues = []

    # 1. Check Slideshow Link Placement
    # Pattern: #differentiation_box(...) followed by #slideshow_link(...) followed by #stage_table(...)
    # We strip whitespace to make regex robust
    clean_content = re.sub(r'\s+', ' ', content)
    
    # Check if link exists
    if "#slideshow_link" not in content:
        issues.append("❌ Missing #slideshow_link(...) function.")
    else:
        # Check order: diff -> link -> stage
        diff_pos = clean_content.find("#differentiation_box")
        link_pos = clean_content.find("#slideshow_link")
        stage_pos = clean_content.find("#stage_table")
        
        if diff_pos == -1:
             issues.append("❌ Missing #differentiation_box(...).")
        if stage_pos == -1:
             issues.append("❌ Missing #stage_table(...).")
             
        if diff_pos != -1 and link_pos != -1 and stage_pos != -1:
            if not (diff_pos < link_pos < stage_pos):
                issues.append("❌ Invalid Order: #slideshow_link MUST be between #differentiation_box and #stage_table.")

    # 2. Check Stage Headers against Shape E (Receptive Skills) as default check
    # Ideally this script should know the shape. For now, we warn if we see "Phase 1" style headers.
    
    if 'stage("1", "Phase 1' in content or 'stage("1", "Context' in content:
        issues.append("❌ Invalid Stage Header: Do not use 'Phase X' or 'Context'. Use standard Shape names like 'Lead-in'.")

    # Check for "Lead-in" if it's a standard lesson
    if 'stage("1", "Lead-in"' not in content and 'stage("1", "Situation' not in content:
         # Soft warning as some shapes differ
         print("⚠️  Warning: Stage 1 is usually 'Lead-in' or 'Situation'. Verify against REFERENCE.md.")

    if issues:
        for issue in issues:
            print(issue)
        return False
    
    print("✅ Typst Structure Validated.")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Typst Lesson Plan Structure")
    parser.add_argument("file_path", help="Path to .typ file")
    args = parser.parse_args()
    
    success = validate_typst_structure(args.file_path)
    sys.exit(0 if success else 1)
