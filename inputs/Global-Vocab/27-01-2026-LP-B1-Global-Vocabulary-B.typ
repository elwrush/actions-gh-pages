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
  shape: "B (Language Practice)",
  assessment: "N/A",
  focus: "Vocabulary (Countries, People, Languages)",
  materials: "27-01-26-Global-Vocabulary-Bell.pdf, YouTube: https://www.youtube.com/watch?v=xbGQeHCXQcs (7:44-11:44)",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have had an opportunity to practice using vocabulary for countries, nationalities, and languages and will be better able to discuss global identities, regional locations, and personal travel experiences in the context of a "Global Explorer" theme.
]

#v(0.5cm)

#differentiation_box[
  This lesson utilizes a "Mingle & Mirror" strategy during the final stage. While the worksheet provides a structured framework for B1 learners, stronger students (B2) are encouraged to provide more detailed population estimates and historical context for their visited countries, while A2+ students can rely on the regional mapping prompts for scaffolding.
]

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in: Global Video Quiz", "8", "To activate schema and spark interest in global geography.", [
    - *Situation*: Class is starting a "Global Explorer" mission. 
    - T plays YouTube video (xbGQeHCXQcs) clipped at 7:44-11:44.
    - Ss watch the "World Geography Quiz" segment and race to identify the countries, capitals, or flags shown.
    - T pauses at key frames to elicit/correct pronunciation.
    - *Transition*: "Now that we've seen the world on screen, let's look at how we talk about these places and their people."
  ], "T-Ss / Ss-Ss"),
  
  stage("TWO", "Controlled Practice: Regional Mapping", "15", "To solidify knowledge of regional terms and continent locations.", [
    - T refers Ss to the *Reference Section* on the worksheet.
    - Briefly clarify "The Middle East" vs "The Far East" using the examples provided.
    - *Task 1 & 2*: Ss work individually to complete the "Quick Quiz" and "Regional Mapping" exercises.
    - T monitors for spelling (e.g., *Portuguese*, *Israelis*).
    - Peer-check answers in pairs before open class feedback.
  ], "Ss-Ss / T-Ss"),
  
  stage("THREE", "Semi-Controlled Practice: Stress & People", "13", "To practice word-level stress and the grammar of collective nationalities.", [
    - *Task 3*: T models the first two stress patterns (Bra-ZI-lian, Chi-NESE). 
    - Ss underline the main stress in the remaining words. Drill pronunciation chorally.
    - *Task 5*: T clarifies the "People" grammar (Suffixes vs. 'The').
    - Marker Sentence: "Thais/Brazilians are..." vs "The French/The British are..."
    - Ss complete Task 5 by transforming the country name in brackets.
    - Feedback focused on the inclusion/exclusion of 'The' and 's'.
  ], "T-Ss"),
  
  stage("FOUR", "Freer Practice: Passport Control & Debate", "10", "To provide freer practice using target language in personalized and critical contexts.", [
    - *Passport Control*: Ss complete the "Over to You" grid for themselves.
    - Mingle: Ss must visit 3 different partners and "interview" them like passport officers, noting down interesting facts.
    - *Critical Thinking*: T poses the debate question: "How would the world be different if everyone spoke the same language?"
    - Ss discuss in small groups, taking notes on the final writing lines.
    - *Content Feedback*: T elicits a few interesting opinions and provides language feedback on common errors noted during the mingle.
  ], "Ss-Ss"),
))
