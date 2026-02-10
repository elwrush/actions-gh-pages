import sys
import re

def validate_density(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # 1. Check for "Part 1", "Part 2" structure (Modeling the YAML density)
    if "Part 1" not in content or "Part 2" not in content:
        issues.append("❌ Procedural Thinness: The model uses 'Part 1, Part 2' to build stages. Your plan is too simple.")
    
    # 2. Check for Classroom Management (Mini WBs, Feedback marks)
    if "Feedback" not in content:
        issues.append("❌ Missing Feedback Loops: The model mandates granular feedback (e.g., '1 min. Feedback').")
    
    if "mini WB" not in content.lower() and "whiteboard" not in content.lower():
        issues.append("❌ Missing Physical Interaction: The model explicitly uses Mini-Whiteboards for engagement.")

    if issues:
        for i in issues: print(i)
        return False
    return True

if __name__ == "__main__":
    if not validate_density(sys.argv[1]):
        sys.exit(1)
