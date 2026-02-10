#import "../../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "08-02-2026",
  cefr: "B1+",
  duration: "46 Minutes",
  shape: "H (SCR Receptive)",
  assessment: "Continuous Assessment",
  focus: "Reading & Speaking",
  materials: "08-02-2026-B1-The-Juniper-Tree.pdf",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will be better able to follow and analyze a complex narrative in the context of "The Juniper Tree", focusing on character motivations and symbolic retribution.
]

#v(0.5cm)

#differentiation_box[
  - *Support*: Provide a glossary for archaic terms ("pious", "seized"). Allow L1 for the initial "grim" concept check.
  - *Challenge*: Ask fast finishers to rewrite the ending from the stepmother's perspective.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/08-02-2026-The-Juniper-Tree-B1/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Warmer", "5", "To activate schema and interest", [
    - **Display**: Show the hero image of the kitchen scene (Stepmother/Father).
    - **Ask**: "What is happening here? Does it look like a happy story or a dark one? Why?"
    - **Elicit**: Predictions about the atmosphere using adjectives (e.g., *grim, foreboding, rustic*).
    - **Context**: Establish that this is a Brothers Grimm tale (1812), not a Disney version.
  ], "T-Ss"),
  
  stage("TWO", "Setup (The Wish)", "4", "To establish the narrative conflict", [
    - **Slide**: Show The Juniper Tree in winter (Blood on snow).
    - **Tell**: The opening narrative: The rich couple, the fatal wish ("red as blood, white as snow").
    - **CCQ**: "Did the mother survive the birth? (No). Was the wish successful? (Yes, but at a cost)."
    - **Introduce**: The Stepmother's arrival and her growing jealousy.
  ], "T-Ss"),

  stage("THREE", "Task 1: The Crime", "8", "To read for detail and motivation", [
    - **Read**: Students read **Paragraphs [4] to [7]** (The apple chest murder and the stew).
    - **Task**: Complete **Worksheet A. Multiple Choice Q1-3**.
    - **Monitor**: Ensure students identify the "accident" as a calculated murder plot.
    - **Feedback**: Elicit the motivation (greed/jealousy) vs. the lie told to the father.
  ], "Ss-Ss"),

  stage("FOUR", "Segue (Transformation)", "4", "To bridge the narrative gap", [
    - **Slide**: Show the bird rising from the mist/fire.
    - **Narrative Bridge**: Describe Marlinchen gathering the bones and the tree's magical response.
    - **Drill**: Pronunciation of target vocabulary: *pious* /pai.əs/ and *seized* /siːzd/.
    - **Explain**: The concept of 'Retribution' (getting what you deserve/karma).
  ], "T-Ss"),

  stage("FIVE", "Task 2: Retribution", "10", "To sequence events and analyze symbols", [
    - **Read**: Students read **Paragraphs [8] to [12]** (The bird's journey and judgment).
    - **Task**: Complete **Worksheet B. Chronological Order** (ordering the gifts).
    - **Task**: Complete **Worksheet C. Character Connections** (matching Gift to Receiver).
    - **Feedback**: Elicit *why* each character got that specific gift (Chain=Power, Shoes=Joy, Stone=Weight of Sin).
  ], "Ss-Ss"),

  stage("SIX", "Analysis (The Song)", "5", "To focus on recall and theme", [
    - **Task**: Complete **Worksheet D. Recall** (The bird's song lyrics).
    - **Ask**: "Why does the father hear a beautiful song while the stepmother hears a storm?"
    - **Elicit**: The contrast between Innocent Ignorance vs. Guilty Knowledge.
  ], "T-Ss"),

  stage("SEVEN", "Discussion (ORE)", "6", "To react personally to the themes", [
    - **Task**: Discuss **Worksheet Task 3**: "Is this story too dark for children today?"
    - **Monitor**: Check for use of the **ORE pattern**:
      - **Opinion**: "I think..."
      - **Reason**: "Because..."
      - **Example**: "Like when the millstone fell..."
  ], "Ss-Ss"),

  stage("EIGHT", "Feedback", "4", "To conclude and correct", [
    - **Content Feedback**: Share the most controversial opinions from the class.
    - **Correction**: Address errors in narrative tenses or vocabulary usage on the board.
    - **Final Thought**: "Does a story need a happy ending to be 'good'?"
  ], "T-Ss"),
))