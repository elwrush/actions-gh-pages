
// ============================================================
// B1 GRAMMAR: THE SENTENCE GATEWAY (STOPPING THE INFINITE FLOW)
// ============================================================

#set page(
  paper: "a4",
  margin: (top: 1.25cm, bottom: 1.5cm, x: 2cm),
)
#set text(font: "Arial", size: 10.5pt, fill: rgb("#333333"))
#set par(leading: 0.6em, justify: true)

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#666666")

// ==========================================
// 1. COMPONENTS
// ==========================================

#let integrated_header() = {
  block(
    width: 100%,
    height: 1.2cm,
    fill: maroon,
    inset: (left: 0.8cm, right: 1cm),
    align(horizon + left)[
      #stack(
        dir: ltr,
        spacing: 1.25em,
        image("/images/ACT_transparent.png", height: 0.6cm),
        image("/images/Bell.png", height: 0.6cm),
        h(0.2cm),
        text(fill: white, size: 9.5pt, weight: "bold", tracking: 0.05em)[
          BELL LANGUAGE CENTRE #h(0.5em) | #h(0.5em) THE GRAMMAR REPAIR SHOP
        ],
      )
    ],
  )
  v(0.3cm)
}

#let target_box(number, title) = {
  block(
    width: 100%,
    fill: rgb("#F8FAFC"),
    radius: 4pt,
    inset: 10pt,
    stroke: 0.5pt + maroon,
    [
      #text(weight: "bold", fill: maroon, size: 10.5pt)[Repair Target #number: #title]
      #v(1.6cm)
      #line(length: 100%, stroke: 0.5pt + maroon)
    ],
  )
}

#let exercise_item(n, text_content) = {
  grid(
    columns: (25pt, 1fr),
    gutter: 10pt,
    align(right)[#text(weight: "bold", fill: maroon, size: 11pt)[#n.]],
    block(width: 100%, inset: (bottom: 0.35cm), [
      #text(size: 11pt)[#text_content]
      #v(0.7cm)
      #line(length: 100%, stroke: 0.5pt + gray-line)
    ])
  )
}

// ==========================================
// 2. DOCUMENT LAYOUT
// ==========================================

#integrated_header()

#text(size: 18pt, weight: "bold", fill: maroon)[Task 1: Your Feedback Review]
#v(0.1cm)
#text[Look at the feedback from your previous writing. What are the three most important 'Sentence Boundaries' you need to fix today?]

#v(0.4cm)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 12pt,
  target_box(1, "Comma Splice"),
  target_box(2, "Fused Sentence"),
  target_box(3, "The Infinite 'And'"),
)

#v(1.2cm)

#text(size: 18pt, weight: "bold", fill: maroon)[Task 2: The Grammar Crime Scene]

#v(0.3cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 25pt,
  [
    #text(weight: "bold", size: 11pt)[Mystery 1: The Comma Splice] \
    #v(0.2em)
    #text(size: 9.5pt, style: "italic", fill: slate-dark)[Aunna: "I agree that fear often stops people from achieving what they want to, Fear of failure..."]
    #v(0.4em)
    #block(fill: rgb("#FFF5F5"), inset: 8pt, radius: 4pt, width: 100%, stroke: (left: 2.5pt + maroon))[
      *The Fix:* Use a *Full Stop* and a *Capital Letter*. A comma is too weak.
    ]
  ],
  [
    #text(weight: "bold", size: 11pt)[Mystery 2: The Fused Sentence] \
    #v(0.2em)
    #text(size: 9.5pt, style: "italic", fill: slate-dark)[Fergie: "I was secondary 2 my teacher needs a volunteer for an english competition"]
    #v(0.4em)
    #block(fill: rgb("#FFF5F5"), inset: 8pt, radius: 4pt, width: 100%, stroke: (left: 2.5pt + maroon))[
      *The Fix:* Two separate facts need a wall between them. Add a full stop.
    ]
  ]
)

#v(0.8cm)

#grid(
  columns: (1.2fr, 0.8fr),
  gutter: 1.5cm,
  [
    #text(size: 15pt, weight: "bold", fill: maroon)[The "Infinite Because" Flow] \
    #v(0.3cm)
    #text[Students often write 40 words without a stop. In Thai, thoughts flow like a river. In English, we need to **Stop, Breathe, and Start again.**]
    #v(0.4cm)
    #block(fill: rgb("#F1F5F9"), inset: 10pt, radius: 4pt, stroke: (left: 2.5pt + slate-dark))[
      #text(size: 9.5pt, fill: slate-dark)[
        "I agree that fear stops people... #strong[because] sometimes fear makes us feel scared #strong[because] I think my grammar is not very good #strong[and] I think others did better."
      ]
    ]
    #v(0.3cm)
    #text(weight: "bold", fill: maroon, size: 10pt)[Rule: One 'because' is okay. Two is too many. Stop!]
  ],
  [
    #align(center + horizon)[
      #image("out_of_breath.png", width: 90%)
    ]
  ]
)

#pagebreak()

#text(size: 18pt, weight: "bold", fill: maroon)[Task 3: The Big Fix (7 Repairs)]
#v(0.3cm)
#text[Find the "invisible walls" between thoughts. Add the Full Stop (.) and the Big Letter (Capital) where they are missing.]

#v(0.6cm)

#exercise_item(1, "I am so tired I want to go to bed.")
#exercise_item(2, "She is very kind, everyone likes her.")
#exercise_item(3, "My friend lives in London, mean while I live in Bangkok.")
#exercise_item(4, "We went to the mall we bought some new shoes for the party.")
#exercise_item(5, "I agree with the statement because fear can stop us from doing things and it makes us feel small and we lose our confidence.")
#exercise_item(6, "The movie was extremely long, therefore many people left before the end.")
#exercise_item(7, "Success takes risk because without risk you cannot grow, failure is just a lesson.")

#v(1fr)

#align(center)[
  #text(style: "italic", size: 8.5pt, fill: gray-line)[© 2026 Bell Language Centre | English Program Grammar Workshop]
]
