#import "/skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "29-01-2026",
  cefr: "B2",
  duration: "45 Minutes",
  shape: "F (Productive Skills)",
  assessment: "N/A",
  focus: "Speaking",
  materials: "Oxford Discover Futures 3, p. 85",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will be better able to prepare and conduct professional sports interviews using a variety of reporting verbs (e.g., _admit, deny, explain_) in the context of young athlete profiles.
]

#v(0.5cm)

#differentiation_box[
  During the preparation for the role-play (Stage 3), students can choose between three different athletes (Petra, Holly, or Newman) based on their interest. Stronger learners are encouraged to use more complex reporting verbs (_insisted on_, _accused of_) while supported learners can focus on simpler structures (_said that_, _told me_).
]

#v(0.5cm)

#slideshow_link("https://elwrush.github.io/lesson-plan-agent/29-01-2026-B2-Sports-Interviews-F/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "6", "To activate schema and generate interest in the topic of sports interviews.", [
    - *Warmer: "Sports Observation"*
    - T uses slideshow to display 7-second clips of Hockey, Badminton, and Basketball.
    - T asks Ss to observe and discuss in pairs: "What are the merits? The risks? Skills needed?"
    - T elicits keywords to the board: _agility, pressure, dedication, sacrifice_.
    - T introduces the "Mission": To become professional sports journalists today.
  ], "T-Ss / Ss-Ss"),
  
  stage("TWO", "Preparation & Input", "12", "To provide content input and model target language (reporting verbs).", [
    - *Task 1: Reading for Specific Information (Ex 5)*
    - T directs Ss to the profiles of Petra, Holly, and Newman on p. 85.
    - Ss read and answer: "How have sports changed their lives? What pressure do they face?"
    - Feedback: T elicits key biographical details.
    - *Task 2: Focus on Reporting Verbs (Ex 6)*
    - T displays the quotes 1-6. Ss match quotes to the correct athlete.
    - *Clarification:* T highlights the verbs: _admit, explain, complain, offer, deny, insist_.
    - T checks meaning using CCQs: "If I say I didn't do something, am I denying or insisting?" (_Denying_). "If I give you tickets for free, am I explaining or offering?" (_Offering_).
    - T drills pronunciation, focusing on word stress: _ad-MIT_, _ex-PLAIN_, _in-SIST_.
  ], "T-Ss / Ss-Ss"),

  stage("THREE", "Preparation for Output", "8", "To scaffold the productive task by preparing interview questions.", [
    - *Task 3: Interview Prep (Ex 7)*
    - T puts Ss in pairs. Ss choose ONE athlete to interview.
    - T directs Ss to the prompts: _Interest in sports, Family encouragement_.
    - Ss write 3 additional professional questions for their chosen athlete.
    - T monitors, ensuring questions are open-ended (e.g., "How did you feel after the accident?" rather than "Were you sad?").
  ], "Ss-Ss"),

  stage("FOUR", "Productive Task (Speaking)", "19", "To provide oral practice of the interview context using target speech.", [
    - *Task 4: The 1-Minute Interview (Ex 8)*
    - Roles: Student A = Athlete, Student B = Journalist.
    - T starts the 1-minute timer on the slideshow.
    - Ss conduct the interview. Journalist (B) MUST take notes on the athlete's answers.
    - T monitors for "Journalistic Energy" and accuracy of pronunciation.
    - Feedback: T highlights 1-2 examples of good interviewing technique heard during monitoring.
  ], "Ss-Ss"),
))
