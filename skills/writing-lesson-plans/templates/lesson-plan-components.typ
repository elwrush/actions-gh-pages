// ============================================================
// LESSON PLAN COMPONENTS LIBRARY
// Bell Language Centre - Standard Template
// ============================================================
// Usage: #import "lesson-plan-components.typ": *

// BRAND COLORS
#let maroon = rgb("#A62D26")
#let light-maroon = rgb("#cb5c55")
#let pale-pink = rgb("#fceceb")

// ==========================================
// 1. HEADER STRAP
// ==========================================

#let lesson_header(lesson_type) = {
  // lesson_type: "bell" or "intensive"
  image("../../../images/" + lesson_type + "-header.jpg", width: 100%)
  v(0.5cm)
}

// ==========================================
// 2. METADATA TABLE
// ==========================================

#let metadata_table(data) = {
  table(
    columns: (1fr, 2fr, 1fr, 2fr),
    stroke: 0.5pt + gray,
    fill: (x, y) => if calc.even(x) { pale-pink } else { white },
    inset: 8pt,
    [*Teacher:*], data.teacher, [*Date:*], data.date,
    [*CEFR Level:*], data.cefr, [*Duration:*], data.duration,
    [*Lesson Shape:*], data.shape, [*Assessment:*], data.assessment,
    [*Main Focus:*], data.focus, [*Materials:*], data.materials,
  )
}

// ==========================================
// 3. MAIN AIM BOX
// ==========================================

#let main_aim_box(text_content) = {
  block(
    width: 100%,
    fill: maroon,
    inset: 10pt,
    text(fill: white, weight: "bold")[Main Aim: #text_content],
  )
}

// ==========================================
// 4. DIFFERENTIATION / PEDAGOGICAL NOTE
// ==========================================

#let differentiation_box(content) = {
  block(
    width: 100%,
    stroke: 2pt + maroon,
    inset: 15pt,
    [
      #text(weight: "bold", fill: maroon, size: 11pt)[Differentiated Input]
      #v(0.3em)
      #text(size: 9.5pt, style: "italic")[Pedagogical Rationale: Differentiated Input & Learner Autonomy \ #content]
    ],
  )
}

// ==========================================
// 5. STAGE TABLE
// ==========================================

#let stage_table(stages) = {
  let slate-dark = rgb("#334155")

  table(
    columns: (10%, 15%, 1fr, 10%),
    stroke: 0.5pt + gray,
    fill: (x, y) => {
      if calc.even(y) { pale-pink } else { white }
    },
    inset: 8pt,
    align: (x, y) => if x == 0 or x == 3 { center } else { left },

    table.header(
      table.cell(fill: slate-dark, text(fill: white, weight: "bold", hyphenate: true)[*Time*]),
      table.cell(fill: slate-dark, text(fill: white, weight: "bold", hyphenate: true)[*Goal*]),
      table.cell(fill: slate-dark, text(fill: white, weight: "bold", hyphenate: true)[*Procedure*]),
      table.cell(fill: slate-dark, text(fill: white, weight: "bold", hyphenate: true)[*Int*]),
    ),

    ..stages.flatten(),
  )
}

// ==========================================
// 6. ANSWER KEY FOOTER
// ==========================================

#let answer_key(content) = {
  v(1cm)
  block(
    width: 100%,
    stroke: (top: 2pt + maroon),
    inset: (top: 10pt),
    [
      #text(weight: "bold", fill: maroon, size: 11pt)[Answer Key:]
      #v(0.3em)
      #content
    ],
  )
}

// ==========================================
// 7. TRANSCRIPT SECTION (for listening)
// ==========================================

#let transcript_section(content) = {
  pagebreak()
  v(0.5cm)
  block(
    width: 100%,
    stroke: (top: 2pt + maroon, bottom: 2pt + maroon),
    inset: (y: 10pt),
    [
      #text(weight: "bold", fill: maroon, size: 11pt)[Listening Transcript:]
    ],
  )
  v(0.5cm)
  text(size: 9.5pt)[#content]
}

// ==========================================
// 8. SLIDESHOW LINK BOX
// ==========================================

#let slideshow_link(url) = {
  v(0.5cm)
  block(
    width: 100%,
    fill: rgb("#EFF6FF"), // Light blue background
    stroke: 1.5pt + rgb("#2563EB"), // Blue border
    inset: 12pt,
    radius: 4pt,
    [
      #grid(
        columns: (30pt, 1fr),
        align: (center + horizon, left + horizon),
        // Icon (simplified SVG-like shape for presentation)
        text(size: 20pt, fill: rgb("#2563EB"))[📊],
        [
          #text(weight: "bold", size: 11pt, fill: rgb("#1E40AF"))[CLICK LINK FOR SLIDESHOW] \
          #v(0.2em)
          #link(url)[#underline(text(fill: rgb("#2563EB"))[#url])]
        ]
      )
    ]
  )
  v(0.5cm)
}

// ==========================================
// 9. STAGE HELPER (for consistent formatting)
// ==========================================

#let stage(number, name, time, goal, procedure, interaction) = {
  (
    // Stage title row (spans all columns)
    table.cell(
      colspan: 4,
      fill: maroon,
      text(fill: white, weight: "bold", hyphenate: true)[STAGE #number: #name],
    ),
    // Data row
    [#time Min],
    goal,
    procedure,
    [#interaction],
  )
}
