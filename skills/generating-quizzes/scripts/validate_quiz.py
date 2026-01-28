import json
import argparse
import sys
import os

VALID_TYPES = [
    "antecedent", "mcq", "boolean", "vocab", "inference", 
    "short_answer", "gapfill", "matching", 
    "error_correction", "reordering", "faq", "paraphrase"
]

BLOOM_LEVELS = ["Remembering", "Understanding", "Applying", "Analyzing", "Evaluating", "Creating"]

def validate_quiz(file_path):
    if not os.path.exists(file_path):
        print(f"Error: File not found: {file_path}")
        return False

    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}")
        return False

    if "tasks" not in data or not isinstance(data["tasks"], list):
        print("Error: Root object must contain a 'tasks' array.")
        return False

    success = True
    for t_idx, task in enumerate(data["tasks"]):
        t_prefix = f"Task {t_idx+1}: "
        
        # Validate Task Meta
        if "task_type" not in task or task["task_type"] not in VALID_TYPES:
            print(f"{t_prefix}Invalid or missing 'task_type'. Must be one of {VALID_TYPES}")
            success = False
            continue

        if "instructions" not in task:
            print(f"{t_prefix}Missing 'instructions'.")
            success = False

        if "questions" not in task or not isinstance(task["questions"], list):
            print(f"{t_prefix}Missing or invalid 'questions' array.")
            success = False
            continue

        # Validate Questions
        for q_idx, q in enumerate(task["questions"]):
            q_prefix = f"{t_prefix}Question {q_idx+1} ({task['task_type']}): "
            
            # Universal keys
            if "query" not in q:
                print(f"{q_prefix}Missing 'query'.")
                success = False
            if "answer" not in q:
                print(f"{q_prefix}Missing 'answer'.")
                success = False
            if "explanation" not in q:
                print(f"{q_prefix}Missing 'explanation'.")
                success = False
            if "bloom_level" not in q or q["bloom_level"] not in BLOOM_LEVELS:
                print(f"{q_prefix}Missing or invalid 'bloom_level'. Must be one of {BLOOM_LEVELS}")
                success = False
            if "anchor_text" not in q:
                print(f"{q_prefix}Missing 'anchor_text'.")
                success = False

            # Type-specific validation
            t_type = task["task_type"]
            
            if t_type in ["mcq", "vocab", "inference"]:
                if "choices" not in q or not isinstance(q["choices"], list) or len(q["choices"]) != 4:
                    print(f"{q_prefix}Must have exactly 4 'choices'.")
                    success = False
                if not isinstance(q.get("answer"), int) or not (0 <= q.get("answer", -1) <= 3):
                    print(f"{q_prefix}'answer' must be integer 0-3.")
                    success = False

            elif t_type == "boolean":
                if "choices" not in q or not isinstance(q["choices"], list) or len(q["choices"]) != 2:
                    print(f"{q_prefix}Must have exactly 2 'choices' (True/False).")
                    success = False
                if not isinstance(q.get("answer"), int) or not (0 <= q.get("answer", -1) <= 1):
                    print(f"{q_prefix}'answer' must be integer 0 or 1.")
                    success = False

            elif t_type == "antecedent":
                if "target_text" not in q:
                    print(f"{q_prefix}Missing 'target_text' (the pronoun/proform).")
                    success = False

            elif t_type == "matching":
                if "pairs" not in q or not isinstance(q["pairs"], list):
                    print(f"{q_prefix}Missing or invalid 'pairs' array.")
                    success = False

            elif t_type == "error_correction":
                if "target_text" not in q:
                    print(f"{q_prefix}Missing 'target_text' (the error).")
                    success = False

            elif t_type == "reordering":
                if not isinstance(q.get("answer"), list):
                    print(f"{q_prefix}'answer' must be a list of indices.")
                    success = False

    if success:
        print(f"Success: {file_path} passed universal validation.")
    else:
        print(f"Validation failed for {file_path}.")
    
    return success

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Validate Universal Quiz JSON format.")
    parser.add_argument("file_path", help="Path to the JSON file to validate.")
    args = parser.parse_args()

    if validate_quiz(args.file_path):
        sys.exit(0)
    else:
        sys.exit(1)
