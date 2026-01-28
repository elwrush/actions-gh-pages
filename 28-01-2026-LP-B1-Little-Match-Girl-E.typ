#import "skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "28-01-2026",
  cefr: "B1",
  duration: "46 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "n/a",
  focus: "Reading",
  materials: "match_girl_worksheet.typ",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced and developed the sub-skills of reading for detail and identifying implicit meaning in the context of Hans Christian Andersen's 'The Little Match Girl', while reflecting on the theme of social inequality.
]

#v(0.5cm)

#differentiation_box[
  This lesson provides a tiered approach to the narrative. While the class focus is on the B1 text, B2 learners have access to a more linguistically complex version of the story and higher-level philosophical prompts. This allows for personalized "i+1" challenge levels within a shared thematic context.
]

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in: Modern Poverty", "8", "To activate schema and establish thematic relevance.", [
    - *Situation:* Display the YouTube video ("Terrible State of American Inner Cities") showing tent cities and modern homelessness.
    - *Task:* In pairs, Ss discuss two questions: 
      1. What are the biggest challenges these people face? 
      2. Why does this happen in wealthy countries?
    - *Feedback:* Brief class discussion to establish the "Complication" of systemic poverty.
  ], "T-Ss / Ss-Ss"),
  
  stage("TWO", "Pre-teach Vocabulary", "7", "To remove lexical barriers to the B1 text.", [
    - *Vocab Input:* Introduce 5 items with clear contextual indicators:
      1. *Barefoot:* "He forgot his shoes at the beach, so he had to walk **barefoot** on the hot sand." (เท้าเปล่า)
      2. *Shivering:* "The boy was **shivering** because he was standing in the cold rain without a coat." (ตัวสั่น)
      3. *Vanished:* "The magician waved his hand and the rabbit **vanished**; it was completely gone!" (อันตรธาน)
      4. *Magnificent:* "The king lived in a **magnificent** palace with golden walls and hundreds of rooms." (งดงามตระการตา)
      5. *Soul:* "Many people believe that when the body dies, the **soul** continues to live forever." (วิญญาณ)
    - *CCQs:* Ask: "If I am barefoot, am I wearing socks?" (No). "If a rabbit vanishes, can I see it?" (No).
  ], "T-Ss"),

  stage("THREE", "Reading for Detail", "22", "To practice scanning and detailed comprehension of a narrative.", [
    - *Procedure:* Ss read "The Little Match Girl" (Part 1: B1 Intermediate) on the worksheet.
    - *Task 1:* Ss complete the 7 Multiple Choice questions.
    - *Peer Check:* Ss compare answers in pairs, discussing *why* they chose specific options (referencing line numbers).
    - *Feedback:* T provides the Answer Key (A/B/C/D summary) and clarifies the "Resolution" of the story's ending.
  ], "Ss-Ss / T-Ss"),

  stage("FOUR", "Post-reading Reflection", "9", "To personalize the theme and practice critical writing.", [
    - *Writing Task:* Ss respond to the writing prompt: *"Should we help the poor? Or should they just take care of themselves?"*
    - *SCR Link:* Ss relate the girl's "Complication" (lack of help) to their own opinions on social responsibility.
    - *Discussion:* Ss share their most persuasive reason with a partner.
  ], "Ss-Ss"),
))

#v(1cm)
#slideshow_link("https://elwrush.github.io/lesson-plan-agent/28-01-2026-B1-Match-Girl-E/")
