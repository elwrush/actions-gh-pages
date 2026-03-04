#import "../../skills/02-writing-lesson-plans/templates/lesson-plan-components.typ": *
#import "/lib/typst/lib.typ": intensive_header

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#intensive_header()

#metadata_table((
  teacher: "Ed Rush",
  date: "04-03-2026",
  cefr: "B1",
  duration: "45 Minutes",
  shape: "C (Test-Teach-Test)",
  assessment: "CA",
  focus: "Relative Clauses & Emergency Vocab",
  materials: "Oxford Discover Futures 3 Workbook Unit 4 (p. 37-38)",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will be better able to identify and use #strong[defining] and #strong[non-defining relative clauses] accurately to describe people, places, and events in the context of heroes and emergencies.
]

#v(0.5cm)

#differentiation_box[
  Stronger students can focus on the nuance of #strong[omitting pronouns] in object clauses (Task 8), while others can focus on the primary distinction between defining and non-defining clauses (Task 7).
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/04-03-2026-b1-lesson-23-grammar/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "5", "To engage Ss and activate schemata about heroes.", [
    - #strong[Hook:] "Hero or Not?" T presents 3 scenarios.
    - Ss vote using icons/gestures.
    - #strong[Elicit:] "What makes someone a hero?"
    - #strong[Interaction:] T-Ss / Ss-Ss.
  ], "T-Ss / Ss-Ss"),
  stage("TWO", "Test 1", "10", "To test prior knowledge of relative pronouns and emergency vocab.", [
    - #strong[Vocab Task:] Ss match emergency phrases to definitions (Task 10).
    - #strong[Grammar Task:] Ss read the Nasreddin Hodja story and choose the correct relative pronouns (Task 5).
    - #strong[Monitoring:] T checks for confusion between 'who', 'which', 'where', and 'when'.
  ], "Indiv / Ss-Ss"),
  stage("THREE", "Teach", "10", "To clarify the rules of relative clauses and pronoun omission.", [
    - #strong[Feedback:] Review Task 5 and Task 10 answers.
    - #strong[Meaning:] Clarify the difference between #emph[Defining] (essential info) and #emph[Non-defining] (extra info with commas).
    - #strong[Form:] Use Task 7 examples (Rosa Parks, Marie Curie) to show comma placement.
    - #strong[Omission Rule:] Introduce the object vs. subject rule using Task 8.
  ], "T-Ss"),
  stage("FOUR", "Test 2", "10", "To provide controlled practice with non-defining clauses.", [
    - #strong[Task 7:] Ss combine sentences using non-defining clauses and pronouns in parentheses.
    - #strong[Task 11:] Ss complete the 'Heroic Friend' story using emergency vocabulary in context.
    - #strong[Peer Check:] Ss swap and check. T provides whole-class feedback.
  ], "Indiv / Ss-Ss"),
  stage("FIVE", "Production", "10", "To provide freer practice and personalization.", [
    - #strong[Riddle Task:] Ss write their own "Guess the Hero" riddle (Task 6 variation) using at least 3 relative clauses.
    - #strong[Speaking:] Ss share riddles in groups.
    - #strong[Discussion:] "Different ways to be a hero" (Task 12).
    - T provides delayed feedback on language usage.
  ], "Indiv / Ss-Ss"),
))
