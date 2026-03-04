
// ============================================================
// THE STRATEGIC WRITER: B1 ARTICLE MASTERCLASS
// 4-PAGE LINEAR LAYOUT (CLEAN & ACCURATE)
// ============================================================

#set page(
  paper: "a4",
  margin: (top: 1cm, bottom: 2cm, x: 2cm),
)
#set text(font: "Arial", size: 12pt, fill: rgb("#333333"))
#set par(leading: 0.8em, justify: true)

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#E0E0E0")
#let ref-bg = rgb("#F8FAFC")
#let toolkit-bg = rgb("#FFF1F2")

// ==========================================
// 1. COMPONENTS
// ==========================================

// HEADER STRAP
#let intensive_header() = {
  align(center)[
    #image("../../images/intensive-header.jpg", width: 100%)
  ]
  v(0.6cm)
}

// TASK TAB BOX
#let task_tab(number, title, color: maroon) = {
  block(
    width: 100%,
    stroke: 1.5pt + color,
    radius: 4pt,
    clip: true,
    below: 0.8cm,
    [
      #block(fill: color, width: 100%, inset: 10pt, [
        #text(fill: white, weight: "bold", size: 14pt)[TASK #number: #title]
      ])
    ],
  )
}

// IDENTITY BLOCK
#let identity_block() = {
  block(width: 100%, inset: (bottom: 1em), [
    #grid(
      columns: (auto, 1fr, auto, 4cm),
      gutter: 1em,
      text(weight: "bold", fill: maroon)[Nickname:],
      line(start: (0pt, 0.8em), length: 100%, stroke: 0.5pt + black),
      text(weight: "bold", fill: maroon)[ID:],
      grid(
        columns: (1fr, 1fr, 1fr, 1fr, 1fr),
        gutter: 4pt,
        ..range(5).map(_ => box(width: 100%, height: 1.2em, stroke: (bottom: 1pt + black)))
      ),
    )
  ])
}

// WRITING LINES
#let writing_lines(count: 15) = {
  v(0.2cm)
  for _ in range(count) {
    line(length: 100%, stroke: 0.5pt + slate-dark)
    v(0.65cm)
  }
}

// B2 MODEL STAMP
#let b2_stamp() = {
  box(
    stroke: 2pt + maroon,
    inset: 8pt,
    radius: 4pt,
    [#text(weight: "bold", fill: maroon, size: 11pt)[TOTAL SCORE: 20/20 (B2 LEVEL)]],
  )
}

// ==========================================
// 2. DOCUMENT CONTENT
// ==========================================

// --- PAGE 1: COVER ---
#intensive_header()

#align(center)[
  #v(3cm)
  #text(size: 24pt, weight: "bold", fill: maroon)[THE B1 WRITER]
  #v(0.5cm)
  #text(size: 16pt, weight: "bold")[Cambridge PET Article Workshop]
]

#v(3cm)
#identity_block()

// --- PAGE 2: TASK 1 (ANALYSIS) ---
#pagebreak()

#task_tab("1", "ANALYZING THE MODEL")

#text(weight: "bold", fill: maroon)[THE ORIGINAL PROMPT:]
#v(0.2cm)
#block(width: 100%, inset: 12pt, fill: ref-bg, stroke: 1pt + gray-line, radius: 4pt)[
  #text(weight: "bold")[Articles wanted!] \
  #text(weight: "bold", size: 14pt)[WHAT MAKES YOU LAUGH?] \
  Write an article telling us what makes you laugh and why. Is it important for people to laugh? \
  The best articles will be published in next month’s magazine.
]

#v(0.5cm)
#b2_stamp()
#v(0.3cm)

