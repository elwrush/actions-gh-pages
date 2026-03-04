#import "../../skills/02-writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#lesson_header("intensive")

#metadata_table((
  teacher: "Ed Rush",
  date: "11-02-2026",
  cefr: "B1",
  duration: "45 Minutes",
  shape: "E (Receptive Skills)",
  assessment: "N/A",
  focus: "Listening",
  materials: "Oxford Future Directions Workbook Listening Unit 2 (p. 19)",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced identifying advantages and disadvantages in the context of a listening text about car-free zones and map navigation.
]

#v(0.5cm)

#differentiation_box[
  Support is provided by pre-teaching key vocabulary (pedestrians, air pollution, handicapped) using visual aids. The listening task is chunked to reduce cognitive load: a gist question first, followed by detailed data extraction. Fast finishers during the vocabulary stage can write their own example sentences.
]

#v(0.5cm)
#slideshow_link("https://elwrush.github.io/actions-gh-pages/11-feb-2026-listening-car-free-zones/")

#v(0.5cm)

#stage_table((
  stage("ONE", "Lead-in", "5", "To engage Ss and activate schemata", [
    - *Part 1: Map Challenge*: Show the map on the board (from WB p. 19). Ss identify the gray area (car-free zone).
    - *Part 2: Prediction*: Pairs discuss: "What are the pros and cons of no cars in the city center?" (Exercise 1). (Ss-Ss).
    - *Feedback*: T elicits ideas and writes them on the board to preview listening themes. (T-Ss).
  ], "T-Ss / Ss-Ss"),

  stage("TWO", "Pre-teach Vocab", "7", "To remove linguistic barriers to comprehension", [
    - *Part 1: Visual Match*: Present target concepts using high-impact visuals: *pedestrians*, *air pollution*, *handicapped*, *carbon footprint*.
    - *Part 2: CCQs*: Use Concept Checking Questions. e.g., "Are pedestrians walking or driving?" "Is air pollution good for health?"
    - *Part 3: Drill*: Model and drill pronunciation chorally and individually, highlighting tricky sounds. (T-Ss).
  ], "T-Ss"),

  stage("THREE", "Gist / Scanning", "5", "To provide a purpose for first listening", [
    - *Part 1: The Big Picture*: T sets the task: "Listen once. Where is the girl going? What is the main topic of the conversation?"
    - *Listen*: Play audio track ODF3 WB 2.01. (S).
    - *Part 2: Check*: Ss briefly compare answers in pairs before whole-class feedback. (Destination: School/Town center; Topic: Car-free zones/Directions). (Ss-Ss / T-Ss).
  ], "S / Ss-Ss / T-Ss"),

  stage("FOUR", "Main Task (Detail)", "10", "To practice listening for specific information", [
    - *Part 1: Data Collection*: Ss look at the chart in Exercise 2.
    - *Listen Again*: Play the audio. Ss note down the advantages and disadvantages mentioned by the Mom and Girl. (S).
    - *Part 2: Peer Check*: Ss compare their charts in pairs. (Ss-Ss).
    - *Feedback*: T elicits answers and clarifies any tricky points using snippets from the audio script if needed. (T-Ss).
  ], "S / Ss-Ss / T-Ss"),

  stage("FIVE", "Vocabulary Focus", "10", "To focus on useful phrases for map navigation", [
    - *Part 1: Map Talk*: Ss complete Exercise 4 (Choose the correct word) individually. (S).
    - *Part 2: Dialogue Build*: Ss use the phrases to complete the dialogue in Exercise 5. (S).
    - *Verify*: Play the audio one last time for Ss to check their dialogue answers. Discuss tricky prepositions. (T-Ss).
  ], "S / T-Ss"),

  stage("SIX", "Post-task", "8", "To provide freer practice and personalize the topic", [
    - *Part 1: Roleplay*: Pairs choose a situation from Exercise 6 (e.g., getting to the theater or beach from the bus station). (Ss-Ss).
    - *Part 2: Create*: Ss write a short dialogue using the map and the new navigation phrases.
    - *Perform*: Selected pairs act out their dialogue for the class while others trace the route on the map. (T-Ss).
  ], "Ss-Ss / T-Ss"),
))
