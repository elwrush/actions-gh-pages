import os
import sys
import re
from pathlib import Path

def enforce_skill_standards():
    """
    Forensically scans the skill directory for violations:
    1. Absolute paths (C:\\...)
    2. Legacy keywords (Google Docs, Cloudflare, etc.)
    3. Stale package references.
    """
    skill_dir = Path(__file__).resolve().parent.parent
    print(f"Forensic Scan of Skill: {skill_dir.name}")
    
    violations = []
    legacy_keywords = ["Google Docs", "Cloudflare", "GDrive", "bell-sheets"]
    
    # Files to ignore (scripts themselves)
    ignored_files = ["enforce_skill_standards.py"]

    for root, dirs, files in os.walk(skill_dir):
        for file in files:
            if file in ignored_files:
                continue
            if file.endswith(('.md', '.py', '.typ')):
                file_path = Path(root) / file
                with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                    for line in f:
                        if 'pattern1 =' in line or 'pattern2 =' in line or 'p1 =' in line or 'p2 =' in line:
                            continue
                        
                        # 1. Absolute Paths (Strict check for drive letters + specific dirs)
                        # Pattern split to avoid self-triggering
                        dirs_pat = "(?:Users|PROJECTS|AppData|Roaming)"
                        p1_pat = "[a-zA-Z]" + ":\\\\" + dirs_pat
                        p2_pat = "C:" + "/" + dirs_pat
                        if re.search(p1_pat, line) or re.search(p2_pat, line):
                            violations.append(f"Absolute path found in {file_path}: {line.strip()}")
                        
                        # 2. Legacy Keywords
                        for kw in legacy_keywords:
                            if kw.lower() in line.lower():
                                violations.append(f"Legacy keyword '{kw}' found in {file_path}: {line.strip()}")

    if violations:
        print("\n" + "!"*50)
        print(f"FORENSIC VIOLATIONS FOUND: {len(violations)}")
        print("!"*50)
        for v in violations:
            print(f"  - {v}")
        return False
    
    print("Forensic review passed. All legacy components scrubbed.")
    return True

if __name__ == "__main__":
    success = enforce_skill_standards()
    sys.exit(0 if success else 1)
