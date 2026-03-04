#import "../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "26-01-2026",
  cefr: "B1/B2 (Differentiated)",
  duration: "46 Minutes",
  shape: "G (Task-Based Learning)",
  assessment: "n/a",
  focus: "Listening & Negotiation",
  materials: "BBC News Video (https://youtu.be/7vJxJyTWBmc), Annotated Transcript",
))

#v(0.5cm)

#main_aim_box[
  *Main Aim:* By the end of the lesson, learners will have completed a task about *negotiating diplomatic solutions* and will be better able to *express complex concerns* in the context of *the Thai-Cambodian border conflict* using content from the BBC News report.

  *Subsidiary Aim:* Learners will also have practiced and developed the sub-skills of *listening for gist and analyzing rhetorical tone* in the context of news broadcasting.
]

#v(0.5cm)

#differentiation_box[
  This lesson employs a "Tiered Task" strategy for B1 and B2 learners. 
  - *B1 (Scaffolded):* Focus on the "Human Impact" narrative. Their task is to identify three logistical needs for evacuees (food, shelter, school). 
  - *B2 (Analytical):* Focus on the "Diplomatic Friction." Their task is to analyze the language of blame used by both sides (*"provoking violence"*, *"target military site"*) and propose a formal mediation protocol. 
  Both levels utilize the same core BBC transcript but perform different roles during the Task Cycle.
]

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in: The Situation (Task 1)", "8", "To activate schema and introduce the conflict context.", [
    - *Situation:* Display images of the Preah Vihear Temple and the Thai-Cambodian border area.
    - *Discussion:* Ask Ss if they know about the history of this area. "What is the problem here?" Elicit basic facts (border, soldiers, temples).
    - *Pair work:* Ss look at a map and discuss why people might be "fleeing" (from the transcript title).
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Vocabulary: Power Words", "6", "To front-load key vocabulary before the listening task.", [
    - *Matching:* Ss match 5 key words from the report to their definitions (*mitigate, retaliate, ceasefire, evacuate, fractious*).
    - *Concept Checking:* Use the slides to check pronunciation and Thai equivalents.
  ], "Ss-Ss / T-Ss"),

  stage("THREE", "Task 2 & 3: Field Report & Analysis", "10", "To listen for gist and analyze specific detail to inform the tiered tasks.", [
    - *The Source:* Watch the BBC video (https://youtu.be/7vJxJyTWBmc).
    - *Gist (Task 2):* "Is the situation resolving or escalating?" Class feedback.
    - *Detail (Task 3):*
      - *B1:* Find three ways the conflict affects ordinary people.
      - *B2:* Identify the "language of accusation." Who said what?
  ], "T-Ss / Ss-Ss"),

  stage("FOUR", "Task 4: Resolution Negotiation", "15", "To collaboratively negotiate a resolution based on CEFR-appropriate goals.", [
    - *The Task:* Small groups act as "Conflict Response Teams."
    - *B1 Group Task:* Propose a 3-step "Humanitarian Aid Plan" for the evacuees.
    - *B2 Group Task:* Propose a 3-point "Asean Mediation Memo."
    - *Planning:* Groups brainstorm their points. T monitors, providing functional language.
  ], "Ss-Ss"),

  stage("FIVE", "Report & Feedback", "7", "To present resolution strategies and provide language correction.", [
    - *Report:* One student from each group presents their 3 steps.
    - *Comparison:* Class votes on the most realistic solution.
    - *Correction:* T addresses 2-3 common errors heard during the task cycle.
  ], "Ss-Class / T-Ss"),
))
