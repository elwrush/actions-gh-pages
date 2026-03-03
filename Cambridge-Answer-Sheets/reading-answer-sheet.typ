#set page(
  paper: "a4",
  margin: (x: 2cm, y: 1.5cm),
)
#set text(font: "Segoe UI", size: 11pt)

// Header Strap
#block(
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

#v(1.0cm)

// Student Info
#box(width: 100%)[
  #set text(size: 12pt)
  #strong[Class:] #box(width: 5cm, stroke: (bottom: 1pt))[#h(1fr)]
  #h(2cm)
  #strong[ID:] #box(width: 5cm, stroke: (bottom: 1pt))[#h(1fr)]
]

#v(0.5cm)

// Title
#align(center)[
  #text(size: 18pt, weight: "bold")[B1 Reading Examination]
]

#v(0.5cm)

// Answer Grid (32 Questions)
#grid(
  columns: (1fr, 1fr),
  column-gutter: 1.5cm,
  block(width: 100%, table(
    columns: (40pt, 1fr),
    rows: (28pt), // Slightly reduced row height to fit 16 rows per column comfortably
    stroke: 0.5pt,
    inset: 0pt,
    align: (center + horizon, left + horizon),
    fill: (x, y) => if x == 0 { gray.lighten(80%) },
    ..for i in range(1, 17) {
      (strong[#i], [])
    }
  )),
  block(width: 100%, table(
    columns: (40pt, 1fr),
    rows: (28pt),
    stroke: 0.5pt,
    inset: 0pt,
    align: (center + horizon, left + horizon),
    fill: (x, y) => if x == 0 { gray.lighten(80%) },
    ..for i in range(17, 33) {
      (strong[#i], [])
    }
  ))
)
