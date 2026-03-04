
// ==========================================
// BUSINESS VOCABULARY: INTENSIVE VERSION
// ==========================================

#import "/skills/generating-worksheets/templates/intensive_worksheet_template.typ": (
  answer_key_header, identity_block, intensive_header, task_header, writing_lines,
)

#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 2cm, x: 2cm),
)

// FONTS & COLORS
#let main-font = ("Times New Roman", "serif")
#let head-font = ("Arial", "sans-serif")
#let maroon = rgb("#8B1538")
#let slate = rgb("#334155")
#let light-bg = rgb("#F8FAFC")

#set text(font: main-font, size: 11pt, fill: slate)
#set par(leading: 0.65em, justify: true)

// COMPONENTS
#let section_header(title) = {
  block(width: 100%, fill: maroon, inset: (x: 8pt, y: 4pt), radius: 2pt, below: 0.8em)[
    #text(font: head-font, weight: "bold", size: 12pt, fill: white)[#title]
  ]
}

#let language_help_box(content) = {
  block(width: 100%, below: 1em, breakable: false)[
    #stack(
      dir: ltr,
      rect(fill: slate, inset: (x: 8pt, y: 4pt), radius: (top: 4pt), stroke: none, text(
        font: head-font,
        weight: "bold",
        size: 10pt,
      )[
        #text(fill: white)[Language] #text(fill: rgb("#2DD4BF"))[help]
      ]),
      h(1fr),
    )
    #v(-6pt)
    #block(
      width: 100%,
      inset: 8pt,
      stroke: 2pt + rgb("#2DD4BF"),
      radius: (bottom: 4pt, top-right: 4pt),
      fill: white,
      content,
    )
  ]
}

#let tablet_ui(content) = {
  block(
    width: 100%,
    fill: rgb("#F1F5F9"),
    radius: 6pt,
    stroke: 1pt + rgb("#CBD5E1"),
    [
      #block(fill: slate, width: 100%, inset: 6pt, radius: (top: 6pt), [
        #grid(
          columns: (auto, 1fr, auto),
          text(fill: white, weight: "bold", size: 14pt)[≡],
          align(center)[#text(fill: white, weight: "bold", size: 10pt, font: head-font)[MORGAN & STENSON]],
          text(fill: white, size: 10pt)[🔍],
        )
      ])
      #block(inset: 12pt, content)
    ],
  )
}

#let q_line(content) = {
  content
  v(0.6cm)
  line(length: 100%, stroke: (paint: rgb("#4D4D4D"), thickness: 0.5pt, dash: "dotted"))
  v(0.4cm)
}

// ==========================================
// DOCUMENT
// ==========================================

#intensive_header()
#identity_block()

#align(center)[
  #text(size: 18pt, weight: "bold", fill: maroon)[Business Vocabulary: From Local to Global]
]

#v(0.5cm)

// --- SECTION 1: READING ---
#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  [
    #section_header("A. Denham Farm Bakery")
    #image("baker_bespoke.jpg", width: 100%, height: 4cm, fit: "cover")
    #v(0.2cm)
    #text(fill: maroon, weight: "bold")[DENHAM FARM BAKERY] is a family business, with three different generations working with a team of 90 employees.

    The company was *set up* in 1991 with the *aim* of producing a *variety* of bread of the highest *quality*. They soon became *experts* in the field.

    The company is *run* from a factory in Ilminster and the *firm* has *expanded* a *great deal*.
  ],
  [
    #section_header("B. Morgan & Stenson")
    #tablet_ui[
      They were *formerly* Stenson & Son, but were *taken over* by JS Morgan. James Morgan took up the *position* of senior partner. The *headquarters* are in Newcastle, but they have five other *branches*.

      James has many *contacts* in the football world, so many of his *clients* are athletes. It was his *ambition* to change the *image* of accountants.
    ]
    #v(0.2cm)
    #language_help_box[
      *Achievement*: Something successful that needed effort. \
      *Former/Ex*: Ex-wife, but former president. \
      *Customer/Client*: Shops have customers; lawyers have clients.
    ]
  ],
)

#v(0.5cm)

// --- SECTION 2: TASKS ---
#task_header(1, "Synonyms & Definitions")
#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  [
    #q_line[1. Delivered #underline[every day] (d........)]
    #q_line[2. A real #underline[need] for quality (d........)]
    #q_line[3. Our #underline[plan] is to open (a...)]
    #q_line[4. The #underline[company] is well (f...)]
    #q_line[5. We have 25 #underline[workers] (e........)]
  ],
  [
    #q_line[6. I #underline[started] the business (s... u.)]
    #q_line[7. Their #underline[main offices] (h..........)]
    #q_line[8. Hoping for a #underline[job] (p.......)]
    #q_line[9. It is #underline[getting bigger] (e........)]
    #q_line[10. Made #underline[a lot] of money (a g.... d...)]
  ],
)

#pagebreak()
#intensive_header()

#task_header(2, "Language Precision")
#columns(2)[
  1. Experts *in / on* farming.
  2. *Set up / take up* tennis?
  3. Famous *clients / customers*.
  4. My *ex- / former* wife.
  5. *Set up / take up* the firm?
  6. Serving a *client / customer*.
  7. *Currently / actually* working.
  8. *Take up / take over* the firm?
  9. *Former / ex-* president.
]

#v(1cm)

#task_header(3, "Sentence Reconstruction")
#block(fill: light-bg, inset: 1cm, radius: 4pt, width: 100%)[
  1. He makes different cakes. *VARIETY*
  #writing_lines(count: 1)

  2. They were very successful. *ACHIEVE*
  #writing_lines(count: 1)

  3. I know a lot of people in banking. *CONTACTS*
  #writing_lines(count: 1)

  4. They used to be called BMG. *FORMERLY*
  #writing_lines(count: 1)

  5. I've always wanted to fly a plane. *AMBITION*
  #writing_lines(count: 1)
]

#v(1cm)
#answer_key_header()
*Task 1*: 1. daily, 2. demand, 3. aim, 4. firm, 5. employees, 6. set up, 7. headquarters, 8. position, 9. expanding, 10. a great deal. \
*Task 2*: 1. in, 2. take up, 3. clients, 4. ex-, 5. set up, 6. customer, 7. currently, 8. take over, 9. former. \
*Task 3*: 1. Variety of cakes, 2. Achieved a great deal, 3. Contacts in banking, 4. Formerly known as, 5. Ambition to fly.
