
# Stage 1: Full Narrative Rewrite (Emotional Storytelling)

text_b1 = """
[1] The year was ending, and a freezing wind blew through the dark streets of the town. It was New Year's Eve. Snow fell gently on a poor little girl who walked alone in the cold. She carried matches in her hand to sell, but her day had been very difficult. She was barefoot because she had lost her mother's old slippers while crossing the street. One slipper had disappeared in the snow, and a rude boy had run away with the other.

[2] Her tiny feet were red and blue from the cold. She clutched her matchbox, but no one had bought anything from her all day. She was shivering and hungry, and she could smell the delicious roast goose cooking in the nearby houses. The lights from the windows danced in the snow, making her feel even more alone.

[3] She was afraid to go home. Her father would be angry because she had made no money, and besides, her house was almost as cold as the street. So, she sat down in a corner between two houses and pulled her feet under her. Her hands felt completely frozen. She thought, "Perhaps just one match could warm me." She struck it against the wall. *Scritch!* Suddenly, a bright flame appeared. It felt as if she were sitting in front of a large, beautiful iron stove. The fire was warm and wonderful, but just as she reached out her feet, the match went out. The stove vanished, and she was left in the cold again.

[4] She struck a second match. The light made the wall look like a thin curtain. Through it, she saw a grand room with a table covered in a white cloth. A roast goose, stuffed with apples, was waiting on the table. To her surprise, the goose jumped down and started towards her! But the match went out, and the vision was replaced by the cold, dark wall. 

[5] With the third match, she found herself under a magnificent Christmas tree. Thousands of candles sparkled on the branches. As she reached for them, the match went out and the lights rose higher, turning into stars. One star fell, leaving a trail of fire. "Someone is dying," she whispered. Her old grandmother had told her that a falling star meant a soul was going to heaven.

[6] She struck another match, and there stood her grandmother, looking kind and bright. "Grandmother!" she cried. "Take me with you!" She quickly lit the rest of her matches to keep the vision alive. They burned brighter than the day. Her grandmother took the little girl in her arms, and they both flew high into the sky, far away from the cold and the hunger. 

[7] The next morning, the townspeople found the little girl. She was sitting in the corner with a peaceful smile on her face, but she had frozen to death. "She was trying to keep warm," they said. No one knew the beautiful things she had seen, or the joy she felt as she entered the New Year with her grandmother.
"""

text_b2 = """
[1] A bitter cold gripped the city on the final night of the year. It was New Year's Eve, and thick snow blanketed the cobblestone streets. In the deepening gloom, a young girl wandered aimlessly, her tattered clothes providing no protection against the winter wind. She was barefoot, having lost her oversized slippers while dodging a carriage earlier that evening. One had vanished beneath the snow, while a mischievous boy had snatched the other, mocking her as he disappeared into the shadows.

[2] The girl trudged onward, her feet numbed into shades of raw red and deep blue. She clutched a bundle of matches, but it had been a disastrous day of trade; not a single soul had spared a coin. Hunger gnawed at her stomach, and the savory scent of roast goose wafted from the glowing windows of the town’s comfortable homes. To her, the celebration felt like a distant world, separated by a wall of glass and indifference.

[3] Fearing her father's inevitable anger should she return empty-handed, she dared not go home. Besides, her own dwelling offered little sanctuary, as the wind whistled through the gaps in the roof. Seeking refuge, she huddled in a narrow alleyway between two brick buildings. Her fingers were stiff with frost, and in her desperation, she decided to strike a single match for a moment’s warmth. *Scritch!* The match flared into a tiny, brilliant candle. In its magical glow, she felt transported. She was no longer in the snow but seated before a magnificent iron stove. The fire inside roared with a comforting, life-giving heat. But just as she stretched out her frozen feet, the match flickered and died. The stove vanished, leaving her alone in the darkness.

[4] Determined to find that warmth again, she struck a second match. As the light expanded, the brick wall seemed to dissolve into a transparent veil. She found herself peering into a grand dining room where a feast was laid out upon a snowy-white cloth. A succulent roast goose, stuffed with fragrant apples, steamed at the center of the table. To her astonishment, the goose leapt from its platter and waddled across the floor with a knife and fork in its breast. Yet, before it could reach her, the match extinguished, and the cold reality of the alleyway returned.

[5] With the third match, she was standing beneath the most spectacular Christmas tree she had ever seen. Thousands of candles sparkled upon its green branches, and colorful ornaments beckoned to her. As she reached upward, the match went out. The lights ascended until they transformed into the brilliant stars of the winter sky. One star streaked across the heavens, leaving a fiery trail. "Someone is passing away," she thought, remembering her late grandmother—the only person who had ever treated her with genuine compassion. Her grandmother had always said that a falling star signaled a soul’s journey to the divine.

[6] Frantically, she struck another match. In the sudden radiance, her grandmother stood before her, bathed in celestial light, looking serene and incredibly kind. "Grandmother!" the girl pleaded. "Oh, please take me with you! I know you will vanish just like the stove and the great Christmas tree." To keep her grandmother near, she struck the entire bundle of matches at once. The light became brighter than midday. Her grandmother reached out, took the girl into her arms, and together they soared through joy, far above the earth, to a place where there was no cold, no hunger, and no fear.

[7] At dawn, the townspeople discovered the small figure huddled in the corner, a peaceful smile frozen on her lips. She had passed away during the night, surrounded by the charred remains of her matches. "She was only trying to keep herself warm," the people remarked solemnly. None of them could have imagined the magnificent splendors she had witnessed, or the radiant glory in which she had entered the New Year.
"""

def count_words(text):
    return len(text.split())

print(f"B1 Word Count: {count_words(text_b1)}")
print(f"B2 Word Count: {count_words(text_b2)}")

with open('little_match_girl_b1.txt', 'w', encoding='utf-8') as f:
    f.write(text_b1.strip())

with open('little_match_girl_b2.txt', 'w', encoding='utf-8') as f:
    f.write(text_b2.strip())
