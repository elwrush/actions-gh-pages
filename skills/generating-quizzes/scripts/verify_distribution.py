import json
import argparse
import sys
import os

def verify_distribution(quiz_path, num_questions=None):
    if not os.path.exists(quiz_path):
        print(f"Error: Quiz file not found: {quiz_path}")
        return False
    
    try:
        with open(quiz_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON format: {e}")
        return False

    if "tasks" not in data:
        print("Error: No 'tasks' array found.")
        return False

    mcq_answers = []
    
    # Collect all MCQ answers
    for task in data["tasks"]:
        if task.get("task_type") in ["mcq", "vocab", "inference"]:
            for q in task.get("questions", []):
                if isinstance(q.get("answer"), int):
                    mcq_answers.append(q["answer"])

    # Check for correct distribution
    print(f"Collected answers: {mcq_answers}")
    
    if len(mcq_answers) < 4:
        print("Warning: Less than 4 questions found. Cannot fully validate balanced distribution.")
        return True # Soft pass for very short quizzes

    unique_answers = set(mcq_answers)
    required = {0, 1, 2, 3}
    missing = required - unique_answers
    
    if missing:
        print(f"Error: The following answer choices are completely missing: {missing}")
        return False
    
    print("Success: Answer distribution is balanced (at least one of each A, B, C, D).")
    return True

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Verify quiz answer distribution.")
    parser.add_argument("quiz_path", help="Path to quiz JSON.")
    args = parser.parse_args()
    
    if verify_distribution(args.quiz_path):
        sys.exit(0)
    else:
        sys.exit(1)