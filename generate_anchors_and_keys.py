
import random

# Randomized Answer Keys
b1_key = [random.randint(0, 3) for _ in range(6)]
b2_key = [random.randint(0, 3) for _ in range(8)]

print(f"B1 Answer Key (6 items): {b1_key}")
print(f"B2 Answer Key (8 items): {b2_key}")

# Anchors for B1 (Goal: 4.1/4.2 - Remembering, Understanding, Applying, Analyzing)
b1_anchors = [
    "Her father told her to sell them, but not one person has bought anything all day.",
    "She strikes a match, and suddenly it feels like she is sitting in front of a warm iron stove.",
    "She sees a beautiful table covered with a white cloth. There is a delicious roast goose on the table...",
    "One star falls, leaving a long line of fire. 'Someone is dying,' she whispers.",
    "She quickly lights all the matches in the box to keep her grandmother there.",
    "The next morning, the townspeople find the little girl frozen in the corner. She has a smile on her face..."
]

# Anchors for B2 (Goal: 4.3 - Evaluating, Creating)
b2_anchors = [
    "One slipper vanished into the snow, and the other was snatched up by a mischievous boy who joked that he would use it as a cradle...",
    "Fearing her father’s inevitable wrath should she return without a single penny, she dared not venture home.",
    "Seeking refuge from the debilitating cold, she huddled in a narrow corner between two tall houses.",
    "She reached out her feet to thaw them, but in that instant, the flame flickered and died.",
    "To her utter amazement, the goose leapt from its platter and waddled across the floor toward her.",
    "Her grandmother had always said that a falling star signaled a soul’s journey to the divine.",
    "In a desperate attempt to keep her grandmother’s presence near, she struck the entire remaining bundle of matches at once.",
    "None of them could have imagined the magnificent splendors she had witnessed..."
]

print("\n---B1 ANCHORS---")
for i, a in enumerate(b1_anchors):
    print(f"{i+1}. {a}")

print("\n---B2 ANCHORS---")
for i, a in enumerate(b2_anchors):
    print(f"{i+1}. {a}")
