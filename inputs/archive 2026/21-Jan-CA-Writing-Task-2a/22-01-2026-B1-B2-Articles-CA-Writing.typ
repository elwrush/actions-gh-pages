// ============================================================
// CA WRITING TASK: ARTICLES (B1/B2)
// 3-PAGE LINED WORKSHEET - CAMBRIDGE STYLE
// ============================================================

#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 2cm, x: 2cm),
)
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let gray-line = rgb("#666666")

// ==========================================
// COMPONENTS
// ==========================================

// PAGE HEADER (INTEGRATED STRAP)
#let integrated_header(subtitle) = {
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
        image("../../images/ACT_transparent.png", height: 0.75cm),
        image("../../images/Bell.svg", height: 0.75cm),
        h(0.2cm),
        text(fill: white, size: 11pt, weight: "bold", tracking: 0.05em)[
          BELL LANGUAGE CENTRE
        ],
      )
    ],
  )
  v(0.2cm)
  line(length: 100%, stroke: 1.5pt + maroon)
  v(0.5cm)
}

// --- DYNAMIC SPACE FILLING (Typst 0.11+) ---
#let line-spacing = 1.1cm // Adjusted for 2-up print scaling (A5 effective size)
#let rule-line = line(length: 100%, stroke: 0.5pt + gray-line)

#let fill-space-with-lines(available-height) = {
  let count = int(available-height / line-spacing)
  if count > 0 {
    stack(
      spacing: line-spacing,
      ..range(count).map(_ => rule-line),
    )
  }
}

// ==========================================
// PAGE 1: B1 WRITING TASK
// ==========================================
#integrated_header("CA Writing Task")

#align(center)[
  #text(size: 14pt, weight: "bold", fill: maroon)[B1 WRITING TASK]
  #v(0.2cm)
  #text(size: 11pt, weight: "bold")[TIME: 20 MINUTES | TARGET: ~100 WORDS]
]

#v(0.5cm)

#text(weight: "bold", size: 11pt)[Articles wanted: Your favorite stories!]

#v(0.3cm)

#text(size: 11pt)[Write an article telling us what you like to read the most: books, manga, comics, or something else?]

#v(0.2cm)

#text(size: 11pt)[• Do you think it's good to read a lot? Why?]

#v(0.3cm)

#text(size: 11pt, style: "italic")[The best articles answering these questions will be published next month.]

#v(0.6cm)

#text(
  size: 10pt,
)[Name: #box(width: 4cm, line(length: 100%, stroke: 0.5pt + gray-line)) #h(0.5cm) Class: #box(width: 3cm, line(length: 100%, stroke: 0.5pt + gray-line)) #h(0.5cm) ID: #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line)) #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line)) #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line)) #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line)) #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line))]

#v(0.4cm)

#text(weight: "bold", size: 10pt)[Your Article:]

#context {
  let current-pos = here().position()
  let available = page.height - page.margin.bottom - current-pos.y
  let buffer = 0.5cm
  v(buffer)
  fill-space-with-lines(available - buffer)
}

// ==========================================
// PAGE 2: B2 WRITING TASK
// ==========================================
#pagebreak()

#integrated_header("CA Writing Task")

#align(center)[
  #text(size: 14pt, weight: "bold", fill: maroon)[B2 WRITING TASK]
  #v(0.2cm)
  #text(size: 11pt, weight: "bold")[TIME: 20 MINUTES | TARGET: 140-190 WORDS]
]

#v(0.5cm)

#text(weight: "bold", size: 11pt)[Articles wanted: Unusual Stories!]

#v(0.3cm)

#text(size: 11pt)[We're looking for articles about unusual material you have read: books, mangas, or anything else.]

#v(0.2cm)

#text(size: 11pt)[• Have you, or a friend, ever read anything that you thought was really unusual?]

#v(0.2cm)

#text(size: 11pt)[• Tell us about it – describe the reading material and explain why it was so unusual.]

#v(0.3cm)

#text(size: 11pt, style: "italic")[The best articles will be published in our next issue.]

#v(0.6cm)

#text(
  size: 10pt,
)[Name: #box(width: 4cm, line(length: 100%, stroke: 0.5pt + gray-line)) #h(0.5cm) Class: #box(width: 3cm, line(length: 100%, stroke: 0.5pt + gray-line)) #h(0.5cm) ID: #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line)) #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line)) #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line)) #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line)) #box(width: 0.8cm, line(length: 100%, stroke: 0.5pt + gray-line))]

#v(0.4cm)

#text(weight: "bold", size: 10pt)[Your Article:]

#context {
  let current-pos = here().position()
  let available = page.height - page.margin.bottom - current-pos.y
  let buffer = 0.5cm
  v(buffer)
  fill-space-with-lines(available - buffer)
}

// ==========================================
// PAGE 3: B2 CONTINUATION
// ==========================================
#pagebreak()

#layout(size => {
  fill-space-with-lines(size.height)
})
