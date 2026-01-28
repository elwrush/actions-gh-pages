#import "../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
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
  materials: "27-01-2026-B1-Superconsumer-Generation-Reading-Bell.pdf",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced and developed the sub-skills of reading for gist (skimming) and detailed information (scanning) in the context of analyzing the "Superconsumer" habits of Generation Y.
]

#v(0.5cm)

#differentiation_box[
  This lesson employs a "Tiered Text" strategy, allowing students to access a B2 "Advanced Reading Extension" if they complete the B1 tasks ahead of schedule. This ensures high-ability learners remain challenged (i+1) while supporting the B1 core group.
]

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in & Vocabulary", "14", "To activate schema and clarify key vocabulary.", [
    - *Part 1: Video Hook* (6 min). Play the YouTube video (https://www.youtube.com/watch?v=_x48tY5sfYM) showing conditions in an Amazon fulfillment center. 
    - Ss watch and discuss in pairs: "What is the 'cost' of getting our products so fast?" and "How does this make you feel about big companies like Amazon?" 
    - *Part 2: Skill-Based Warmup* (4 min). Hand out worksheet. Ss discuss Task 1: "Where do you shop most often?" and compare with parents/grandparents.
    - *Part 3: Vocabulary* (4 min). Elicit/Clarify 5 markers: *Demand*, *Multinational*, *Influence*, *Interact*, *Personalize*. Ss match words to context sentences.
  ], "Ss-Ss / T-Ss"),
  
  stage("TWO", "Reading for Gist & Detail", "23", "To practice skimming and scanning sub-skills.", [
    - *Global Reading* (6 min). Ss skim paragraph 2-6 and complete Task 2: Matching headings. Check in pairs then whole class feedback.
    - *Scan for Numbers* (8 min). Ss scan the text for specific numbers to complete Task 3. Focus on fast processing of numerical data.
    - *Close Reading (Detailed)* (9 min). Ss read carefully to decide T/F/NG for Task 4. Feedback focusing on the evidence in the text rather than personal opinion.
    - *Fast Finishers*: Direct students to the "B2 Reading Extension" on page 6.
  ], "Ss-Ss / Indiv"),
  
  stage("THREE", "Post-reading Reflection", "9", "To personalize the topic and practice evaluation.", [
    - *Critical Thinking* (Task 5). Ss reflect on the situational prompt about generational shopping habits. 
    - Ss write a short response (min. 70 words) using the identity block on page 5.
    - T monitors for content and language, providing 1-to-1 feedback.
  ], "Indiv / T-Ss"),
))
