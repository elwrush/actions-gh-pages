#import "/skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "31-01-2026",
  cefr: "B1",
  duration: "46 Minutes",
  shape: "B (Language Practice)",
  assessment: "N/A",
  focus: "Vocabulary: At the Beach",
  materials: "b1-beach-vocab.pdf",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have had an opportunity to practice using coastal vocabulary and activity-related collocations and will be better able to describe their beach holiday experiences in the context of a 1-minute speaking mission.
]

#v(0.5cm)

#differentiation_box[
  - *Support*: Provide sentence stems for the speaking task (e.g., "I prefer to... because...").
  - *Challenge*: Ask stronger learners to include at least 3 collocations in their 1-minute speech.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/b1-beach-vocab/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "5", "To activate schema and introduce the lesson mission.", [
    - Show the **MISSION** slide (Slide 2).
    - Ask Ss: "What makes a perfect beach holiday?" Elicit a few ideas.
    - Highlight the 3 goals: Vocabulary, Grammar Accuracy, and Fluency.
    - Set the context: "Imagine you are an examiner listening to a student talk about their holiday."
  ], "T-Ss"),
  
  stage("TWO", "Language Clarification", "8", "To review coastal geography and word families.", [
    - Show **BUILDING BLOCKS** (Slide 4). Elicit the difference between 'coast', 'shore', and 'beach'.
    - *Task 1: Sun Words* (Slide 7-8).
    - Ask Ss to brainstorm words starting with "Sun".
    - Feedback: Elicit 'sunbathe' (verb), 'suntan' (noun), 'sunburn' (noun/verb).
    - *Concept Check*: "Is a suntan healthy?" (No). "What do you need to prevent sunburn?" (Sunscreen/block).
  ], "T-Ss"),

  stage("THREE", "Controlled Practice (Matching)", "8", "To practice common collocations.", [
    - Show **WORD PARTNERS** (Slide 10). Explain that 'rough' goes with 'sea', not 'sand'.
    - *Task 2: Matching* (Slide 11-12).
    - Ss match words in the left column (Sun, Wind, Seaside) to the right (Tan, Surfing, Resort).
    - Peer Check: Ask Ss to compare answers.
    - Feedback: Reveal answers on the slide. Drill pronunciation of 'Rough' /rʌf/ and 'Resort' /rɪˈzɔːt/.
  ], "Ss-Ss"),

  stage("FOUR", "Controlled Practice (Accuracy)", "10", "To distinguish between commonly confused words.", [
    - Show **PRECISION TRAINING** (Slide 15).
    - *Task 4: Word Choice* (Slide 16-17).
    - Ss choose the correct word in the sentences (e.g., "go for a stroll" vs "go for a shop").
    - Ask: "Why is 'shop' wrong here?" (You go 'shopping', not 'for a shop').
    - Focus on 'stroll' vs 'walk' (Stroll is relaxed).
  ], "Indiv -> Pairs"),

  stage("FIVE", "Semi-Controlled Practice", "5", "To practice vocabulary in context.", [
    - *Task 5: Completion* (Slide 18-20).
    - Ss complete the sentences with the words from previous tasks.
    - Elicit answers. Highlight the grammar: "Doctors recommend *that*..." or "Risk *of*...".
  ], "Indiv"),

  stage("SIX", "Freer Practice (Speaking)", "10", "To produce target language in a timed speaking task.", [
    - Show **SPEAKING FORMULA** (Slide 21). Explain O.R.E. (Opinion, Reason, Example).
    - *Task 6: Speaking Mission* (Slide 22).
    - Give Ss 2 minutes to prepare ONE question from their worksheet.
    - Put Ss in pairs. Student A speaks for 1 minute. Student B listens and checks: Did they use O.R.E? Did they use 3 vocab words?
    - Swap.
    - Feedback: Ask 2-3 students to report what their partner said.
  ], "Ss-Ss"),
))
