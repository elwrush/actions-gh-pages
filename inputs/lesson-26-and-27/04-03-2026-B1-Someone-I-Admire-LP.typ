#import "/skills/02-writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "04-03-2026",
  cefr: "B1",
  duration: "45 Minutes",
  shape: "F (Productive Skills)",
  assessment: "Draft Completion",
  focus: "Writing",
  materials: "OFD3 Unit 4 Writing, WB p. 41",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will be better able to write a description of someone they admire, using attitude adverbs and supporting their opinions with specific facts and real-life examples.
]

#v(0.5cm)

#differentiation_box[
  During the drafting stage (Stage 4), supported learners will focus on using at least three attitude adverbs (e.g., *Amazingly, Clearly*) and two supporting facts. Advanced learners will be challenged to integrate complex sentence structures, such as relative clauses, to connect their opinions to the evidence provided in their 225-word draft.
]

#v(0.5cm)

#slideshow_link("https://elwrush.github.io/actions-gh-pages/lesson-26-and-27/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "6", "To engage students and activate schema regarding 'admirable' figures.", [
    - *The Adjective Match (**Task 4: Choice of Subject**):* T uses the slideshow to display images of a fictional character, a historical figure, and an athlete. 
    - Ss work in pairs to brainstorm two adjectives for each person (e.g., *brave, skilled, influential*). *T-Ss / Ss-Ss*
    - *Feedback:* T elicits adjectives to the board and asks: "Who is someone YOU admire? Why?" *Elicit*
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Preparation", "10", "To brainstorm and plan the content of the description.", [
    - *Planning (**Worksheet Task 1 / Workbook Task 4 & 5**):* Ss select their specific person to admire and make notes in their WB (**Task 5**) on why they admire them. *Indiv*
    - *Fact Mapping (**Worksheet Task 1 / Workbook Task 6**):* Ss identify at least two specific facts or achievements from the person's life that support their opinion. T monitors and provides target vocabulary for their subjects. *Indiv*
  ], "Indiv"),

  stage("THREE", "Preparation", "10", "To introduce the 'Supporting your opinion' strategy and 'Attitude Adverbs' focus.", [
    - *Strategy Focus (**Worksheet Header / Workbook Task 6**):* T presents the "**Writing Strategy: Supporting your opinion**." Ss discuss why facts and examples are better than just opinions. *T-Ss / Ss-Ss*
    - *Language Input (**Worksheet Task 2 / Workbook Task 7**):* T introduces six key attitude adverbs from the slideshow (*Amazingly, Surprisingly, Remarkably, Fortunately, Clearly, Generously*). *T-Ss*
    - *Mini-task:* Ss transform simple sentences into "attitude" sentences (e.g., "He won the race" -> "*Remarkably*, he won the race"). T checks meaning and models word stress (*re-MARK-ab-ly*). *Elicit / CCQ*
  ], "T-Ss / Indiv"),

  stage("FOUR", "Task", "19", "To produce the 225-word first draft using the models and language from Stages 2-3.", [
    - *Drafting (**Worksheet Task 3 / Workbook Task 8**):* Ss write their first draft of the description (approx. 225 words). T starts a 15-minute timer on the slideshow. *Indiv*
    - *Monitoring:* T circulates to check for the active inclusion of attitude adverbs (**Task 7**) and supporting facts (**Task 6**). *T-Ss*
    - *Wrap-up:* Ss read their "Closing Statement" aloud to a partner to check for a strong finish. *Ss-Ss*
  ], "Indiv / Ss-Ss"),
))
