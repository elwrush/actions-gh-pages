#import "../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("intensive")

#metadata_table((
  teacher: "Ed Rush",
  date: "27-01-2026",
  cefr: "B1",
  duration: "45 Minutes",
  shape: "E (Receptive Skills - Listening)",
  assessment: "N/A",
  focus: "Skills (Listening)",
  materials: "raw_content.md, custom worksheet",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced and developed the sub-skills of listening for gist and detailed comprehension in the context of a news report about the Bondi Beach attack and acts of community bravery.
]

#v(0.5cm)

#differentiation_box[
  This lesson employs a "Tiered Support" strategy. Vocabulary pre-teaching ensures B1 learners can access the denser parts of the news report. During detail tasks, learners are encouraged to negotiate meaning in pairs before class-wide feedback, promoting peer-learning and reducing cognitive load.
]

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "10", "To activate schema and interest in the topic of Bondi Beach and news reports.", [
    - *Part 1*: Display a high-quality image of Bondi Beach on the projector. Ss work in pairs to answer: "Where is this?" and "What do people usually do here?" (5 min). Feedback to establish Sydney/Australia context.
    - *Part 2*: "What makes a person a 'hero'?" Ss brainstorm 3 qualities in pairs. 3 min. Brief open-class feedback to prime the "acts of bravery" theme in the recording.
  ], "Ss-Ss / T-Ss"),
  
  stage("TWO", "Pre-teach Vocabulary", "8", "To clarify blocking vocabulary and ensure students can access the listening text.", [
    - Elicit/Pre-teach 5 blocking words: *targeted, receiving treatment, disarm, overwhelmed, tight-knit*. 
    - Use context sentences on the board/slides. Ss guess meanings in pairs. 
    - Drill for pronunciation (especially *targeted* and *overwhelmed*). 5 min. 
    - Concept Check Questions (CCQs): "If you are overwhelmed, do you feel calm?" (No). 3 min.
  ], "T-Ss / Ss-Ss"),

  stage("THREE", "Listening for gist and specific information", "22", "To practice listening for the main idea (gist) followed by detailed comprehension.", [
    - *Task 1 (Gist)*: Play recording 00:00 - 01:00. Ss answer: "What happened, and why were people gathered there?" (Celebrate Hanukkah). 4 min. Peer-check then feedback.
    - *Task 2 (Detail)*: Play 01:00 - 02:15. Ss answer 4 questions on the worksheet: (1) Death toll? (2) Gunmen status? (3) Hiding spots? (4) Who is Ahmed Al Ahmed? 8 min. Ss negotiate answers in pairs before class feedback.
    - *Task 3 (Advice)*: Play 02:15 - 03:30. Ss tick advice given by the presenter (e.g., focus on good news, switch off if needed). 6 min. Peer-check and check answers against the key.
    - *Task 4 (Community)*: Play final section. Pairs discuss what "tight-knit" means in this context. 4 min.
  ], "Individual / Ss-Ss"),

  stage("FOUR", "Post-listening speaking task", "5", "To personalize the topic and speak about community support.", [
    - In small groups, Ss discuss: "How can a community help each other after a bad event?" and "Why is it important to focus on the good news too?" 4 min.
    - Brief open-class wrap-up and language feedback. 1 min.
  ], "Ss-Ss"),
))
