# Visual Plan: Frankenstein (B1 Reading)

> **VISUAL GATE**: This plan defines the layouts and assets for every slide.

## Assets
- **Video 1**: `../images/horror_house_7s.mp4` (Title/Theme)
- **Video 2**: `../images/mission_bg_clipped.mp4` (Mission)
- **Video 3**: `../images/gold_bg.mp4` (Segues) - do not use video for segues, plain backgounds re fine
- **Image 1**: `images/page-144.jpg` (Mary Shelley / Text)
- **Image 2**: `images/page-145.jpg` (Lab scene)
- **Image 3**: `images/page-146.jpg` (Visual Analysis)

## Slide Breakdown

### Phase 1: Context & Genre
1.  **Title Slide**: `layout: title`
    *   Title: FRANKENSTEIN
    *   Subtitle: B1 Reading
    *   Video: `horror_house_7s.mp4` (Loop: true, Opacity: 0.6)

2.  **Mission Slide**: `layout: mission`
    *   Title: YOUR MISSION
    *   Video: `mission_bg_clipped.mp4`
    *   Objectives: ANALYZE genre, PROFILE author, SEQUENCE events, DECODE flaws.

3.  **Segue 1**: `layout: segue`
    *   Title: PHASE 1: CONTEXT
    *   Subtitle: Get ready to analyze the creator and his creation.
    *   give me an image prompt for Frankenstein 

4.  **Strategy (Genre)**: `layout: strategy`
    *   Title: TASK 1: GENRE
    *   Table content: What (Identify genre) / Why (Set expectations) / Tips (Look for Gothic elements).

5.  **Task 1 (Genre)**: `layout: quiz` (Auto-Animate)
    *   Question: What is the genre?
    *   Options: Classic Horror, Science Fiction, Fairy Tale, Detective, Comedy, Crime.
    *   Instruction: Choose TWO.
    *   **Timer**: 2 minutes (with RESET).

6.  **Answer 1**: `layout: answer_detail`
    *   Question: The Genre
    *   Answer: Early Science Fiction / Classic Horror
    *   Evidence: "Written in 1818... scientific speculation."
    *   Explanation: It combines the fear of the unknown with the power of science.

7.  **Strategy (Profile)**: `layout: strategy`
    *   Title: TASK 2: AUTHOR PROFILE
    *   Table content: What (Find facts) / Why (Understand context) / Tips (Scan for WHO/WHERE/WHEN/HOW).

8.  **Task 2 (Profile)**: `layout: split_table`
    *   Title: MARY SHELLEY
    *   Image: provide an image prompt and I will generate a pic for you
    *   Table: Find WHO, WHERE, WHEN, and HOW.
    *   **Timer**: 3 minutes (with RESET).

9.  **Answer 2**: `layout: answer_detail`
    *   Question: Author Profile
    *   Answer: Mary Shelley (1797-1851)
    *   Evidence: "Summer of 1816... ghost story challenge."
    *   Explanation: The idea came from a nightmare during a stormy night in Geneva.

### Phase 2: Vocabulary & Prediction
10. **Segue 2**: `layout: segue`
    *   Title: PHASE 2: VOCABULARY
    *   Subtitle: Get ready to guess meaning from context.
    *   DO NOT USE videos for segue slides

11. **Strategy (Vocab)**: `layout: strategy` You should be using vocabulary slides which present images with phonemes, context sentences and backgound imahes
    *   Title: TASK 3: GUESS THE WORDS
    *   Table content: What (Complete sentences) / Why (Build vocabulary) / Tips (Use context clues).

12. **Task 3a (Vocab)**: `layout: cloze` (Auto-Animate)
    *   Title: COMPLETE (1/2)
    *   Sentences 1-3: Promising student, life begins, isolated.
    *   **Timer**: 4 minutes (with RESET).

13. **Task 3b (Vocab)**: `layout: cloze` (Auto-Animate)
    *   Title: COMPLETE (2/2)
    *   Sentences 4-5: Power of a storm, feeling of fear.

