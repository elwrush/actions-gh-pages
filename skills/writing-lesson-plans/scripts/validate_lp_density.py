import os
import sys
import re

def validate_density(file_path):
    if not os.path.exists(file_path):
        print(f"[ERROR] File not found: {file_path}")
        return False

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find procedures in stage calls: stage("num", "name", "time", "goal", [procedure], "int")
    # We look for the 5th argument (the procedure) which is inside [ ]
    # stage\s*\(\s*".*?",\s*".*?",\s*".*?",\s*".*?",\s*\[(.*?)(\s*,\s*".*?")?\]\s*\)
    procedure_matches = re.findall(r'stage\s*\(\s*".*?",\s*".*?",\s*".*?",\s*".*?",\s*\[(.*?)\]', content, re.DOTALL)

    if not procedure_matches:
        print("[ERROR] No stages found in lesson plan. Did you use the #stage() helper?")
        return False

    errors = []
    MIN_CHARS_PER_STAGE = 150 # Absolute minimum for a professional procedure

    for i, proc in enumerate(procedure_matches):
        stage_num = i + 1
        clean_proc = proc.strip()
        
        # 1. Length Check
        if len(clean_proc) < MIN_CHARS_PER_STAGE:
            errors.append(f"Stage {stage_num}: Procedure is too thin ({len(clean_proc)} chars). Needs more granular pedagogical detail.")

        # 2. Interaction Marker Check
        if not re.search(r'(T-S|S-S|Ss-Ss|Pairs|Indiv|Group|Elicit|CCQ)', clean_proc, re.IGNORECASE):
             errors.append(f"Stage {stage_num}: Missing interaction markers or elicitation cues (Elicit, CCQ, T-S) within the procedure text.")

        # 3. Slide Reference Check (BANNED)
        if re.search(r'Slide\s*\d+', clean_proc, re.IGNORECASE):
            errors.append(f"Stage {stage_num}: BANNED LANGUAGE. Do not refer to specific slide numbers (e.g., 'Slide 4'). Refer to the content instead.")

    if errors:
        print(f"\n[FAILED] Procedural Density Check Failed for {file_path}:")
        for err in errors:
            print(f"  - {err}")
        return False

    print(f"\n[PASSED] Procedural density for {file_path} is professional.")
    return True

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate_lp_density.py <path_to_lp.typ>")
        sys.exit(1)
    
    if not validate_density(sys.argv[1]):
        sys.exit(1)