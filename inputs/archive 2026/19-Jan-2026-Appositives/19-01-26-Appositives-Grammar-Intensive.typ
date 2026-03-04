
// ============================================================
// B1 GRAMMAR: APPOSITIVES - THE ART OF PRECISION
// ============================================================

#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 2cm, x: 2cm),
)
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.8em, justify: true)

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let line-dark = rgb("#333333") // Standard dark gray for lines

// ==========================================
// 1. COMPONENTS
// ==========================================

#let intensive_header() = {
  // Printer-safe: centered with top padding
  // No massive negative dy; let it sit naturally with a slight upward nudge for better balance
  v(-0.5cm)
  align(center)[
    #block(width: 105%, image("/images/intensive-header.jpg"))
  ]
  v(0.4cm)
}

#let identity_block() = {
  block(width: 100%, inset: (bottom: 0.4em), [
    #grid(
      columns: (auto, 1fr, auto, 4cm),
      gutter: 1em,
      text(weight: "bold", fill: maroon)[Name:],
      line(start: (0pt, 0.8em), length: 100%, stroke: 0.5pt + black),
      text(weight: "bold", fill: maroon)[Student ID:],
      grid(
        columns: (1fr, 1fr, 1fr, 1fr, 1fr),
        gutter: 4pt,
        ..range(5).map(_ => box(width: 100%, height: 1.2em, stroke: (bottom: 1pt + black)))
      ),
    )
  ])
}

#let rule_box(title, body) = {
  table(
    columns: 100%,
    fill: rgb("#F8FAFC"),
    stroke: 0.5pt + maroon,
    inset: 12pt,
    align: left,
    [
      #text(weight: "bold", fill: maroon, size: 12pt)[#title] \
      #v(0.2em)
      #body
    ]
  )
}

#let writing_lines(count: 15) = {
  v(0.4cm)
  for _ in range(count) {
    line(length: 100%, stroke: 0.5pt + line-dark)
    v(0.6cm)
  }
}

// ==========================================
// 2. CONTENT
// ==========================================

#intensive_header()

#align(center)[
  #text(size: 22pt, weight: "black", fill: maroon)[APPOSITIVES] \
  #text(size: 14pt, style: "italic", fill: slate-dark)[:: THE ART OF PRECISION ::]
]

#v(0.6cm)

#grid(
  columns: (1fr, 6cm),
  gutter: 1.5cm,
  [
    #text(weight: "bold", size: 13pt)[Task 1: The Master's Detail] \
    #v(0.4em)
    Read the following description of a famous artist. Notice how the text provides extra information about the people and things mentioned.

    #block(stroke: (left: 2pt + maroon), inset: (left: 10pt), [
      *Leonardo da Vinci*, a master of the Italian Renaissance, was more than just a painter. He was an inventor, an engineer, and a visionary. His most famous work, *the Mona Lisa*, sits in the Louvre Museum in Paris. Leonardo often kept notebooks, leather-bound volumes filled with sketches and ideas, to record his observations of the natural world. His great rival, *Michelangelo*, also worked in Italy during this period.
    ])

    #v(0.6cm)
    #text(weight: "bold", size: 11pt)[Instructions:] \
    Underline the phrases that provide extra information about the *bold* subjects.
  ],
  [
    #align(center + horizon)[
      #image("mona_lisa_clean.png", width: 100%)
      #v(0.4em)
      #text(size: 9pt, fill: slate-dark, style: "italic")[Precision in the Master's Work.]
    ]
  ],
)

#v(0.6cm)

#rule_box("The Logic of Appositives: Reduced Relative Clauses", [
  An appositive is a #strong[reduced relative clause]. We remove the relative pronoun (#emph[who/which]) and the verb (#emph[to be]) for a more sophisticated rhythm.

  #grid(
    columns: (1fr, 1fr),
    gutter: 1cm,
    [
      #strong[Mid-Sentence:] \
      #text(style: "italic", size: 10pt)[My brother, #strong[a master chef], lives in Bangkok.]
    ],
    [
      #strong[End-Sentence:] \
      #text(style: "italic", size: 10pt)[I live with my brother, #strong[a master chef].]
    ],
  )

  #v(0.4em)
  *Why use them?*
  - #strong[Position:] They can sit mid-sentence (surrounded by commas) or at the end (following a single comma).
  - #strong[Style:] It removes the "clutter" of unnecessary words to create a faster, professional flow.
])

#pagebreak()


#block(breakable: false)[
  #text(weight: "bold", size: 13pt)[Task 2: The Architect's Grid] \
  #v(0.4em)
  Combine the following sentences into one using an appositive. Follow the example.
]

#v(0.2cm)
*Example:* My teacher is Mr. Smith. He is a local marathon runner. \
*Result:* My teacher, a local marathon runner, is Mr. Smith.

#v(0.2cm)
1. The capital of Thailand is Bangkok. It is a bustling metropolis. \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + line-dark)
2. My favorite book is 'The Hobbit'. It is a classic fantasy novel. \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + line-dark)
3. Serena Williams is a world-renowned tennis player. She has won 23 Grand Slam titles. \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + line-dark)
4. My cousin is a pilot. He flies for Thai Airways. \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + line-dark)
5. The durian is a distinctive fruit. It is known for its strong smell. \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + line-dark)
6. Albert Einstein was a brilliant physicist. He developed the theory of relativity. \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + line-dark)
7. Tokyo is the capital of Japan. It is the largest city in the world. \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + line-dark)

#v(0.4cm)

#pagebreak()


#block(breakable: false)[
  #text(weight: "bold", size: 13pt)[Task 3: Production] \
  #v(0.4em)
  Describe a place or a person you find fascinating (#strong[Target: 70+ words]). You must use at least #emph[three appositives] to add precision and detail to your writing.
]

#v(0.4cm)

#writing_lines(count: 16)

#pagebreak()
#text(weight: "bold", size: 14pt, fill: maroon)[Answer Key]
#v(1em)

*Task 1:*
- a master of the Italian Renaissance (refers to Leonardo da Vinci)
- the Mona Lisa (refers to his most famous work)
- leather-bound volumes filled with sketches and ideas (refers to notebooks)
- Michelangelo (refers to his great rival)

*Task 2 (Answers may vary):*
1. Bangkok, a bustling metropolis, is the capital of Thailand.
2. My favorite book, a classic fantasy novel, is 'The Hobbit'.
3. Serena Williams, a world-renowned tennis player, has won 23 Grand Slam titles.
4. My cousin, a pilot, flies for Thai Airways.
5. The durian, a distinctive fruit, is known for its strong smell.
6. Albert Einstein, a brilliant physicist, developed the theory of relativity.
7. Tokyo, the capital of Japan, is the largest city in the world.
