#import "../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "26-01-2026",
  cefr: "B1",
  duration: "46 Minutes",
  shape: "C (Test-Teach-Test)",
  assessment: "CA",
  focus: "Grammar (Sentence Boundaries)",
  materials: "26-01-2026-B1-Sentence-Boundaries-Grammar-Bell.pdf",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will be better able to identify and repair sentence boundary errors (Comma Splices, Fused Sentences, and Run-on Sentences) by analyzing their own feedback metadata and applying controlled practice rules to their previous writing drafts.
]

#v(0.5cm)

#differentiation_box[
  This lesson utilizes data-driven feedback (ERRANT analysis and Error Count Trajectories) to personalize the "Complication" stage of the lesson. Learners use their own mistake patterns as the diagnostic base before moving to controlled practice and final production/repair.
]

#v(0.5cm)

#stage_table((
  stage("ONE", "Feedback Insight (Diagnostic)", "10", "To analyze individual performance data.", [
    - **Step 1: Metric Review.** Show slides with Grade blocks, Feedback comments, and Progress charts.
    - Students locate their own data in their reports.
    - **Mistake Analysis:** Elicit the target error count (<= 3).
    - **Task 1 (Worksheet):** Students identify their personal "Repair Targets" based on their report.
  ], "T-Ss / Ss-Ss"),
  stage("TWO", "The Mechanics of Boundaries", "21", "To clarify and practice boundary rules.", [
    - **Hook:** Display "Elon Mask" sentence. Elicit the boundary problem.
    - **Lesson Task:** Explain that these are the most common mistakes across 5 classes.
    - **The Crime Scene (Task 2):** Analyze the mystery sentences from Aunna, Fergie, and Tata.
    - **The Heuristic:** "One because is okay. Two because is too much."
    - **Controlled Practice (Task 3):** Students complete the 7 repairs on the worksheet.
  ], "T-Ss / Ss-Ss"),
  stage("THREE", "The Final Level (Production)", "15", [To generalize skill to personal work.], [
    - **Mission:** Students return to their original writing tasks.
    - Using their practice from Task 3, they rewrite their problematic paragraphs, ensuring every "infinite" flow is broken by a gateway (Full stop + Capital).
    - **Peer Audit:** Students swap and check for specifically Comma Splices using a "Sentence Boundary" lens.
  ], "Ss-Ss"),
))
