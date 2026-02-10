import sys
import subprocess
import os

def run_workflow_validation(folder_name):
    base_path = os.path.join("inputs", folder_name)
    script_path = os.path.join("skills", "writing-lesson-plans", "scripts", "validate_lesson_plan_workflow.py")
    struct_script = os.path.join("skills", "writing-lesson-plans", "hooks", "validate_typst_structure.py")
    density_script = os.path.join("skills", "writing-lesson-plans", "hooks", "validate_pedagogical_density.py")
    
    try:
        # 1. Run Workflow Check
        subprocess.run([sys.executable, script_path, folder_name], check=True)
        
        # 2. Run Typst Structure Check (Find the typ file first)
        published_dir = os.path.join(base_path, "published")
        if os.path.exists(published_dir):
            typ_files = [f for f in os.listdir(published_dir) if f.endswith('.typ')]
            if typ_files:
                typ_path = os.path.join(published_dir, typ_files[0])
                subprocess.run([sys.executable, struct_script, typ_path], check=True)
                # 3. Run Density Check
                subprocess.run([sys.executable, density_script, typ_path], check=True)
                
    except subprocess.CalledProcessError:
        print("❌ Lesson Plan Workflow Validation Failed.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python plan-validator.py <folder_name>")
        sys.exit(1)
    
    folder_name = sys.argv[1]
    run_workflow_validation(folder_name)
