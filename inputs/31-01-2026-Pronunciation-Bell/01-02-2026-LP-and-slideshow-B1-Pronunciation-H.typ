#import "/skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

// --- DOCUMENT SETUP ---
#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 1.5cm, x: 2cm),
)
#set text(font: "Arial", size: 11pt)

// --- HEADER ---
#lesson_header("intensive")

// --- METADATA ---
#metadata_table((
  teacher: "Ed Rush",
  date: "01 Feb 2026",
  cefr: "B1",
  duration: "46 Minutes",
  shape: "Shape H (SCR Discovery)",
  assessment: "Peer Transcription (Secret Code Swap)",
  focus: "Pronunciation: Sounds & Symbols",
  materials: "Worksheet, Interactive Slideshow, Audio Track 15",
))

#v(0.5cm)
#main_aim_box("To discover that English spelling is unreliable and that the Phonemic Chart is 'The Map' required to decode and produce accurate spoken sentences.")

#slideshow_link("https://elwrush.github.io/lesson-plan-agent/31-01-2026-Pronunciation-Bell/")

// --- STAGES ---
#stage_table((
  stage(
    "1", "SITUATION: THE LIE", "5",
    "Establish common ground & create tension",
    [
      - Show Slide 4 ("ENGLISH IS A LIE"). 
      - Elicit from the class: "How many letters are in the alphabet?" (26). "How many sounds are in English?" (44). 
      - T-S Action: Write 'ough' on the board. Ask students to pronounce it in: *though, through, tough, cough*. 
      - Highlight the frustration: Different sounds for the same letters. Establish that current skills (relying on spelling) lead to communication breakdown. Use the simile: "English spelling is like a broken GPS—it tells you one thing, but leads you somewhere else."
    ],
    "T-Ss"
  ),
  stage(
    "2", "SITUATION: PRE-TEACH VOCABULARY", "5",
    "Pre-teach blocking vocabulary",
    [
      - T-S: Present 3 essential terms for the lesson using Slide 5 visuals:
        1. *Symbol* /ˈsɪm.bəl/: A sign that represents a sound. E.g., /p/.
        2. *Vibrate* /vaɪˈbreɪt/: To move quickly back and forth. (Demonstrate with phone or throat).
        3. *Encode* /ɪnˈkəʊd/: To turn a normal word into a secret code.
      - Elicit: "If I write /p/, is that a letter or a symbol?" (Symbol).
      - Drill these words chorally to ensure students can talk about the lesson goals accurately.
    ],
    "T-Ss"
  ),
  stage(
    "3", "COMPLICATION: VIBRATION", "7",
    "Trigger functional breakdown & pattern recognition",
    [
      - Show Slide 5. Introduce the "Finger on Throat" technique.
      - Elicit: Students say /p/ (Quiet) then /b/ (Loud). Ask: "Which one makes your throat vibrate?" (Voiced /b/).
      - T-S: Direct students to the blue (Unvoiced) and orange (Voiced) color coding on their charts. 
      - Pairs (Ss-Ss): Students test each other's throats for /t/ vs /d/, /k/ vs /ɡ/, /f/ vs /v/. 
      - Insight: If you don't know the symbol, you don't know if it's 'quiet' or 'loud'—leading to mistakes like 'bat' sounding like 'pat'. Elicit if they can feel the difference in their own names.
    ],
    "Ss-Ss"
  ),
  stage(
    "4", "COMPLICATION: THE VOWEL TRAP", "7",
    "Deepen the problem (Discovery)",
    [
      - Show Slide 6. Highlight the "Alphabet Names" (A, E, I, O, U).
      - Elicit: "Say the letter 'A'." (They say /eɪ/). T-S: Show them /eɪ/ on the chart.
      - Discovery: Students hunt their worksheet charts to find the symbols for E (/iː/), I (/aɪ/), O (/əʊ/), and U (/uː/).
      - CCQ: "Is the sound /eɪ/ one sound or two sounds moving together?" (Two—it's a diphthong).
      - Insight: Our 'familiar' letter names are actually some of the most complex sounds in the IPA. Students realize they need 'The Map' even for the basics.
    ],
    "T-Ss"
  ),
  stage(
    "5", "RESOLUTION: THE MAP IN ACTION", "9",
    "Practice using the solution strategy",
    [
      - Show Slide 8 (TASK 1). T-S: Explain that the chart is 'The Map' to escape 'The Lie' of spelling.
      - Task (Individual): Play audio track 15. Students listen and decode the first 4 phonemic sentences on their worksheet. 
      - Monitoring: T checks for students using the chart as a reference rather than guessing based on spelling.
      - Feedback: Reveal answers on Slide 10. Students self-correct and reflect on which symbols were the hardest to 'read'. Elicit: "Did the map help you catch the difference between Tom and Tim?"
    ],
    "Indiv"
  ),
  stage(
    "6", "REFINING THE SENSES", "4",
    "Refine the skill",
    [
      - Show Slides 13-14 (TASK 2 & 3). 
      - Task (Individual): Students listen to 10 words and tick /ɒ/, /ɔː/, or /əʊ/.
      - Comparison (Ss-Ss): Students compare their sorting results in pairs before the teacher reveals the answer slides.
      - T-S: Teacher drills any problematic words (e.g., 'quarrel' vs 'water'). Focus on lip position for /ɔː/ vs /əʊ/.
    ],
    "Ss-Ss"
  ),
  stage(
    "7", "THE FINAL CHALLENGE", "9",
    "Application of insight (Freer Practice)",
    [
      - Show Slide 24. Explain "THE SECRET CODE SWAP."
      - Task (Pairs): Students write one "Secret Sentence" about their classroom or partner (e.g., "Paul has a black pen").
      - Encoding: Students use their worksheet chart to transcribe it into phonemic symbols ONLY. No English letters allowed!
      - Swap: Students swap papers. Partner must speak the sentence aloud to "break the code."
      - Monitoring: T moves between pairs, ensuring clear pronunciation and correct phoneme mapping. Note any common errors for final whole-class feedback.
    ],
    "Pairs"
  ),
))

#v(0.5cm)
#differentiation_box("Students choose their own sentences for the final challenge, allowing for self-leveling based on their comfort with the phonemic symbols. Stronger students can attempt complex diphthongs like /əʊ/ and /ɔɪ/.")

#answer_key([
  *Task 1:* 1. Tom likes writing poetry. 2. Jane's got a friendly brown pet cat. 3. Sue was fast asleep...
  *Task 2:* 1. clock (/ɒ/), 2. sport (/ɔː/), 3. boat (/əʊ/), 4. saw (/ɔː/), 5. got (/ɒ/)...
])