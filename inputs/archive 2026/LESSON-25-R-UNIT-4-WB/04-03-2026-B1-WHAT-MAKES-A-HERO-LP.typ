#import "../../skills/02-writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "04-03-2026",
  cefr: "B1",
  duration: "45 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "Controlled & Semi-controlled Reading Tasks",
  focus: "Fact vs. Opinion & Unsung Heroes",
  materials: "Workbook Unit 4 (pp. 34-35)",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced identifying facts and opinions in the context of an article about unsung heroes.
]

#v(0.5cm)

#differentiation_box[
  Students will work in mixed-ability pairs for the initial schema activation and vocabulary matching tasks. For the detailed reading (Fact vs. Opinion), higher-level students will be challenged to find their own examples of facts and opinions within the text, while lower-level students focus on the pre-selected highlighted sentences.
]

#slideshow_link("https://elwrush.github.io/actions-gh-pages/lesson-25-r-unit-4-wb/")

#v(0.5cm)

#stage_table((
  stage("1", "Lead-in", "5", "To activate schemata and elicit concept of unsung heroes.", [
    - *Part 1: Hero Quiz*: T shows images of 3 people (Athlete, Volunteer, Scientist). Ss vote: "Is this a hero?" (T-Ss / Voting).
    - *Part 2: Defining Unsung*: T elicits the difference between a "hero" and an "unsung hero." (Elicit / T-Ss).
  ], "Ss-Ss"),

  stage("2", "Pre-teach Vocab", "8", "To remove lexical barriers and focus on word stress.", [
    - *Part 1: Context Matching*: Ss match 5 key words (*recognition*, *determination*, *expedition*, *courageous*, *achievement*) to contextual sentences on the slides. (Ss-Ss).
    - *Part 2: Pronunciation*: T models and drills word stress (e.g., de-ter-mi-*NA*-tion, ac-*CIEVE*-ment). (Drill / T-Ss).
  ], "Ss-Ss"),

  stage("3", "Gist / Scanning", "7", "To practice scanning sub-skills using headings.", [
    - *Part 1: Speed Scan*: Timed 2-minute scan. Ss match names (Junko, Svetlana, Scott) to their respective fields (Mountain, Space, Internet). (Timed / Solo).
    - *Part 2: Feedback*: T asks "How did you find the names so quickly?" (Strategy Check: Headings). (Elicit / T-Ss).
  ], "S / T-Ss"),

  stage("4", "Main Task (Detail)", "15", "To practice identifying fact vs. opinion.", [
    - *Part 1: Fact vs. Opinion*: Ss identify F or O for the 8 highlighted sentences in the text (WB Ex. 2). (Solo).
    - *Part 2: Evidence Check*: Ss complete WB Ex. 4 (True/False) with evidence from the text. (Pairs).
    - *Part 3: Feedback*: Whole class feedback. (T-Ss).
  ], "S / Ss-Ss"),

  stage("5", "Post-task", "10", "To recycle language and personalize the topic.", [
    - *Part 1: Word Building*: Ss find noun forms of *courageous*, *achieve*, *lead*, *determine* in the text. (Solo).
    - *Part 2: My Hero*: Pairs discuss: "Who is an unsung hero in your life? What makes them heroic?" (Ss-Ss).
  ], "Ss-Ss"),
))

#answer_key[
  *Vocab:* 1. recognition, 2. determination, 3. expedition, 4. courageous, 5. achievement \
  *Ex. 2:* (Fact/Opinion sentences 1-8 based on WB keys) \
  *Ex. 4:* 1. F, 2. F, 3. T, 4. T, 5. T, 6. T, 7. T, 8. F, 9. T, 10. T
]
