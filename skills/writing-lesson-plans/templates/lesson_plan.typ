
// ==========================================
// LESSON PLAN TEMPLATE (TYPST) - V2
// ==========================================
#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 1.5cm, x: 2cm),
)
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.6em, justify: true)

// Colors
#let maroon = rgb("#8B1538")
#let gray-light = rgb("#F8FAFC")
#let gray-line = rgb("#DDDDDD")

// --- INTEGRATED STRAP HEADER (Synced with Worksheet) ---
#let header(title, teacher, date, duration, level) = {
  block(
    width: 100%,
    height: 1.5cm,
    fill: maroon,
    inset: (left: 0.8cm, right: 1cm),
    radius: 0pt,
    align(horizon + left)[
      #stack(
        dir: ltr,
        spacing: 1.25em,
        image("/images/ACT_transparent.png", height: 0.75cm),
        image("/images/Bell.svg", height: 0.75cm),
        h(0.2cm),
        text(fill: white, size: 10.5pt, weight: "bold", tracking: 0.05em)[
          BELL LANGUAGE CENTRE #h(0.5em) | #h(0.5em) #title
        ],
      )
    ],
  )
  v(0.2cm)
  grid(
    columns: (1fr, auto),
    text(style: "italic", fill: maroon, weight: "bold", size: 9pt)[Lesson Plan: Writing Skills],
    text(fill: rgb("#666666"), size: 8pt)[#teacher | #date | #duration | #level],
  )
  v(0.2cm)
  line(length: 100%, stroke: 1.5pt + maroon)
  v(0.5cm)
}

// --- DIFFERENTIATION BOX ---
#let differentiation_box(body) = {
  block(
    fill: rgb("#fff1f2"),
    stroke: 1pt + maroon,
    inset: 12pt,
    radius: 4pt,
    width: 100%,
    [
      #text(weight: "bold", fill: maroon, size: 11pt)[DIFFERENTIATION]
      #v(0.4em)
      #text(size: 9.5pt, style: "italic")[#body]
    ],
  )
  v(0.5cm)
}

// --- METADATA BOX ---
#let metadata(objective, materials, assessment) = {
  block(
    fill: gray-light,
    inset: 10pt,
    radius: 4pt,
    width: 100%,
    stroke: 0.5pt + gray-line,
    [
      #text(weight: "bold", fill: maroon)[Objective:] #objective
      #v(0.5em)
      #text(weight: "bold", fill: maroon)[Materials:] #materials
      #v(0.5em)
      #text(weight: "bold", fill: maroon)[Assessment:] #assessment
    ],
  )
  v(0.5cm)
}

// --- STAGE TABLE ---
#let stage_row(number, name, aim, procedure, time, interaction) = {
  table(
    columns: 1fr,
    fill: maroon,
    inset: 6pt,
    align(center)[#text(fill: white, weight: "bold", size: 9pt)[STAGE #number: #name]]
  )
  table(
    columns: (8%, 20%, 52%, 10%, 10%),
    inset: 8pt,
    stroke: 0.5pt + gray-line,
    align(center + horizon)[#number],
    [#text(size: 9pt)[#aim]],
    [#text(size: 9pt)[#procedure]],
    align(center + horizon)[#text(size: 9pt)[#time min]],
    align(center + horizon)[#text(size: 9pt)[#interaction]],
  )
}

// ==========================================
// CONTENT
// ==========================================

#header(
  "THE GRAMMAR REPAIR SHOP",
  "Ed Rush",
  "12 Jan 26",
  "46 mins",
  "B1 (Mixed A2-B2)",
)

#differentiation_box[
  This lesson plan specifically references the concept of differentiation that was the subject of the recent INSETT in the following ways. Firstly, students have not received generalised feedback about their writing, but tailored feedback which identifies each student's own particular grammatical errors as identified by Cambridge University's ERRor ANnotation Toolkit (ERRANT). Second, students will not engage in a generalised follow-up writing task, but instead will choose a writing task that is graded to align to their current level of grammatical proficiency.
]

#metadata(
  "By the end of the lesson, learners will be better able to self-correct their own specific grammatical errors while producing a levelled writing task.",
  "Tailored Cambridge ERRANT Feedback Reports (Individual), Differentiated Worksheet (V13)",
  "Production of CEFR-leveled writing task with targeted self-correction.",
)

#text(size: 14pt, weight: "bold", fill: maroon)[Lesson Procedure]
#v(0.5em)

// STAGE 1
#stage_row(
  "1",
  "The Tailored Diagnostic",
  "To distribute and frame personalized feedback data",
  [
    *Receiving the Data*
    - T frames the lesson: "Today isn't about general grammar. It's about YOUR grammar."
    - Hand out individual **Cambridge ERRANT** feedback reports.
    - Ss read their specific "Error Profile" (e.g., Satang seeing his Article and Preposition errors).
  ],
  "7",
  "T-Ss / Indiv",
)

// STAGE 2
#stage_row(
  "2",
  "Repair Target Selection",
  "To prioritize specific errors for immediate repair",
  [
    *Setting the Menu*
    - Ss look at Page 1 of the Worksheet.
    - Ss select their "Top 3 Repair Targets" from their report and write them in the target boxes.
    - T circulates to check that targets are specific (not just "Grammar").
  ],
  "8",
  "Indiv",
)

// STAGE 3
#stage_row(
  "3",
  "Levelled Task Selection",
  "To align challenge with proficiency",
  [
    *Choosing the Path*
    - T explains the 3 levels of writing tasks (A2, B1, B2).
    - Ss turn to the page matching their assessed level.
    - Brief "Dot-Dash" planning in the margin to structure content before writing.
  ],
  "6",
  "T-Ss",
)

// STAGE 4
#stage_row(
  "4",
  "The Repair Shop (Drafting)",
  "To produce writing with active self-monitoring",
  [
    *Drafting with Radar Monitoring*
    - Ss write their descriptive paragraphs.
    - **CRITICAL:** Ss must use the "Self-Correction Radar" at the top of the page to check their work *as they write*.
    - T monitors specifically for the "Repair Targets" identified in Stage 2.
  ],
  "15",
  "Indiv",
)

// STAGE 5
#stage_row(
  "5",
  "Quality Control (Peer Review)",
  "To practice collaborative error detection",
  [
    *Differentiated Peer Review*
    - Ss swap papers.
    - Peers check the "Radar" points. Did the writer fix what they said they would?
    - Peer circle-marking (focusing *only* on the 3 targets).
  ],
  "5",
  "Ss-Ss",
)

// STAGE 6
#stage_row(
  "6",
  "Checkout",
  "To consolidate the correction habit",
  [
    *Reflection*
    - "Which of your 3 targets did you find easiest to fix?"
    - Collect worksheets and reports.
  ],
  "5",
  "T-Ss",
)
