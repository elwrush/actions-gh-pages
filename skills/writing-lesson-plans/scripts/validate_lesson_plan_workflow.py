import argparse
import os
import sys

def check_file_exists(path, description):
    if os.path.exists(path):
        print(f"✅ {description} Found: {path}")
        return True
    else:
        print(f"❌ {description} Missing: {path}")
        return False

def validate_workflow(lesson_folder):
    print(f"🛡️  Validating Lesson Plan Workflow for: {lesson_folder}")
    base_dir = os.path.abspath(os.path.join("inputs", lesson_folder))
    
    if not os.path.exists(base_dir):
        print(f"❌ Lesson directory not found: {base_dir}")
        sys.exit(1)

    all_passed = True

    # 1. Shape Selection Gate
    # Check if a shape has been explicitly selected in a metadata file or log
    # For now, we'll check if the Typst file contains a valid @shape label or metadata
    typ_files = [f for f in os.listdir(base_dir) if f.endswith('.typ')]
    if not typ_files:
        print("❌ No Typst Lesson Plan found. You must complete the Shape Selection and Lesson Planning phase first.")
        all_passed = False
    else:
        print(f"✅ Typst Lesson Plan Found: {typ_files[0]}")
        # TODO: parse typ file for shape metadata

    # 1.5 PDF Existence Check
    pdf_path = os.path.join(base_dir, "lesson_plan.pdf")
    if not check_file_exists(pdf_path, "Compiled Lesson Plan PDF"):
        print("❌ Lesson Plan PDF missing. You MUST compile `lesson_plan.typ` and get user approval.")
        all_passed = False

    # 2. Visual Roadmap Gate
    roadmap_path = os.path.join(base_dir, "visual_plan.md")
    if not check_file_exists(roadmap_path, "Visual Roadmap"):
        print("❌ CRITICAL: Visual Roadmap missing. You must strictly follow the 'Roadmap First Law'.")
        all_passed = False

    if all_passed:
        print("✅ Workflow Validation Passed.")
        sys.exit(0)
    else:
        print("🛑 Workflow Validation Failed.")
        sys.exit(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Lesson Plan Workflow")
    parser.add_argument("folder_name", help="Name of the lesson folder")
    args = parser.parse_args()
    validate_workflow(args.folder_name)
