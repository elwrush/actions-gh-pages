import os
import sys

def validate_dist_hygiene(dist_dir):
    """
    Checks the dist directory for forbidden files (source materials, non-web assets).
    """
    forbidden_extensions = {'.typ', '.pdf', '.json', '.md', '.py', '.txt', '.bak', '.backup'}
    forbidden_files = {'presentation.json', 'slide_architecture.md', 'desktop.ini', 'Thumbs.db'}
    
    issues = []
    
    if not os.path.exists(dist_dir):
        print(f"Error: Dist directory not found: {dist_dir}")
        sys.exit(1)

    print(f"🔍 Validating hygiene of: {dist_dir}")

    for root, dirs, files in os.walk(dist_dir):
        for file in files:
            file_path = os.path.join(root, file)
            ext = os.path.splitext(file)[1].lower()
            
            # 1. Extension Check
            if ext in forbidden_extensions:
                # Exception: root index.html is allowed, but no other .json (wait, index.html is not .json)
                # We allow .json only in specific reveal.js engine folders if necessary, but build_dist.js should have filtered them.
                issues.append(f"Forbidden extension '{ext}': {file_path}")
            
            # 2. Filename Check
            if file in forbidden_files or file.lower() in forbidden_files:
                issues.append(f"Forbidden file '{file}': {file_path}")

    if issues:
        print("\n❌ HYGIENE VALIDATION FAILED!")
        for issue in issues:
            print(f"  - {issue}")
        print("\nClean the 'dist/' folder and fix the build script before deploying.")
        sys.exit(1)
    else:
        print("\n✅ Hygiene validation passed. No source materials found in dist/.")

if __name__ == "__main__":
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dist_path = os.path.join(project_root, 'dist')
    
    validate_dist_hygiene(dist_path)