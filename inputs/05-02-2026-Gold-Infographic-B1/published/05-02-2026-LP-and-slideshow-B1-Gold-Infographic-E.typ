#import "../../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "05-02-2026",
  cefr: "B1",
  duration: "46 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "N/A",
  focus: "Reading",
  materials: "Oxford Discover Futures, Unit 10, pp104-105",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced the sub-skills of scanning for information and reading for specific detail in the context of an infographic about the science and history of gold.
]

#v(0.5cm)

#differentiation_box[
  Support is provided through pre-teaching high-frequency technical vocabulary (e.g., excavate, radiation) and using a "Speed Scan" phase to build confidence before the detailed data extraction task. Fast finishers are encouraged to categorize additional verb suffixes from the text.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/lesson-plan-agent/05-02-2026-Gold-Infographic-B1/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "5", "To engage Ss and activate schemata", [
    - *Golden Fact or Fiction*: Display three statements about gold on the screen (e.g., "Gold is edible," "All the gold ever mined fits in 3 swimming pools").
    - Ss discuss in pairs and vote 'Fact' or 'Fiction'.
    - Elicit a brief discussion: "Do you think gold is the most valuable thing on our planet? Why/why not?" (T-S interaction).
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Pre-teach Vocab", "8", "To remove barriers to the text", [
    - *Contextual Discovery*: Present 5 target words: *origin, excavate, manipulate, radiation, precious*.
    - T provides English context sentences (e.g., "Archaeologists had to *excavate* the site for months to find the tomb.")
    - Ss match words to definitions in pairs (S-S).
    - Model and drill pronunciation, highlighting word stress in *ex-ca-vate* and *ma-nip-u-late*. (T-S).
  ], "T-Ss / Ss-Ss"),

  stage("THREE", "Gist / Scanning", "7", "To practice scanning headings/images", [
    - *Speed Scan*: Set a 2-minute timer for Ex 1.
    - Ss look ONLY at images and headings to answer the 5 questions (S).
    - *Peer-Check*: Ss compare answers in pairs (S-S).
    - *Feedback*: Elicit answers and ask specific scanning strategy questions: "Which part of the infographic helped you find the answer to Q4 (underground)?" (T-S).
  ], "Ss / Ss-Ss"),

  stage("FOUR", "Main Task (Detail)", "12", "To practice reading for specific data/detail", [
    - *Data Detective*: Ss read the full text to match figures (e.g., 1.6 quadrillion tons) to their meaning (Ex 3).
    - Ss then answer the 4 comprehension questions in Ex 4 (S).
    - T monitors, providing support with keywords like "historical" or "dentistry".
    - *Detailed Feedback*: Discuss answers as a class, eliciting the reason why Cleopatra used gold. (T-S).
  ], "Ss / T-Ss"),

  stage("FIVE", "Vocabulary Focus", "8", "To discover verb suffixes", [
    - *Suffix Hunt*: Point to the "Discover Vocabulary" box.
    - Ss find the verb forms for words in Ex 5 within the text (e.g., beauty -> beautify).
    - Ss categorize the 4 suffixes identified in Ex 6 (-ify, -ize, -en, -ate) in pairs (S-S).
    - T clarifies how these suffixes transform nouns/adjectives into verbs. (T-S).
  ], "Ss-Ss / T-Ss"),

  stage("SIX", "Post-task", "6", "To personalize the topic", [
    - *Talking Points*: Ss discuss Ex 8 questions in small groups: "Is gold necessary for our lives?" and "What makes a resource valuable?" (S-S).
    - T circulates to capture "good language" and interesting ideas for the final wrap-up.
    - Brief content feedback to conclude the lesson. (T-S).
  ], "Ss-Ss"),
))
