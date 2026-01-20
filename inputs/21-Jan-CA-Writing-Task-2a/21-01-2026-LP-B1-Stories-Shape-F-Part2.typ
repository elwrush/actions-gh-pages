#import "../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "21-01-2026",
  cefr: "B1",
  duration: "40 Minutes",
  shape: "F (Productive Skills - Writing)",
  assessment: "Continuous Assessment (CA)",
  focus: "Writing Task Completion",
  materials: "21-Jan-CA-Writing-Task-2a",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have written a ~100-word article about a story, answering all three prompt questions with appropriate paragraphing and engaging language.
]

#v(0.5cm)

#stage_table((
  stage(
    "ONE",
    "Lead-in & Plan Review",
    "5",
    "To reactivate the context and review plans.",
    [
      - Ss take out their plans from the previous lesson.
      - *Peer Swap Strategy*:
        - B1 Peers check: Story Name? Place? Books vs Films?
        - B2 Peers check: Character analysis? Plot depth? Is the comparison nuanced?
      - T asks: "Who has a title that makes me want to read?"
    ],
    "Ss-Ss / T-Ss",
  ),
  stage(
    "TWO",
    "Language & Strategy Focus: The Hook",
    "10",
    "To practice writing engaging opening sentences.",
    [
      - T reviews the 'Boring vs Engaging' opening concept.
      - *Differentiation*:
        - B1 Focus: Personal Question ("Do you like stories?").
        - B2 Focus: Setting the Scene ("It was a dark and stormy night when I first opened...") or Dramatic Statement ("Books are dead. Long live cinema.").
      - Ss write/refine their opening sentence.
    ],
    "T-Ss / S",
  ),
  stage(
    "THREE",
    "Checklist & Guidelines",
    "5",
    "To set expectations for the assessment.",
    [
      - T reminds Ss of the constraints:
        - B1: ~100 words.
        - B2: 140-190 words.
        - ALL: 3 Paragraphs minimum.
      - T writes start and end times on board (20 mins total).
    ],
    "T-Ss",
  ),
  stage(
    "FOUR",
    "Writing Task (CA)",
    "20",
    "To evaluate writing proficiency in a timed context.",
    [
      - Ss write their articles in silence.
      - T monitors ONLY to ensure task compliance (answering the question), not to correct language.
      - T ensures B2 students are writing enough depth to hit 140 words.
    ],
    "S (Exam conditions)",
  ),
))
