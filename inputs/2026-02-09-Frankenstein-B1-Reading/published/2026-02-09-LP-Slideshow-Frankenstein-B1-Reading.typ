#import "../../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

// DOCUMENT SETUP
#set page(
  paper: "a4",
  margin: (x: 2cm, y: 2cm),
)
#set text(font: "Arial", size: 11pt)

// HEADER
#lesson_header("bell")

// METADATA
#metadata_table((
  teacher: "Ed Rush",
  date: "09-02-2026",
  cefr: "B1",
  duration: "50 mins",
  shape: "E (Receptive Skills)",
  assessment: "Reading Comprehension",
  focus: "Reading for Detail & Scanning",
  materials: "Frankenstein Excerpt, Slideshow, Mini-Whiteboards",
))

// MAIN AIM
#v(0.5cm)
#main_aim_box("By the end of the lesson, learners will have practiced the sub-skills of scanning for facts and reading for detail in the context of an excerpt from the novel Frankenstein.")

// DIFFERENTIATION
#v(0.5cm)
#differentiation_box("Students can choose to read the text alone or in pairs. Key vocabulary is pre-taught visually to support lower-level learners.")

// SLIDESHOW LINK
#slideshow_link("https://lesson-slideshows.pages.dev/2026-02-09-Frankenstein-B1-Reading/")

// STAGES
#v(0.5cm)
= Lesson Procedure

#stage_table((
  stage("1", "Lead-in", "7", "To engage Ss and activate schema", [
    - *Part 1* – Mini WB. 1 per student. Ss work in teams to answer: "Who is Frankenstein: the Man or the Monster?" and "What is his first name?" 1 min. Feedback.
    - *Part 2* – Display 6 genre icons. In pairs, Ss negotiate which two best describe a story about a scientist creating life in 1818. 2 min. Feedback.
    - *Part 3* – Show title "FRANKENSTEIN" with lightning visual. Ss tell partner one thing they know about the story. 1 min. Feedback.
  ], "T-Ss"),

  stage("2", "Pre-teach Vocabulary", "10", "To remove blocking vocabulary", [
    - *Part 1* – Present 5 context sentences on PP (seized, isolated, disappointment, promising, tragedy). Ss in pairs guess meanings based on narrative clues. 4 min.
    - *Part 2* – Drill pronunciation of target words. Focus on word stress for 'disappointment' and 'isolated'. 2 min.
    - *Part 3* – Mini WB Check. T says a definition, Ss race to write the correct word. 2 min. Feedback.
  ], "T-Ss"),

  stage("3", "Reading for detail and specific information", "25", "To practice scanning & sequencing", [
    - *Part 1 (Scanning Race)* – Ss open texts to Mary Shelley biography. Task: Find Who, Where, When, and How. First team to finish all four wins. 4 min. Feedback.
    - *Part 2 (Prediction)* – Ss read the first two paragraphs of narrative. Use Task 3 "Guess the Words" to check initial impressions of Victor's character. 5 min. Feedback.
    - *Part 3 (Sequencing)* – Ss read the full excerpt. Task: Put events A-F in order. 8 min. Pairs swap worksheets and check against the key on PP. 3 min. Feedback.
  ], "S/Ss-Ss"),

  stage("4", "Post-reading speaking task", "8", "To react to the content", [
    - *Part 1* – In pairs, Ss discuss Victor's 'flaws'. "Was he reckless or just ambitious?" "Is he responsible for what happened?" 4 min.
    - *Part 2* – Whole class feedback. T collects 3-4 opinions on the main theme (Dangerous Knowledge). 2 min. Content + language feedback.
  ], "Ss-Ss")
))

// ANSWER KEY
#answer_key([
  *Task 1 (Genre)*: Early Science Fiction / Classic Horror \
  *Task 2 (Profile)*: Mary Shelley, Near Geneva, Summer 1816, Ghost story challenge. \
  *Task 3 (Prediction)*: 1. Promising, 2. How life begins, 3. Isolated, 4. A storm, 5. Fear. \
  *Task 4 (Sequence)*: 1.e, 2.a, 3.d, 4.b, 5.f, 6.c \
  *Task 5 (Narrator)*: Victor Frankenstein (Later date/regretful tone). \
  *Task 7 (Flaws)*: Obsessive, Irresponsible, Reckless. \
  *Task 8 (Themes)*: Dangerous Knowledge, Morality.
])