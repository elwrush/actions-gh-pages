#import "../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "2026-02-10",
  cefr: "B1",
  duration: "46 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "N/A",
  focus: "Reading",
  materials: "Oxford Discover Futures 3, pp 144-145",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced the sub-skills of scanning for information and reading for specific detail in the context of the Gothic novel Frankenstein by Mary Shelley.
]

#v(0.5cm)

#differentiation_box[
  Support is provided through pre-teaching high-frequency literary and sci-fi vocabulary (e.g., promising, isolated) and using a "Strategy Bridge" for genre identification. Fast finishers are encouraged to identify Victor's character flaws and their consequences within the text.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/2026-02-09-Frankenstein-B1-Reading/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Context & Genre", "06", "To orient students to the Gothic/Sci-Fi genre and the author", [
    - *Interactive Hook*: Show "FRANKENSTEIN" with icons: 🕯️ (horror), 🧪 (science), 😢 (sadness). Ss elicit feelings/themes (Fear, Science, Tragedy) (T-Ss).
    - *Mission*: Present badges: Analyze Genres, Profile Author, Sequence Narrative, Decode Themes.
    - *Strategy Bridge*: Genre identification strategy (Look for "dark" or "science" keywords).
    - *Task 1 (Genre)*: Students identify the genres (Classic Horror / Early Science Fiction) based on [Intro Para 3] (Ss-Ss).
    - *Task 2 (Profile)*: Timed Scan (2 mins) of "About the Author" for Mary Shelley facts (Born: London, 1816: Geneva) (S).
    - *Feedback*: Verify facts and genre definitions from the text.
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Vocab & Prediction", "10", "To pre-teach keywords and remove barriers to the text", [
    - Contextual Discovery: Present 5 target words focused on the story and Victor's flaws:
        1. *mast* (Victor built a 150-meter metal **mast** above his laboratory to catch the lightning)
        2. *awful* (Victor looked at the creature's thin, yellow skin and saw an **awful** smile on its face)
        3. *irresponsible* (Victor was **irresponsible** because he forgot about his family and letters for two years)
        4. *obsessive* (Victor's work was **obsessive**; he worked every day and night without a single holiday)
        5. *reckless* (Instead of being careful, Victor's **reckless** use of electricity caused a huge disaster)
    - Task 3 (Gap Fill): Ss complete the vocabulary cloze (S).
    - Answer 3: Review answers and model pronunciation for keywords (T-Ss).
    - Prediction: Ss guess how Victor's "obsessive" work leads to an "awful" result.
  ], "T-Ss / S"),

  stage("THREE", "The Story (Gist)", "15", "To reconstruct the narrative arc", [
    - *Reading*: Ss read text chunks (Para 1-20) on pp. 144-145 (S).
    - *Strategy Bridge*: Strategy for Sequence (Look for time markers: "First", "Then", "After two years").
    - *Task 5 (Sequence)*: Speed Sequence of events A-F from p.146 (Ss-Ss).
    - *Feedback*: Verify correct order (Waldman -> Death -> Lab -> Machine -> Life -> Fear).
  ], "S / Ss-Ss"),

  stage("FOUR", "Deep Analysis", "15", "To analyze character flaws and themes", [
    - *Task 8 (Flaws)*: Ss identify Victor's flawed character traits (Irresponsible, Obsessive, Reckless) from p.147 (Ss-Ss).
    - *Task 9 (Themes)*: Ss identify central themes (Forbidden Knowledge / Morality) from p.147 (Ss-Ss).
    - *Final Discussion*: personal evaluation of Victor's choices and the Gothic mood.
  ], "Ss-Ss / T-Ss"),
))