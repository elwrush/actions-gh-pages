#import "../../skills/02-writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("intensive")

#metadata_table((
  teacher: "Ed Rush",
  date: "10-02-2026",
  cefr: "B1",
  duration: "45 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "N/A",
  focus: "Reading",
  materials: "Oxford Future Directions Workbook Reading Unit 3",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced the sub-skills of scanning for information and reading for specific detail in the context of a social media conversation about future foods.
]

#v(0.5cm)

#differentiation_box[
  Support is provided through pre-teaching high-frequency technical vocabulary (e.g., algae, molecules) and using a "Speed Scan" phase to build confidence before the detailed data extraction task. Fast finishers are encouraged to search for and describe other future foods not mentioned in the text.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/10-Feb-2026-Reading/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "5", "To engage Ss and activate schemata", [
    - *Part 1: Future Food Fact or Fiction*: Display three statements about future foods on the screen (e.g., "In the future, we will eat burgers made of bugs").
    - Ss discuss in pairs and vote 'Fact' or 'Fiction' (Ss-Ss).
    - *Part 2: Personal Hook*: Elicit a brief discussion: "What is the most unusual food you have tried or heard of?" 
    - 1 min. Content Feedback. (T-Ss).
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Pre-teach Vocab", "8", "To remove barriers to the text", [
    - *Part 1: Contextual Discovery*: Present 5 target words: *algae, unexceptional, crickets, molecules, extract*.
    - T provides English context sentences (e.g., "Scientists *extract* important materials from the earth.")
    - Ss match words to definitions/parts of speech in pairs (S-S).
    - *Part 2: Form & Pron*: Model and drill pronunciation, highlighting word stress in *un-ex-cep-tion-al* and *mol-e-cules*. 
    - 2 min. Feedback on form. (T-S).
  ], "T-Ss / Ss-Ss"),

  stage("THREE", "Gist / Scanning", "7", "To practice scanning for specific topics", [
    - *Part 1: Speed Scan*: Set a 2-minute timer for the text.
    - Ss scan the social media conversation to answer: "Which three future foods are discussed?" (algae, crickets, The Impossible Burger) (S).
    - *Part 2: Strategy Share*: Ss compare answers in pairs (S-S).
    - *Feedback*: Elicit answers and ask specific scanning strategy questions: "Which words or layout features helped you quickly spot the foods?" 1 min. Feedback. (T-S).
  ], "Ss / Ss-Ss"),

  stage("FOUR", "Main Task (Detail)", "15", "To practice reading for specific data/detail", [
    - *Part 1: Data Detective*: Ss read the full text to complete Exercise 2 (True/False and correct the false sentences) and Exercise 3 (Yes/No and find the evidence). (S).
    - T monitors, providing support with keywords and scanning techniques.
    - *Part 2: Evidence Check*: Ss compare evidence sentences in pairs.
    - *Detailed Feedback*: Discuss answers as a class. Explicitly elicit the sentence from the text that gave them the information. 3 min. Feedback. (T-S).
  ], "Ss / T-Ss"),

  stage("FIVE", "Vocabulary Focus", "5", "To figure out meaning from context", [
    - *Part 1: Context Clues*: Point to the "Reading strategy" box on page 24.
    - Ss complete Exercise 1, focusing on parts of speech, synonyms, antonyms, and prefixes. (S).
    - *Part 2: Discovery*: T clarifies how prefixes like *un-* (as in *unexceptional*) change meaning, and how surrounding sentences provide clues. 
    - 1 min. Feedback. (T-Ss).
  ], "Ss-Ss / T-Ss"),

  stage("SIX", "Post-task", "5", "To personalize the topic", [
    - *Part 1: Talking Points*: Ss discuss Exercise 4 questions in small groups: "Which of the three foods mentioned would you most like to eat? Why?" and "Which would you least like to eat?" (S-S).
    - *Part 2: The Future Menu*: T circulates to capture "good language" and interesting ideas.
    - 2 min. Final content feedback and wrap-up. (T-S).
  ], "Ss-Ss"),
))
