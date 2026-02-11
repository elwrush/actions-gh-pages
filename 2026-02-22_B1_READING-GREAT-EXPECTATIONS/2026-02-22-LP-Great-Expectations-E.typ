#import "../../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "22-02-2026",
  cefr: "B1",
  duration: "50 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "Formative / Peer Feedback",
  focus: "Reading",
  materials: "pp138-140 Oxford Discover Futures 2",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced scanning for biographical facts, reading for specific detail, and locating textual evidence in the context of Victorian literature.
]

#v(0.5cm)

#differentiation_box[
  Support is provided through visual scaffolding (Probe-First tables) and the sequential reveal of the editing task. High-flyers are challenged to find nuanced evidence for character motivation using the O-R-E framework.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/2026-02-22_B1_READING-GREAT-EXPECTATIONS/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "5", "Engage & Activate", [
    (T-Ss) **Fact or Fiction?**: Ss vote on 3 statements about Victorian prison ships ("hulks").
    (Pairs) Discussion on the atmospheric setting of the marshes.
    (T-Ss) **Mission Briefing**: Introduce the three goals: Meet Dickens, Understand Story, Discuss Themes.
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Pre-teach Vocab", "8", "Remove Barriers", [
    (T-Ss) **Contextual Discovery**: Use slides to present 5 key items:
    - *Churchyard*
    - *Gravestone*
    - *Marsh*
    - *Blacksmith*
    - *File*
    (Pairs) Ss match words to definitions/Thai translations based on visual context.
    (T-Ss) Drill: Focus on word stress.
  ], "T-Ss / Ss-Ss"),

  stage("THREE", "Gist / Scanning", "8", "Scanning Practice", [
    (Ss) **Task 1 (Scanning)**: 90s timer to find 3 author facts from Section 1.
    (Pairs) **Task 2 (Visual Prediction)**: Use Probe-First table to categorize man/boy details.
    (Pairs) **Task 3 (Matching)**: Guess associations from the scene image before reading.
  ], "Ss / Ss-Ss"),

  stage("FOUR", "Main Task (Detail)", "15", "Read for Detail", [
    (Ss) **Audio Experience**: Listen to theatrical audio while following the text.
    (Ss) **Task 4 (Recall/Reaction)**: Answer 5 questions.
    (T-Ss) Feedback: Elicit verbatim textual evidence for all answers.
  ], "Ss / T-Ss"),

  stage("FIVE", "Vocabulary Focus", "8", "Accuracy & Recycling", [
    (Pairs) **Task 5 (Editing)**: Identify 7 mistakes in the summary paragraph.
    (T-Ss) Interactive reveal using sequential `editing` layout.
  ], "Ss-Ss / T-Ss"),

  stage("SIX", "Post-task", "6", "Personalize & Evidence", [
    (Pairs) **Task 6 (Analysis)**: Decide on 5 Agree/Disagree statements with evidence.
    (Ss-Ss) Discussion: Explore themes using O-R-E (Opinion-Reason-Example).
  ], "Ss-Ss"),
))

#answer_key[
  *Task 1*: 1. Hard lives. 2. Memorable characters. 3. Boy to a man. \
  *Task 5 (7 errors)*: 1. morning->afternoon, 2. market->churchyard, 3. aunt->sister, 4. music->a gun, 5. evening->morning, 6. head->shoulder, 7. ill->angry. \
  *Task 6 (5 Qs)*: 1. Lonely (A), 2. Happy Home (D), 3. Young Man (A), 4. Truly Bad (D), 5. Enemies (A).
]