14. **Answer 3**: `layout: answer_detail`
    *   Question: Vocabulary Check
    *   Answer: 1. Promising, 2. How life begins, 3. Isolated, 4. A storm, 5. Fear.
    *   Explanation: These words describe Victor's journey from student to creator.

### Phase 3: The Story Sequence
15. **Segue 3**: `layout: segue`
    *   Title: PHASE 3: THE STORY
    *   Subtitle: Get ready to reconstruct the narrative.
    *   Video: `gold_bg.mp4`

16. **Strategy (Ordering)**: `layout: strategy`
    *   Title: TASK 4: ORDER EVENTS
    *   Table content: What (Sequence A-F) / Why (Track narrative arc) / Tips (Look for time markers).

17. **Task 4a (Order)**: `layout: ranking` (Auto-Animate)
    *   Title: SEQUENCE (1/2)
    *   Items A-C: Machine, Laboratory, Fear.
    *   **Timer**: 5 minutes (with RESET).

18. **Task 4b (Order)**: `layout: ranking` (Auto-Animate)
    *   Title: SEQUENCE (2/2)
    *   Items D-F: Death/Secret, Waldman, Electricity.

19. **Answer 4**: `layout: answer_detail`
    *   Question: Correct Order
    *   Answer: 1.E, 2.A, 3.D, 4.B, 5.F, 6.C.
    *   Explanation: Victor meets his mentor, builds his lab, discovers the secret, and finally creates the monster.

### Phase 4: Deep Analysis
20. **Segue 4**: `layout: segue`
    *   Title: PHASE 4: ANALYSIS
    *   Subtitle: Get ready to think deeper about characters and themes.
    *   Video: `gold_bg.mp4`

21. **Strategy (Analysis)**: `layout: strategy`
    *   Title: TASK 5: NARRATOR & TIME
    *   Table content: What (Identify voice/date) / Why (Perspective) / Tips (Identify WHO is speaking).

22. **Task 5 (Analysis)**: `layout: split_table`
    *   Title: ANALYSIS QUESTIONS
    *   Image: `images/page-146.jpg`
    *   Questions: Who is the narrator? When is it told? Indications?
    *   **Timer**: 3 minutes (with RESET).

23. **Answer 5**: `layout: answer_detail`
    *   Question: Analysis
    *   Answer: Victor Frankenstein (Narrator) / Later date (Looking back).
    *   Evidence: Victor's voice reveals the tragedy after the fact.

24. **Strategy (Flaws)**: `layout: strategy`
    *   Title: TASK 7: CHARACTER FLAWS
    *   Table content: What (Select flaws) / Why (Character study) / Tips (Bad personality traits).

25. **Task 7 (Flaws)**: `layout: checklist` (Auto-Animate)
    *   Title: VICTOR'S FLAWS
    *   Options: Arrogant, Obsessive, Reckless, Irresponsible.
    *   **Timer**: 2 minutes (with RESET).

26. **Answer 7**: `layout: answer_detail`
    *   Question: Character Flaws
    *   Answer: Obsessive, Irresponsible, Reckless.
    *   Explanation: His obsession with science makes him reckless and irresponsible for his creation.

27. **Strategy (Themes)**: `layout: strategy`
    *   Title: TASK 8: CENTRAL THEMES
    *   Table content: What (Identify themes) / Why (Main idea) / Tips (The moral of the story).

28. **Task 8 (Themes)**: `layout: checklist` (Auto-Animate)
    *   Title: THEMES
    *   Options: Dangerous Knowledge, Morals/Right vs Wrong.
    *   **Timer**: 2 minutes (with RESET).

29. **Answer 8**: `layout: answer_detail`
    *   Question: Key Themes
    *   Answer: Dangerous Knowledge & Morality.
    *   Explanation: The story warns us about the dangers of playing God without a conscience.
