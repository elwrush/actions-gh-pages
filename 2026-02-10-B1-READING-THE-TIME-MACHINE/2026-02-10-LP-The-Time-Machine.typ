#import "/skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(margin: (x: 1.5cm, y: 1.5cm))
#set text(font: "Roboto", size: 11pt)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "10-02-2026",
  cefr: "B1",
  duration: "46 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "Formative (Recall tasks)",
  focus: "Reading for Gist & Detail",
  materials: "Oxford Discover Futures 2, 146-148",
))

#main_aim_box("By the end of the lesson, learners will have practiced scanning and detail-reading sub-skills in the context of a science fiction play script.")

#v(0.5cm)
#differentiation_box("Learners can choose between identifying characters (Standard) or analyzing the foreshadowing techniques (Extension) during the final stages.")

#v(0.5cm)
#text(size: 14pt, weight: "bold", fill: rgb("#A62D26"))[Lesson Procedure]
#v(0.5em)
#stage_table((
  ..stage(1, "Lead-in", "5", "Activate schema & engage", [
    *Fact or Future?*
    - T shows technologies: Time Machine, Invisibility, Mars Colony.
    - Pairs discuss: Which will exist in 50 years? Which is literal fiction?
    - Feedback: T reveals H.G. Wells (today's author) predicted these in 1895. T-Ss.
  ], "T-Ss"),

  ..stage(2, "Pre-teach Vocab", "8", "Remove lexical barriers", [
    *Tech Specs*
    1. *Relativity* (/ˌrel.əˈtɪv.ə.ti/)
    2. *Prototype* (/ˈproʊ.tə.taɪp/)
    3. *Circuit Board*
    4. *Digital Time Display*
    5. *Lever*
    - Ss match words to definitions from glossary.
    - Pairs check against text context. Ss-Ss.
  ], "Ss-Ss"),

  ..stage(3, "Gist / Scanning", "5", "Practice scanning for structure", [
    *Scene Lock-up*
    - Ss have 3 mins to match Scene 1-4 with summary sentences (Task 4). Solo work.
    - Feedback: How did you find the scene? (Names, locations, keywords). T-Ss.
  ], "Solo"),

  ..stage(4, "Main Task (Detail)", "13", "Practice reading for detail", [
    *Character Recall*
    - Ss identify character for 5 actions/lines (Task 3).
    - *Constraint*: Must provide Scene number as evidence (e.g. [Scene 2]).
    - Feedback: Peer-check in pairs then whole class. Ss-Ss.
  ], "Ss-Ss"),

  ..stage(5, "Post-task", "15", "Language focus & Personalization", [
    *The Foreshadowing Detective*
    - *Part 1 (Language)*: Pairs find 1 example of "Foreshadowing" in Scene 3 (e.g., Jasmine's warning).
    - *Part 2 (Personal)*: Discussion: "Destination 3026" - If you had Dan's machine, where would you go? Why? Ss-Ss.
  ], "Ss-Ss"),
))

#slideshow_link("https://elwrush.github.io/actions-gh-pages/2026-02-10-B1-READING-THE-TIME-MACHINE/")


#answer_key([
  *Task 3 (Recall):* 1. Dan's mother, 2. Kai, 3. Jasmine, 4. Dan, 5. Maya.
  
  *Task 4 (Gist):* Scene 1: (4), Scene 2: (2), Scene 3: (5), Scene 4: (3). Extra: (1).
])
