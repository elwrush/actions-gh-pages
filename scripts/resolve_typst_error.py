import sys
import subprocess
import os
import re

TYPST_CODEBASE = r"C:\PROJECTS\WRITING-ASSESSMENT	emp_typst_repo"

def suggest_fix(error_msg):
    """
    Analyzes a Typst error message and suggests a fix based on known patterns
    and codebase searches.
    """
    print(f"Analyzing error: {error_msg}")
    
    # Pattern 1: Unclosed Delimiter near function calls
    if "unclosed delimiter" in error_msg:
        print("
[DIAGNOSIS]: The parser is likely confusing a literal '(' or '[' with a code block delimiter.")
        print("[SOLUTION 1]: Wrap the content in a string: #text("(___)")")
        print("[SOLUTION 2]: Abstract the function into a variable: #let gap = h(1fr) -> #gap (text)")
        
        # Search for examples in codebase
        print("
[CODEBASE EXAMPLES]:")
        search_cmd = ["rg", "unclosed delimiter", TYPST_CODEBASE, "-C", "2"]
        subprocess.run(search_cmd, shell=True)
        return

    # Pattern 2: Unknown variable/function
    match = re.search(r"unknown variable: `(.*)`", error_msg)
    if match:
        var_name = match.group(1)
        print(f"
[DIAGNOSIS]: The variable '{var_name}' is not defined.")
        print(f"[SOLUTION]: Check if you need to import it from @local/bell-sheets or define it.")
        
        # Search for definition
        print(f"
[SEARCHING DEFINITION]:")
        search_cmd = ["rg", f"let {var_name}", TYPST_CODEBASE]
        subprocess.run(search_cmd, shell=True)
        return

    print("
[GENERIC SEARCH]: Searching codebase for error keywords...")
    # Extract key terms
    keywords = [w for w in error_msg.split() if len(w) > 4][:2]
    if keywords:
        search_cmd = ["rg", keywords[0], TYPST_CODEBASE]
        subprocess.run(search_cmd, shell=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python resolve_typst_error.py <error_message>")
    else:
        suggest_fix(sys.argv[1])