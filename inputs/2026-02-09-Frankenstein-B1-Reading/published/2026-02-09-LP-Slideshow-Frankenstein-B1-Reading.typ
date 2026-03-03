#import "../../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "2026-02-10",
  cefr: "B1",
  duration: "60 Minutes",
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
  stage("ONE", "Context & Genre", "10", "To orient students to the Gothic/Sci-Fi genre and the author", [
    - *Title*: Show "FRANKENSTEIN". Elicit what they know (Monster? Green?).
    - *Mission*: Present "Your Mission" badges (Analyze, Profile, Sequence, Decode).
    - *Bridge*: Strategy for Genre (Look for "dark" or "science" words).
    - *Task 1 (Genre)*: Students choose TWO genres from list (Horror, Sci-Fi, Fairy Tale, etc.).
    - *Task 2 (Profile)*: Scan "About the Author" text for Mary Shelley facts (1816, Geneva).
    - *Feedback*: Review author facts and genre identification.
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Vocab & Prediction", "15", "To pre-teach keywords and remove barriers to the text", [
    - *Contextual Discovery*: Present 5 target words: *promising, how life begins, isolated, a storm, fear*.
    - T provides English context sentences derived from the story.
    - *Task 3 (Gap Fill)*: Ss complete sentences using the target words (S).
    - *Answer 3*: Review answers with definitions and model pronunciation (T-S).
    - *Prediction*: Ss guess Victor's secret based on the keywords.
  ], "T-Ss / Ss-Ss"),

  stage("THREE", "The Story (Gist)", "20", "To reconstruct the narrative arc", [
    - *Reading*: Students read the text chunks on pp. 144-145.
    - *Bridge*: Strategy for Ordering (Look for time markers: "First", "Then", "After two years").
    - *Task 5 (Sequence)*: Ss order events A-F (S).
    - *Feedback*: Review the correct sequence and discuss the mood of the story.
  ], "Ss / T-Ss"),

  stage("FOUR", "Deep Analysis", "15", "To analyze character flaws and themes", [
    - *Task 5 (Analysis)*: Questions about Victor's narrator voice and timing.
    - *Task 7 (Flaws)*: Ss use a checklist to identify Victor's flaws (Obsessive, Irresponsible).
    - *Task 8 (Themes)*: Ss identify core themes (Dangerous Knowledge).
    - *Final Discussion*: "Was Victor a bad person or just curious?" (T-S).
  ], "Ss-Ss / T-Ss"),
))