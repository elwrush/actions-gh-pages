
text = """
On a bitterly cold New Year's Eve, a young girl wandered the frozen streets, barefoot and shivering. She was tasked with selling matches, but not a single soul had purchased a box all day. Fearing her father’s certain wrath if she returned empty-handed, she sought refuge in a narrow alleyway. To ward off the terminal chill, she struck a single match against the brick wall. 

In its fleeting glow, she experienced a series of wondrous visions: a warm iron stove, a succulent roast goose, and a magnificent Christmas tree. Each vision vanished as soon as the flame flickered out. When she glimpsed her late grandmother in the next spark, the girl frantically struck the remaining matches to sustain the apparition. 

The old woman, radiant and kind, took the girl into her arms. Together, they soared into a realm where cold, hunger, and fear were non-existent. The following morning, townspeople discovered the girl’s frozen body, a serene smile gracing her lips. While they pitied her tragic end, they remained oblivious to the beautiful splendors she had witnessed before her gentle departure from the mortal world.
"""

def count_words(text):
    return len(text.split())

print(f"Word Count: {count_words(text)}")
print("---TEXT START---")
print(text.strip())
print("---TEXT END---")
