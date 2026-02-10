import os
import sys
import subprocess

TYPST_CODEBASE = r"C:\PROJECTS\WRITING-ASSESSMENT\temp_typst_repo"

def search_codebase(pattern, include_tests=True):
    print(f"Searching Typst codebase for: {pattern}")
    
    # Use ripgrep via shell if available, or fall back to a simple walk
    try:
        cmd = ["rg", pattern, TYPST_CODEBASE, "--type", "rust", "--type", "typst"]
        if not include_tests:
            cmd.extend(["-g", "!tests/**"])
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.stdout:
            print(result.stdout[:2000]) # Truncate for brevity
            return result.stdout
        else:
            print("No matches found in codebase.")
            return None
    except FileNotFoundError:
        # Fallback to os.walk
        matches = []
        for root, dirs, files in os.walk(TYPST_CODEBASE):
            for file in files:
                if file.endswith((".rs", ".typ")):
                    path = os.path.join(root, file)
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            for i, line in enumerate(f):
                                if pattern in line:
                                    matches.append(f"{path}:{i+1}: {line.strip()}")
                                    if len(matches) > 20: break
                    except:
                        pass
            if len(matches) > 20: break
        
        for m in matches:
            print(m)
        return "\n".join(matches)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python search_typst_codebase.py <pattern>")
    else:
        search_codebase(sys.argv[1])