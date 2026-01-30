#import "../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "29-01-2026",
  cefr: "B2",
  duration: "46 Minutes",
  shape: "F (Productive Skills)",
  assessment: "Writing CA",
  focus: "Productive Skills (Speaking/Writing)",
  materials: "Sports Interviews Textbook Handout",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will be better able to report interviews and conversations using a variety of reporting verbs (e.g. _admit, deny, insist_) in the context of sports biographies.
]

#v(0.5cm)

#differentiation_box[
  During the preparation for the role-play (Stage 4), students can choose between three different athletes (Petra, Holly, or Newman) based on their interest. Stronger learners are encouraged to use more complex reporting verbs (_insisted on_, _accused of_) while supported learners can focus on simpler structures (_said that_, _told me_).
]

#v(0.5cm)

#slideshow_link("https://elwrush.github.io/lesson-plan-agent/29-01-2026-B2-Sports-Interviews-F/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "6", "To activate schema and generate interest in the topic of sports biographies.", [
    - *Warmer: "Sports Stars"*
    - T displays images of famous athletes (e.g., LeBron James, Serena Williams) on the board.
    - T asks Ss: "Who are these people? What do you know about their lives?"
    - T elicits keywords: _training, sacrifice, injury, success_.
    - T asks: "How do sports change people's lives? Is it always positive?" (Link to text).
  ], "T-Ss"),
  
  stage("TWO", "Preparation & Input (Reading)", "12", "To provide content input and model target language (reporting verbs).", [
    - *Task 1: Reading for Specific Information (Ex 5)*
    - T hands out the profiles of Petra, Holly, and Newman.
    - Ss read and answer the questions: "Which sport? How have sports changed their lives?"
    - Feedback: T elicits answers from the class.
    - *Task 2: Focus on Reporting Verbs (Ex 6)*
    - T focuses Ss on the quotes 1-6. T asks: "Who said this? Petra, Holly, or Newman?"
    - *Clarification:* T highlights the reporting verbs (_admit, explain, complain, offer, deny, insist_).
    - T checks meaning: "Which verb means to say something is not true?" (_Deny_). "Which verb means to demand something strongly?" (_Insist_).
    - *Drilling:* T drills pronunciation of the verbs, focusing on stress (e.g., _ad-MIT_, _de-NY_).
  ], "T-Ss / Ss-Ss"),

  stage("THREE", "Preparation for Output", "8", "To scaffold the productive task by preparing questions.", [
    - *Task 3: Interview Preparation (Ex 7)*
    - T puts Ss in pairs.
    - T instructions: "Choose ONE athlete. Imagine you are going to interview them."
    - T directs Ss to the example questions:
      - "When did you first become interested in sports?"
      - "Have your families and friends encouraged you?"
    - Ss write 2-3 more questions using the prompts in the book or their own ideas.
    - T monitors and supports with vocabulary.
  ], "Ss-Ss"),

  stage("FOUR", "Productive Task (Speaking Role-play)", "10", "To provide oral practice of the interview context.", [
    - *Task 4: The Interview (Ex 8)*
    - T assigns roles: Student A = Athlete, Student B = Interviewer.
    - Student B asks the questions; Student A answers (using imagination based on the profile).
    - *Critical Step:* Student B must take notest on the answers (for the writing task).
    - T monitors conversations.
  ], "Ss-Ss"),

  stage("FIVE", "Productive Task (Writing)", "10", "To practice reporting the interview using target language.", [
    - *Task 5: Writing the Article (Ex 9)*
    - T instructs Ss: "Now, you are the journalist. Write a short paragraph for _Sports Without Borders_ magazine."
    - T highlights the sentence starter: "For this article, I interviewed [Name]..."
    - *Constraint:* Ss must use at least 3 reporting verbs from Stage 2.
    - Ss write their paragraphs individually.
    - *Plenary:* T asks 1-2 students to read their reports to the class if time permits.
  ], "Indiv"),
))