#block(
  width: 100%,
  stroke: (left: 4pt + maroon),
  inset: (left: 12pt),
  [
    #text(style: "italic", size: 11pt)[
      #text(fill: maroon, weight: "bold")[[Part 1]] "I love to watch comedies a lot because it makes me laugh. #text(weight: "bold", fill: maroon)[The comedy I love the most is the Chinese Running Man.] I enjoy watching and laughing it with my family."
      #v(0.5em)
      #text(fill: maroon, weight: "bold")[[Part 2]] "#text(weight: "bold", fill: maroon)[In the show, famous actors and actresses must overcome some challenging quests, such as trading a coffee bean with someone else for something more expensive...] The storylines are very interesting and they always tickle my funny bone. Laughing out loud is great!"
      #v(0.5em)
      #text(fill: maroon, weight: "bold")[[Part 3]] "Laughing can help us to release stress and make us feel better. #text(weight: "bold", fill: maroon)[It may also make us more attractive too!]"
    ]
  ],
)

#v(0.8cm)
#text(weight: "bold", fill: maroon)[CONTENT CHECKLIST:]
#v(0.5em)
- #text(weight: "bold")[Part 1]: Did they say *what* makes them laugh? (Yes: Chinese Running Man).
- #text(weight: "bold")[Part 2]: Did they say *why* it makes them laugh? (Yes: Actors overcoming challenges).
- #text(weight: "bold")[Part 3]: Did they say if it's *important*? (Yes: Releases stress/more attractive).

// --- PAGE 3: TASK 2 (PLANNING) ---
#pagebreak()

#task_tab("2", "PLANNING YOUR RESPONSE")

#text[Before you start writing, plan your ideas for the main body paragraph (Paragraph 2).]

#v(0.5cm)

#block(width: 100%, stroke: 1pt + slate-dark, radius: 4pt, [
  #block(fill: slate-dark, width: 100%, inset: 8pt, [
    #text(fill: white, weight: "bold")[TOPIC SENTENCE (The Main Idea)]
  ])
  #v(2cm)
])

#v(0.5cm)

#grid(
  columns: 1fr,
  gutter: 0.5cm,
  block(width: 100%, stroke: 1pt + slate-dark, radius: 4pt, [
    #block(fill: maroon, width: 100%, inset: 8pt, [
      #text(fill: white, weight: "bold")[SUPPORTING DETAILS (Give examples and evidence)]
    ])
    #v(6cm)
  ]),
)

#v(0.5cm)
#block(width: 100%, stroke: 0.5pt + maroon, inset: 12pt, radius: 4pt, [
  #text(weight: "bold", fill: maroon)[THE FINAL CHECK:]
  #v(0.5em)
  - Have you answered all THREE parts of the question?
  - Have you used connecting words (e.g., *because, such as, furthermore*)?
  - Have you used modals (e.g., *could, may, might*) to give opinions?
])

// --- PAGE 4: TASK 3 (PRODUCTION) ---
#pagebreak()

#task_tab("3", "WRITING YOUR ARTICLE")

#text(weight: "bold", fill: maroon)[THE EXAM TASK:]
#v(0.2cm)
#block(width: 100%, inset: 12pt, fill: ref-bg, stroke: 1pt + gray-line, radius: 4pt)[
  #text(weight: "bold")[Articles wanted!] \
  #text(weight: "bold", size: 14pt)[TECHNOLOGY AND YOU] \
  Write an article telling us which website or app you like the most and how often you use it. Do you think it is important for teenagers to have a computer? Why? \
  The best articles will be published in next month’s magazine.
]

#v(0.5cm)
#block(width: 100%, fill: toolkit-bg, inset: 10pt, radius: 4pt, [
  #text(weight: "bold", fill: maroon)[WRITING TOOLBOX:]
  #v(0.4em)
  #text(size: 10pt)[
    - *Expressing Preference*: "The app I use most frequently is..." / "I am particularly fond of..."
    - *Giving Opinion*: "I strongly believe that..." / "In my view, computers are essential because..."
    - *Adding Detail*: "Furthermore, they allow us to..." / "For instance, students can..."
  ]
])

#v(0.4cm)
#writing_lines(count: 12)

#v(1fr)
#align(center)[#text(size: 9pt, fill: slate-dark)[Bell Language Centre | Intensive Program | 2026]]
