
// ==========================================
// BUSINESS VOCABULARY: DESIGN V9 (COMPLETE)
// ==========================================

#set page(
  paper: "a4",
  margin: (top: 1cm, bottom: 1.5cm, x: 1.5cm),
)

// FONTS & COLORS
#let main-font = ("Times New Roman", "serif")
#let head-font = ("Arial", "sans-serif")
#let maroon = rgb("#8B1538")
#let maroon-light = rgb("#C4564F")
#let slate = rgb("#334155")
#let amber = rgb("#F59E0B")
#let teal = rgb("#0F766E") // Added for Language Help box style
#let light-bg = rgb("#F8FAFC")

#set text(font: main-font, size: 11pt, fill: slate)
#set par(leading: 0.65em, justify: true)

// ==========================================
// COMPONENTS
// ==========================================

#let bell_header() = {
  align(center)[
    #image("../../images/bell-header.jpg", width: 100%)
  ]
  v(0.2cm)
}

#let cinematic_title() = {
  block(
    width: 100%,
    height: 4cm, // Reduced height
    radius: 4pt,
    clip: true,
    stroke: 1pt + maroon,
    [
      #place(image("header_banner.jpg", width: 100%, height: 100%, fit: "cover"))
      #block(width: 100%, height: 100%, fill: maroon.transparentize(20%))
      #place(center + horizon)[
        #text(
          size: 11pt,
          fill: white.transparentize(20%),
          weight: "bold",
          tracking: 0.2em,
          font: head-font,
        )[THE JOURNEY]
        #v(0.05cm)
        #text(size: 28pt, fill: white, weight: "black", tracking: 0.05em, font: head-font)[FROM LOCAL TO GLOBAL]
      ]
    ],
  )
}

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
    #v(-6pt) // Overlap slightly
    #block(
      width: 100%,
      inset: 8pt,
      stroke: 2pt + rgb("#2DD4BF"), // Teal border to match image
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

#let writing_lines(count) = {
  for _ in range(count) {
    v(0.85cm) // Reduced from 1.2cm
    line(length: 100%, stroke: (paint: rgb("#404040"), thickness: 1pt, dash: "dotted"))
  }
}

#let q_line(content) = {
  content
  v(1cm)
  line(length: 100%, stroke: (paint: rgb("#404040"), dash: "dotted"))
  v(0.5cm)
}

// ==========================================
// DOCUMENT
// ==========================================

// --- PAGE 1: READING ---
#bell_header()
#cinematic_title()
#v(0.5cm)

// 2-Column Layout for Texts
#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,

  // COL 1: BAKERY
  [
    #section_header("A. The Local Success")
    #image("baker_bespoke.jpg", width: 100%, height: 4cm, fit: "cover")
    #v(0.2cm)
    #text(fill: maroon, weight: "bold")[DENHAM FARM BAKERY] is a family business, with three different generations working with a team of 90 employees.

    The company was *set up* in 1991 with the *aim* of producing a *variety* of bread of the highest *quality*. The Denham family saw there was a growing *demand* for organic products, and they soon became *experts* in the field.

    The company is *run* from a factory in Ilminster, where the bread is baked *daily* and *delivered* to shops. The *firm* has *expanded* a *great deal*, but it remains a family business.

    #v(0.2cm)
    #language_help_box[
      If you *achieve* something, you have been successful in something that needed a lot of work and effort. The noun is *achievement*, e.g. _Writing a book has been my greatest achievement._
    ]
  ],

  // COL 2: CORPORATE
  [
    #section_header("B. The Corporate View")
    #tablet_ui[
      Morgan & Stenson are a firm of *accountants*. They were *formerly* Stenson & Son, but were *taken over* by JS Morgan five years ago. James Morgan took up the *position* of senior partner. The *headquarters* are in Newcastle, but they have five other *branches*.

      James Morgan is a former owner of a football club, with many *contacts* in the football world, so many of his *clients* are footballers. Last year the company attracted *attention* when it advertised on TV. It was his *ambition* to change the *image* of accountants.
    ]
    #v(0.2cm)
    #language_help_box[
      We usually talk about an *ex-*wife/boyfriend, but a *former* president/career/banker. \
      Shops and organisations have *customers*; lawyers, accountants have *clients*. \
      We *take up* a job or activity, but we *set up* a company.
    ]
  ],
)

// --- PAGE 2: EXERCISES ---
#pagebreak()
#section_header("Vocabulary Practice")
#v(0.2cm)

