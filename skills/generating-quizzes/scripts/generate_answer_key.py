import sys
import random
import json

def generate_key(num_questions):
    if num_questions < 4:
        print("Error: Number of questions must be at least 4 to ensure balanced distribution.")
        sys.exit(1)

    # Ensure at least one of each answer
    base_key = [0, 1, 2, 3]
    remaining_slots = num_questions - 4
    
    # Fill remaining slots randomly
    for _ in range(remaining_slots):
        base_key.append(random.randint(0, 3))
    
    # Shuffle until valid (no more than 2 consecutive identical answers)
    valid = False
    final_key = []
    
    attempts = 0
    while not valid and attempts < 1000:
        random.shuffle(base_key)
        valid = True
        for i in range(len(base_key) - 2):
            if base_key[i] == base_key[i+1] == base_key[i+2]:
                valid = False
                break
        attempts += 1
        final_key = base_key

    if not valid:
        # Fallback: simple round-robin if random shuffling fails
        final_key = [(i % 4) for i in range(num_questions)]
        random.shuffle(final_key) # Mild shuffle

    return final_key

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python generate_answer_key.py <num_questions>")
        sys.exit(1)
    
    try:
        num = int(sys.argv[1])
        key = generate_key(num)
        print(json.dumps(key))
    except ValueError:
        print("Error: Invalid number of questions.")
        sys.exit(1)