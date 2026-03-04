#import "/skills/02-writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("intensive")

#metadata_table((
  teacher: "Ed Rush",
  date: "02-03-2026",
  cefr: "B1",
  duration: "45 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "N/A",
  focus: "Listening",
  materials: "Oxford Discover Futures 3, WB p.9, Track 1.01",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced the sub-skills of listening for gist and specific detail in the context of a podcast interview about the influence of digital media versus parents on teenagers.
]

#v(0.5cm)

#differentiation_box[
  Support is provided by pre-teaching key lexical items related to social influence (e.g., generation gap, psychologist) and using a staged listening approach (global to specific). Differentiated peer-checking allows students to support each other during the detailed matching task.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/28Jan-Listening-WB-p9/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "5", "To engage Ss and activate schemata", [
    - *Digital Influencer Quiz*: Display three statements about YouTube and social media influence (e.g., "70% of teens trust YouTubers more than traditional celebrities").
    - Ss discuss 'Fact' or 'Fiction' in pairs (Ss-Ss).
    - Elicit brief feedback: "Who has more influence on what you buy: your parents or a YouTuber you follow?" (T-S).
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Pre-teach Vocab", "8", "To remove lexical barriers", [
    - Contextual Discovery: Present 5 target words:
      - *generation gap*
      - *psychologist*
      - *influence*
      - *well-being*
      - *personal finance*
    - T provide English context sentences for each item. (e.g., "The *generation gap* makes it hard for my grandma to understand TikTok.")
    - Ss match words to definitions in pairs (Ss-Ss). Elicit Thai translations for consolidation.
    - Model and drill pronunciation, highlighting stress in *psy-cho-lo-gist* and *ge-ne-ra-tion*. (T-S).
  ], "T-Ss / Ss-Ss"),

  stage("THREE", "Gist / Scanning", "7", "To practice global listening", [
    - *Speed Listen (Gist)*: Set a *2-minute* timer for the first global task.
    - Play Track 1.01. Ss listen for the *Main Topic* (Ex 1) and Dr. Schmidt's job (Ex 2).
    - Ss compare answers in pairs (Ss-Ss) before a quick class vote.
    - *Feedback*: Elicit answers and ask: "Was it easy to hear the main topic? Which keywords helped?" (T-S).
  ], "S / Ss-Ss"),

  stage("FOUR", "Main Task (Detail)", "15", "To practice listening for specific detail", [
    - *Detailed Listening*: Play Track 1.01 again. Ss answer the multiple-choice questions in Ex 3 (S).
    - *Data Detective (Ex 4)*: Play specific segments if needed for Ss to match research findings to Dr. Schmidt's points (S).
    - *Peer-Check*: Ss swap workbooks and check answers in pairs.
    - *Detailed Feedback*: Discuss correct options and elicit evidence from the transcript (e.g., why parents still influence education). (T-S).
  ], "S / T-Ss"),

  stage("FIVE", "Post-task", "10", "To personalize and recycle language", [
    - *The Influence Debate (Ex 5)*: Ss discuss four topics in small groups: education, finance, health, and well-being.
    - *Prompt*: "In which of these areas do you listen to your parents the most? In which do you listen to the internet?"
    - T monitors for "good language" and provides content feedback and brief error correction to conclude. (Ss-Ss).
  ], "Ss-Ss"),
))

#answer_key[
  *Ex 3 (MCQ)*: 1-b, 2-d, 3-d, 4-a, 5-c. 
  *Ex 4 (Matching)*: 1-a, 2-g, 3-d, 4-c, 5-f, 6-e, 7-b.
]
