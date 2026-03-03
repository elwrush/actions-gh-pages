#import "../lib/typst/lib.typ": *

#set page(
  paper: "a4",
  margin: (x: 2cm, y: 1.5cm),
)
#set text(font: "Segoe UI", size: 11pt)

// Header Strap
#let header_strap = block(
  width: 100%,
  stroke: (bottom: 2pt + black),
  inset: (bottom: 10pt),
  grid(
    columns: (auto, 1fr),
    gutter: 0.8cm,
    align: horizon,
    image("../images/ACT.png", width: 2.2cm),
    stack(
      spacing: 4pt,
      text(size: 17pt, weight: "bold")[Assumption College Thonburi Language Centre],
      text(size: 14pt, weight: "bold", fill: gray.darken(40%))[Mathayom Program],
    )
  )
)

// Student Info
#let student_info = box(width: 100%)[
  #set text(size: 12pt)
  #strong[Class:] #box(width: 5cm, stroke: (bottom: 1pt))[#h(1fr)]
  #h(2cm)
  #strong[ID:] #box(width: 5cm, stroke: (bottom: 1pt))[#h(1fr)]
]

// --- PAGE 1 ---
#header_strap
#v(0.8cm)
#student_info
#v(0.5cm)

#align(center)[
  #text(size: 18pt, weight: "bold")[B1 Writing Examination]
]

#v(0.5cm)

#text(size: 14pt, weight: "bold")[Question 1] \
#text(style: "italic")[You must answer this question.]

#writing_lines_dynamic(line-spacing: 1cm)

// --- PAGE 2 ---
#pagebreak()
#student_info
#v(0.5cm)

#text(size: 14pt, weight: "bold")[Question 2] \
#text(style: "italic")[Answer ONE of the questions in this section.]

#writing_lines_dynamic(line-spacing: 1cm)

