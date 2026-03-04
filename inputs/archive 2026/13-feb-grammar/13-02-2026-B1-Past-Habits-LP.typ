#import "../../skills/02-writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("intensive")

#metadata_table((
  teacher: "Ed Rush",
  date: "13-02-2026",
  cefr: "B1",
  duration: "45 Minutes",
  shape: "C (Test-Teach-Test)",
  assessment: "CA",
  focus: "Grammar (used to vs would)",
  materials: "Oxford Discover Futures 3 Workbook Chapter 1",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will be better able to describe past habits and states using #strong[used to] and #strong[would] accurately in spoken and written contexts.
]

#v(0.5cm)

#differentiation_box[
  This lesson allows for varying degrees of challenge during the practice stage. Stronger students can incorporate "be used to / get used to" for extra complexity, while others can focus purely on differentiating between "used to" (states) and "would" (actions).
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/13-feb-grammar/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "5", "To engage Ss and activate schemata about past habits.", [
    - #strong[Hook:] T writes "When I was 10, I..." on the board.
    - T gives a personal example (e.g., "I used to play hide and seek").
    - #strong[Elicit:] Ss brainstorm 3 things they did as children that they don't do now.
    - #strong[Interaction:] Ss discuss in pairs.
  ], "T-Ss / Ss-Ss"),
  stage("TWO", "Test 1", "10", "To test prior knowledge of past habits using 'used to' and 'would'.", [
    - #strong[Task Setup:] Ss open Workbook to Page 7.
    - Ss complete #strong[Exercise 5] (Complete the dialogue with the correct form of used to) and #strong[Exercise 7] (Replace used to with would where possible).
    - #strong[Monitoring:] T monitors to identify common errors and see if Ss naturally understand when "would" cannot be used (e.g., with state verbs).
    - Ss check answers in pairs.
  ], "Indiv / Ss-Ss"),
  stage("THREE", "Teach", "10", "To clarify meaning, form, and pronunciation of target language.", [
    - #strong[Feedback:] T reviews answers on the board for Ex 5 & 7.
    - #strong[Meaning (CCQ):] "Do we still do these things now?" (No). "Can we use 'would' for living somewhere?" (No, only for actions).
    - #strong[Form:] Clarify that #emph[used to] works for BOTH states and habits. #emph[Would] works ONLY for repeated actions/habits in the past. 
    - #strong[Pronunciation:] Model and drill the pronunciation of "used to" /juːst tʊ/ (not "yooz-d"). Chorally and individually.
  ], "T-Ss"),
  stage("FOUR", "Test 2", "10", "To test understanding of the clarified rules.", [
    - #strong[Controlled Practice:] Ss complete #strong[Exercise 8] (Complete sentences with used to / didn't use to or would / wouldn't. Note: both forms are possible for some).
    - #strong[Peer Check:] Ss swap papers and check answers.
    - #strong[Feedback:] T monitors and corrects common errors on the board, specifically emphasizing the constraint of "would".
  ], "Indiv / Ss-Ss"),
  stage("FIVE", "Practice", "10", "To provide freer practice.", [
    - #strong[Personalization:] Ss think of a major change in their life (like starting a new school, referencing Ex 12).
    - #strong[Writing Task:] Ss write 3 sentences about their past habits vs now, using both 'used to' and 'would'.
    - #strong[Speaking Task:] Ss share their sentences with their group.
    - T monitors for correct usage and provides delayed feedback on any persistent errors.
  ], "Indiv / Ss-Ss"),
))
