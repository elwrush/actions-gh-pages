#import "skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "28-01-2026",
  cefr: "B1+",
  duration: "90 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "Continuous Assessment",
  focus: "Reading & Vocabulary",
  materials: "Global Logistics & Relative Clauses",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will be better able to identify key information in a text about global supply chains and use non-defining relative clauses to add detail to descriptions.
]

#v(0.5cm)

#slideshow_link("https://elwrush.github.io/lesson-plan-agent/18-01-26_Global-Logistics-Relative-Clauses/")

#v(0.5cm)

#differentiation_box[
  This lesson utilizes a "Tiered Text" strategy. Fast finishers will be directed to the B2 level extension text, while students requiring more support will work with the simplified A2+ version of the same logistics report.
]

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in / SCR Situation", "10", "To activate schema and establish the logistics context.", [
    - Ss look at images of cargo ships and warehouses.
    - Discussion: What are the biggest challenges in shipping goods globally?
    - Introduce the "Situation": A major tech company needs to move 50,000 units from Shenzhen to London.
  ], "T-Ss / Ss-Ss"),
  
  stage("TWO", "Reading for Detail", "25", "To practice scanning for specific figures and names in a technical report.", [
    - Ss scan the text for "Task 1: Logistics Audit".
    - Peer-check answers regarding shipping times and costs.
    - Class feedback focusing on numerical accuracy.
  ], "Ss-Ss / T-Ss"),
))
