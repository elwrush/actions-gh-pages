#import "../../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: true)

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "10-02-2026",
  cefr: "B1",
  duration: "46 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "Formative / Peer Feedback",
  focus: "Reading",
  materials: "Oxford Discover Futures 2, 146-148",
))

#v(0.5cm)

#main_aim_box(
  "By the end of the lesson, learners will have practiced scanning and detail-reading sub-skills in the context of a science fiction play script, while analyzing character motivations and narrative structure."
)

#v(0.5cm)

#slideshow_link("https://elwrush.github.io/actions-gh-pages/2026-02-10-B1-READING-THE-TIME-MACHINE/")

#v(0.5cm)

#stage_table((
  ..stage(
    1, "Lead-in", "5", "Contextualize the author and genre",
    [
      *The Father of Sci-Fi*
      - Show H.G. Wells profile slide (Task 1).
      - Ss scan for: Publication Date (1895), Concept (Time Machine), Co-founder (Jules Verne).
      - T highlights: Wells predicted the future (Atomic Bomb, Internet) in 1895.
    ],
    "T-Ss / Solo"
  ),
  ..stage(
    2, "Reading / Listening", "12", "Gist and Detail Understanding",
    [
      *Entering the Machine (Task 2)*
      - Play audio (ODF2_SB_2.26.mp3) while students follow the text.
      - Ss answer 5 True / False / Not Mentioned questions.
      - *Key Focus*: Distinguishing between "False" (contradiction) and "Not Mentioned" (absence).
      - Feedback / Peer Check.
    ],
    "Solo -> Ss-Ss"
  ),
  ..stage(
    3, "Character Analysis", "8", "Deep processing of traits",
    [
      *Case Files (Task 3)*
      - Ss identify the character behind specific attitudes/lines.
      - Focus on finding evidence (e.g., specific quotes or actions).
      - Check answers in pairs.
    ],
    "Solo -> Pairs"
  ),
  ..stage(
    4, "Text Structure", "8", "Understanding narrative flow",
    [
      *Timeline Logic (Task 4)*
      - Ss match Scene 1-4 with summary descriptions.
      - Discuss logical progression: Discussion -> Demo -> Specifics -> Climax (Return).
    ],
    "Pairs"
  ),
  ..stage(
    5, "Discussion", "13", "Critical thinking and personalization",
    [
      *The Verdict*
      - Debate: Was Dan right to risk his life for science?
      - *Sides*: Brave Pioneer (Progress requires risk) vs. Reckless Fool (He worried his family).
      - Class vote on the "Verdict".
    ],
    "Groups -> Class"
  ),
))


#answer_key([
  *Task 1 (Scanning):* 1. 1895, 2. Time Travel Machine, 3. Jules Verne.
  
  *Task 2 (Detail - T/F/NM):*
  1. *False* (Weekly, not fortnightly).
  2. *False* (Implied choice, not mandatory).
  3. *True* (Mixed reactions).
  4. *True* (Prototype built first).
  5. *Not Mentioned* (Scene ends before story).

  *Task 3 (Who Said What?):*
  1. Mother (Vague idea), 2. Kai (Critical/Negative), 3. Jasmine (Notices clock), 4. Dan (Serious), 5. Maya (Breaks news).

  *Task 4 (Timeline):*
  Scene 1: Discussion of projects.
  Scene 2: Small machine demo.
  Scene 3: Discussing the prototype.
  Scene 4: Dan returns.
])
