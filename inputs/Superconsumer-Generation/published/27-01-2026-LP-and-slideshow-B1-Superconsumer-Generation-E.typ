
#import "../../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2.5cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "27-01-2026",
  cefr: "B1",
  duration: "46 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "N/A",
  focus: "Reading",
  materials: "B1-Superconsumer-Reading.pdf / B2-Ext.pdf",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have developed their reading sub-skills of skimming for gist and scanning for numerical data within the context of analyzing the "Superconsumer" habits of Generation Y.
]

#v(0.5cm)

#differentiation_box[
  This lesson utilizes a "Tiered Text" strategy. Higher-ability learners (B2 range) are provided with a more linguistically complex version of the text (B2 Extension) should they complete the B1 tasks ahead of schedule.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/Superconsumer-Generation/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in & Vocabulary", "14", "To activate schema and clarify key vocabulary.", [
    - *Part 1: Video Hook* (6 min). Play the YouTube video (https://www.youtube.com/watch?v=_x48tY5sfYM) showing Amazon fulfillment center. 
    - Elicit curiosity: "What is the 'cost' of getting our products so fast?"
    - *Part 2: Pre-Teach Vocabulary* (8 min). Clarify/Elicit markers:
      1. *Demand* /dɪˈmɑːnd/: A strong request for something to be provided.
      2. *Multinational* /ˌmʌltiˈnæʃnəl/: Involving several different countries.
      3. *Influence* /ˈɪnfluəns/: The power to have an effect on people or things.
      4. *Interact* /ˌɪntərˈækt/: To communicate or do things with other people.
      5. *Personalize* /ˈpɜːrsənəlaɪz/: To design or change something so that it is suitable for a particular person.
  ], "Ss-Ss / T-Ss"),
  
  stage("TWO", "Reading for Gist & Detail", "23", "To practice skimming and scanning sub-skills.", [
    - *Skimming (Task 2)* (6 min). Ss skim paragraphs 2-6 to match headings. Focus on speed.
    - *Scanning for Numbers (Task 3)* (8 min). Ss scan for specific figures to identify their context.
    - *Detailed Reading (Task 4)* (9 min). T/F/NG task. Ss must find textual evidence for their answers.
    - *Fast Finisher*: Direct to "B2 Reading Extension" at the end of the material.
  ], "Indiv / Ss-Ss"),
  
  stage("THREE", "Reflection & Critical Thinking", "9", "To personalize the topic and practice analytical writing.", [
    - *Personalization (Task 5)*. Ss discuss their shopping habits vs. their parents'.
    - *Writing Production*. Ss write a reflection (min. 70 words) on: Trust in influencers, Personalized ads, and Social Media impact.
    - T monitors timings (10 min timer).
  ], "Ss-Ss / Indiv"),
))

