#import "/skills/02-writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("intensive")

#metadata_table((
  teacher: "Ed Rush",
  date: "29-01-2026",
  cefr: "B1",
  duration: "45 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "N/A",
  focus: "Reading",
  materials: "Unit 2 - Legendary Cities (WB p.14-15)",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced the sub-skills of scanning for specific information and reading for detail in the context of three legendary cities: Atlantis, El Dorado, and Shangri-La.
]

#v(0.5cm)

#differentiation_box[
  Support is provided by pre-teaching key lexical items related to legendary cities (e.g., philosopher, ritual, fictional) and using a staged reading approach (scanning for specific data before detailed comprehension). Peer-checking allows students to support each other during the gap-fill and multiple-choice tasks.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/29-Jan-Reading-Part-6/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "5", "To engage Ss and activate schemata", [
    - *Legendary Cities Quiz*: Display three statements about "lost cities" (e.g., "Atlantis was a real city in the Atlantic Ocean," "El Dorado was a city made of solid gold").
    - Ss discuss 'Fact' or 'Fiction' in pairs (Ss-Ss).
    - Elicit brief feedback: "Do you think these places ever existed?" (T-S).
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Pre-teach Vocab", "8", "To remove lexical barriers", [
    - Contextual Discovery: Present 5 target words:
      - *philosopher*
      - *earthquake*
      - *ritual*
      - *fictional*
      - *paradise*
    - T provide English context sentences for each item (e.g., "Plato was a famous Greek *philosopher* who wrote about Atlantis.").
    - Ss match words to definitions in pairs (Ss-Ss). Elicit Thai translations for consolidation.
    - Model and drill pronunciation, highlighting stress in *phi-LO-so-pher* and *RI-tu-al*. (T-S).
  ], "T-Ss / Ss-Ss"),

  stage("THREE", "Gist / Scanning", "7", "To practice scanning for specific info", [
    - *Speed Scan (Summary)*: Set a *4-minute* timer for the scanning task (WB Ex 3).
    - Ss scan the text on p.15 to fill the 10 gaps in the summary with names, dates, and numbers.
    - Ss compare answers in pairs (Ss-Ss).
    - *Feedback*: Elicit answers and ask: "Was it easy to find the numbers and names?" (T-S).
  ], "S / Ss-Ss"),

  stage("FOUR", "Main Task (Detail)", "15", "To practice reading for specific detail", [
    - *Data Detectives*: Ss read the article again to answer the multiple-choice questions in Ex 5 (S).
    - *Evidence Hunt (Ex 4)*: Ss answer the three questions and *underline* the specific sentence in the text that provides the proof.
    - *Peer-Check*: Ss check their answers in pairs, comparing their underlined evidence.
    - *Detailed Feedback*: Discuss correct options and elicit evidence from the text (e.g., why Atlantis disappeared). (T-S).
  ], "S / T-Ss"),

  stage("FIVE", "Post-task", "10", "To personalize and recycle language", [
    - *Your Shangri-La (Ex 6)*: Ss discuss their "dream city" in small groups.
    - *Prompt*: "What would your dream city look like? What would it have? What would it *definitely not* have?"
    - T monitors for recycling of descriptive adjectives (e.g., *remote, beautiful, powerful*).
    - Conclude with brief content feedback. (Ss-Ss).
  ], "Ss-Ss"),
))

#answer_key[
  *Ex 3 (Summary)*: 1. 2,000, 2. earthquake, 3. India, 4. Japan, 5. Greece, 6. 1500s, 7. Muisca, 8. Kunlun, 9. Lost Horizon, 10. 1933. 
  *Ex 4 (Questions)*: 1. No, he didn't. 2. No, they didn't. 3. No, they haven't. 
  *Ex 5 (MCQ)*: 1-c, 2-a, 3-b, 4-b, 5-d, 6-c.
]
