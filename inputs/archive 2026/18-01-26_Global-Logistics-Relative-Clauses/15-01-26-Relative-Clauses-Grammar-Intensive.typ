
// ============================================================
// INTENSIVE WORKSHEET: RELATIVE CLAUSES (B1 Grammar)
// ============================================================
// Topic: The Bountiful Harvest
// Based on Gold Standard Template (v13)
// ============================================================

#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 2.5cm, x: 2cm),
)
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.8em, justify: true)

// Meander removed for simplicity

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#E0E0E0")
#let intensive-bg = rgb("#F8FAFC")

// ==========================================
// 1. COMPONENTS
// ==========================================

// INTENSIVE HEADER BLOCK
// INTENSIVE HEADER BLOCK
#let intensive_header() = {
  block(
    width: 100%,
    [
      #image("/images/intensive-header.jpg", width: 100%)
    ],
  )
  v(0.3cm)
}

// TASK HEADER
#let task_header(number, title) = {
  v(0.8cm)
  block(width: 100%, [
    #text(weight: "bold", fill: maroon, size: 14pt)[TASK #number: #title]
    #v(0.2cm)
    #line(length: 100%, stroke: 1.5pt + maroon)
    #v(0.4cm)
  ])
}

// WRITING LINES (Intensive Quality Standard)
#let writing_lines(count: 10) = {
  v(1.5cm) // Initial gap before lines
  for _ in range(count) {
    line(length: 100%, stroke: 0.5pt + gray)
    v(1.5cm) // Double spacing for corrections (1.5cm as per quality standards)
  }
}

// ==========================================
// 2. DOCUMENT CONTENT
// ==========================================

// --- PAGE 1 ---
#intensive_header()

#align(center)[
  #text(size: 24pt, weight: "bold", fill: maroon, font: "Georgia")[THE BOUNTIFUL HARVEST] \
  #text(size: 14pt, style: "italic", fill: slate-dark)[Exploring Relative Clauses in Agriculture]
]

#v(0.5cm)

#text(weight: "bold", fill: maroon, size: 13pt)[Grammar Focus: Relative Clauses] \
We use relative clauses to describe or give extra information about an *object*, *person*, or *place*. This allows us to combine two ideas into one sophisticated sentence, which is essential for B1 level communication.

#v(0.6em)

#table(
  columns: (auto, auto, 1fr),
  fill: (x, y) => if y == 0 { maroon.lighten(90%) },
  stroke: 0.5pt + gray-line,
  inset: 8pt,
  [*Pronoun*], [*Used for...*], [*Example*],
  [*who*], [People], [Farmers *who* sell in local markets often earn more.],
  [*that / which*], [Things], [Crops *which* grow in Turkey include citrus fruits.],
  [*where*], [Places], [The farm *where* I grew up grows pomegranates.],
)

#v(0.8em)
#text(weight: "bold")[Defining vs. Non-defining] \
Defining clauses give *essential* information (no commas). Non-defining clauses give *extra* information and must be surrounded by *commas*.
_Example (ND):_ Pomegranates, which are delicious, are rich in vitamins.

#task_header(1, "IDENTIFY & CLASSIFY")
#text(style: "italic")[Underline the relative clause. Decide if it is Defining (D) or Non-Defining (ND).]

#v(0.4cm)

#let t1_items = (
  "Common foods which are grown in this country include wheat, fruit, and vegetables.",
  "Farmers who sell in the local market always sell seasonal crops.",
  "Crumble, which is an English dessert, is made from fruit, flour, sugar, and butter.",
  "The area on the coast, where many farmers are based, is good for growing crops.",
  "The food stall owners, who work in this area, must have a license.",
  "The town where I lived as a teenager is famous for its hot and spicy food.",
)

