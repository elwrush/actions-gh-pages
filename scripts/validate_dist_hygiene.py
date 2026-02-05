
import os
import sys

def validate_dist():
    dist_dir = "dist"
    if not os.path.exists(dist_dir):
        print("[SKIP] No dist/ folder to validate.")
        return True

    errors = []
    
    # 1. Check for PDFs in dist/
    for root, dirs, files in os.walk(dist_dir):
        for file in files:
            if file.endswith(".pdf"):
                errors.append(f"FORBIDDEN: PDF file found in distribution: {os.path.join(root, file)}")

    # 2. Check for engine duplication in subfolders
    # root/dist/lesson/dist should not exist
    for entry in os.listdir(dist_dir):
        lesson_path = os.path.join(dist_dir, entry)
        if os.path.isdir(lesson_path) and entry not in ['dist', 'plugin', 'css', 'images', 'skills']:
            for engine_folder in ['dist', 'plugin', 'css']:
                if os.path.exists(os.path.join(lesson_path, engine_folder)):
                    errors.append(f"FORBIDDEN: Duplicate engine folder '{engine_folder}' found in: {lesson_path}")

    if errors:
        print("\n[FAILED] Distribution Hygiene Validation Failed:")
        for err in errors:
            print(f"  - {err}")
        return False
    
    print("\n[PASSED] Distribution Hygiene is perfect.")
    return True

if __name__ == "__main__":
    if not validate_dist():
        sys.exit(1)