// TASK 1: COMPACT GRID
#text(weight: "bold", fill: maroon)[Task 1: People & Roles]
#h(1em)
#text(size: 10pt)[Tick (✓) the words which refer to people.]
#v(0.2cm)
#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr),
  gutter: 8pt,
  ..("headquarters", "accountant", "employee", "quality", "branches").map(x => box(
    stroke: 1pt + gray,
    inset: 5pt,
    radius: 3pt,
    width: 100%,
    align(center)[#x],
  )),
  ..("client", "expert", "contacts", "bakery", "variety").map(x => box(
    stroke: 1pt + gray,
    inset: 5pt,
    radius: 3pt,
    width: 100%,
    align(center)[#x],
  ))
)

#v(0.5cm)
#line(length: 100%, stroke: 0.5pt + maroon.lighten(50%))
#v(0.5cm)

// TASK 2: DENSE COLUMNS
#text(weight: "bold", fill: maroon)[Task 2: Synonyms]
#h(1em)
#text(size: 10pt)[Replace the underlined word(s) with a word or phrase that has a similar meaning.]
#v(0.2cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  [
    #q_line[1. Delivered #underline[every day].]
    #q_line[2. Real #underline[need] for quality.]
    #q_line[3. Our #underline[plan] is to open.]
    #q_line[4. The #underline[company] is well.]
    #q_line[5. We have 25 #underline[workers].]
  ],
  [
    #q_line[6. I #underline[started] the business.]
    #q_line[7. Their #underline[main offices].]
    #q_line[8. Hoping for a #underline[job].]
    #q_line[9. It is #underline[getting bigger].]
    #q_line[10. Made #underline[a lot] of money.]
  ],
)

#v(0.5cm)
#line(length: 100%, stroke: 0.5pt + maroon.lighten(50%))
#v(0.5cm)

// TASK 3: INLINE CHOICE
#text(weight: "bold", fill: maroon)[Task 3: Word Choice]
#v(0.2cm)
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

// --- PAGE 3: PRODUCTION ---
#pagebreak()
#section_header("Writing Production")
#v(0.2cm)

#text(weight: "bold", fill: maroon)[Task 4: Rewrite the sentence using the word in bold.]
#v(0.3cm)

#block(fill: light-bg, inset: 1cm, radius: 4pt, width: 100%)[
  1. He makes different cakes. *VARIETY*
  #writing_lines(1)

  2. They were very successful. *ACHIEVE*
  #writing_lines(1)

  3. I know a lot of people in banking. *CONTACTS*
  #writing_lines(1)

  4. They used to be called BMG. *FORMERLY*
  #writing_lines(1)

  5. I've always wanted to fly a plane. *AMBITION*
  #writing_lines(1)

  6. She has a great knowledge of finance. *EXPERT*
  #writing_lines(1)

  7. People noticed the adverts. *ATTRACT*
  #writing_lines(1)
]

#v(0.5cm)

// TASK 5: GAP FILL (Ex 39.5)
#block(
  fill: rgb("#F0FDF4"), // Green-50
  stroke: (left: 4pt + rgb("#15803D")), // Green-700
  inset: 12pt,
  radius: 4pt,
  width: 100%,
  [
    #text(weight: "bold", fill: rgb("#15803D"))[Task 5: Success Story (Gap Fill)]
    #par(leading: 1.8em)[ // Increased leading for writing space
      Daniela set up her courier service (DCS) in 1979. If you wanted to send documents across London, she promised to #box(width: 1.5cm, stroke: (bottom: 1pt + black)) them in less than an hour. It was only a small #box(width: 1.5cm, stroke: (bottom: 1pt + black)), but DCS #box(width: 1.5cm, stroke: (bottom: 1pt + black)) immediate success.

      Daniela soon set up another #box(width: 1.5cm, stroke: (bottom: 1pt + black)) in Manchester, which was #box(width: 1.5cm, stroke: (bottom: 1pt + black)) by her brother. The business soon #box(width: 1.5cm, stroke: (bottom: 1pt + black)) rapidly, and it is now her #box(width: 1.5cm, stroke: (bottom: 1pt + black)) to have a branch in every major city.
    ]
  ],
)


// --- PAGE 4: KEY ---
#pagebreak()
#text(size: 16pt, weight: "bold", fill: maroon)[Answer Key]
#v(0.5cm)

#grid(
  columns: (1fr, 1fr, 1fr),
  [
    *Task 1* \
    accountant \ employee \ client \ expert \ contacts
  ],
  [
    *Task 2* \
    1. daily \ 2. demand \ 3. aim \ 4. firm/business \ 5. employees \ 6. set up \ 7. headquarters \ 8. position \ 9. expanding \ 10. a great deal
  ],
  [
    *Task 3* \
    *Task 3* \
    1. in \ 2. take up \ 3. clients \ 4. ex- \ 5. set up \ 6. customer \ 7. currently \ 8. take over \ 9. former
  ],
)

#v(0.5cm)
*Task 4: Rewrites* \
1. He makes a variety of cakes. \
2. They achieved a great deal. \
3. I have many contacts in banking. \
4. They were formerly known as BMG. \
5. It's my ambition to fly a plane. \
6. She is an expert in finance. \
7. The adverts attracted a lot of attention.

#v(0.5cm)
*Task 5: Success Story* \
1. deliver, 2. firm/business, 3. achieved, 4. branch, 5. run, 6. expanded, 7. ambition