#stack(
  dir: ttb,
  spacing: 0.4cm,
  ..t1_items
    .enumerate()
    .map(((i, item)) => grid(
      columns: (auto, 1fr, auto),
      gutter: 1em,
      [#text(weight: "bold")[#(i + 1).]],
      [#item],
      [#box(width: 1.5cm, height: 1.2em, stroke: (bottom: 1pt + slate-dark), baseline: 0.2em)],
    )),
)


#v(0.4cm)

#task_header(2, "FILL THE GAPS")
#text(style: "italic")[Complete the sentences with *who*, *which / that*, or *where*.]

#v(0.6cm)

// GAPFILL COMPONENT (Local Definition for immediate stability)
#let gapfill_exercise(items, placeholder: "__", line_length: 2.5cm) = {
  stack(
    dir: ttb,
    spacing: 0.4cm,
    ..items
      .enumerate()
      .map(((i, item)) => {
        let parts = item.split(placeholder)
        let content = parts
          .intersperse(
            box(width: line_length, height: 1em, stroke: (bottom: 0.5pt + black), baseline: 0.2em),
          )
          .join()
        grid(
          columns: (auto, 1fr),
          gutter: 1em,
          text(weight: "bold")[#(i + 1).], content,
        )
      }),
  )
}

#let t2_items = (
  "People __ lived in the countryside were given a small piece of land to farm.",
  "In the past, people lived __ it was easy to grow their own food.",
  "The new kinds of food __ are popular nowadays are usually processed.",
  "The food __ we eat in my country is usually imported.",
  "In hot and dry places __ there is little rain, it is hard to grow food.",
  "People living in the city, __ are usually richer, do not eat as much fruit.",
)

#gapfill_exercise(t2_items)

#task_header(3, "SENTENCE JOINING")
#text(style: "italic")[Join the sentences using a relative clause after the subject.]

#v(0.6cm)

// SINGLE SENTENCE WRITING COMPONENT (Local Definition)
#let single_sentence_writing(items, vertical_space: 1.2cm) = {
  stack(
    dir: ttb,
    spacing: 1cm,
    ..items
      .enumerate()
      .map(((i, item)) => block(width: 100%, [
        #text(weight: "bold")[#(i + 1). #item] \
        #v(vertical_space)
        #line(length: 100%, stroke: 0.5pt + gray)
      ])),
  )
}

#let t3_items = (
  "The people mostly eat fish. They live on small islands.",
  "Bottled water is more expensive than gas. It comes from other countries.",
  "The dish comes from the north. It is made from rice, fish, herbs, and spices.",
  "The places are in the center of the country. They eat more meat.",
)

#single_sentence_writing(t3_items)

#pagebreak()
#v(0.4cm)

#task_header(4, "PERSONAL WRITING")
#text(weight: "bold", fill: maroon)[THE CHALLENGE:] \
#text[Write a paragraph (50-70 words) about your *favourite food*. You must include at least *two relative clauses* (e.g. "Pizza, which is Italian, is my favourite...").]

#writing_lines(count: 8)

#v(1fr)

#block(
  width: 100%,
  stroke: 1pt + maroon,
  inset: 12pt,
  radius: 4pt,
  fill: intensive-bg,
  [
    #text(weight: "bold", fill: maroon)[Self-Correction Radar:]
    #h(1em)
    #box(width: 10pt, height: 10pt, stroke: 1pt + maroon, radius: 2pt, baseline: 25%) #h(4pt) Two relative clauses?
    #h(1.2em)
    #box(width: 10pt, height: 10pt, stroke: 1pt + maroon, radius: 2pt, baseline: 25%) #h(4pt) Correct use of commas (for ND)?
    #h(1.2em)
    #box(width: 10pt, height: 10pt, stroke: 1pt + maroon, radius: 2pt, baseline: 25%) #h(4pt) Spelt 'pomegranate' correctly?
  ],
)

#pagebreak()
#intensive_header()
#text(weight: "bold", size: 16pt, fill: maroon)[ANSWER KEY]

#v(1cm)
*Task 1:* 1. which... (D) | 2. who... (D) | 3. , which... (ND) | 4. , where... (ND) | 5. , who... (ND) | 6. where... (D) \
*Task 2:* 1. who | 2. where | 3. which/that | 4. which/that | 5. where | 6. who \
*Task 3:*
1. The people who live on small islands mostly eat fish.
2. Bottled water, which comes from other countries, is more expensive than gas.
3. The dish, which is made from rice, fish, herbs, and spices, comes from the north.
4. The places which are in the center of the country eat more meat.
