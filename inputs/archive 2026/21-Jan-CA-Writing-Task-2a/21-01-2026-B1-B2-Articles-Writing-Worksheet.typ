
// ============================================================
// WRITING DEVELOPMENT WORKSHEET: ARTICLES (B1/B2)
// 4-PAGE BOOKLET VERSION
// ============================================================

#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 2cm, x: 2cm),
)
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 1em, justify: false)

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#666666")
#let light-bg = rgb("#F8FAFC")

// ==========================================
// 1. COMPONENTS
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
        image("/images/ACT_transparent.png", height: 0.75cm),
        image("/images/Bell.svg", height: 0.75cm),
        h(0.2cm),
        text(fill: white, size: 11pt, weight: "bold", tracking: 0.05em)[
          BELL LANGUAGE CENTRE
        ],
      )
    ],
  )
  v(0.2cm)
  line(length: 100%, stroke: 1.5pt + maroon)
  v(0.6cm)
}

// BOLD GRADIENT HEADER
#let title_banner() = {
  v(0.4cm)
  stack(
    dir: ltr,
    spacing: 12pt,
    // Stronger Accent: Stacked circles
    stack(
      dir: ttb,
      spacing: 3pt,
      circle(radius: 6pt, fill: maroon),
      circle(radius: 6pt, fill: rgb("#FCD34D")),
      circle(radius: 6pt, fill: slate-dark),
    ),
    // Headline with gradient
    [
      #text(
        fill: gradient.linear(maroon, rgb("#5B0A1F"), angle: 45deg),
        size: 32pt,
        weight: 900,
        font: "Arial",
        tracking: 0.02em,
      )[WRITING ARTICLES]
      #v(-0.5cm)
      #text(fill: slate-dark, size: 11pt, weight: "bold", tracking: 0.25em)[IMAGINATION & STRUCTURE]
    ],
  )
  v(0.6cm)
  line(length: 100%, stroke: 2pt + maroon)
  v(0.8cm)
}

// SECTION HEADER
#let section_header(title) = {
  block(width: 100%, fill: light-bg, inset: 10pt, radius: 4pt, stroke: 1pt + gray-line, [
    #text(weight: "bold", fill: maroon, size: 12pt)[#title]
  ])
  v(0.5cm)
}

// CHECKBOX
#let checkbox(label) = {
  box(height: 12pt, width: 12pt, stroke: 1pt + maroon, radius: 2pt)
  h(0.5em)
  text(size: 11pt)[#label]
}

// ==========================================
// PAGE 1: DECONSTRUCTION & ANALYSIS
// ==========================================
#integrated_header("Analysis & Strategy")
#title_banner()

#section_header("Task 1: Deconstructing the Model")

#text(
  style: "italic",
)[Refer to the model article *"What Makes You Laugh?"*. Locate and analyze the following features. This structure will be the skeleton for your own article.]

#v(0.5cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  block(width: 100%, height: auto, inset: 10pt, stroke: (left: 2pt + maroon), [
    *1. The Hook (Introduction)*
    #v(0.5em)
    Find the *Rhetorical Question*.
    #v(0.5em)
    #line(length: 100%, stroke: 0.5pt + gray-line)
    #v(0.5em)
    *Why does this work?*
    #v(2cm)
    #line(length: 100%, stroke: 0.5pt + gray-line)
  ]),
  block(width: 100%, height: auto, inset: 10pt, stroke: (left: 2pt + maroon), [
    *2. The Connection (Style)*
    #v(0.5em)
    Find 2 examples of *Direct Address* ("you/we").
    #v(0.5em)
    #line(length: 100%, stroke: 0.5pt + gray-line)
    #v(0.5em)
    #line(length: 100%, stroke: 0.5pt + gray-line)
    #v(0.5em)
    #line(length: 100%, stroke: 0.5pt + gray-line)
  ]),
)

#v(0.5cm)

// MODEL TEXT DISPLAY
#block(
  fill: rgb("#F0F9FF"), // Light Blue background
  stroke: (left: 4pt + rgb("#0284C7")),
  radius: (top-right: 4pt, bottom-right: 4pt),
  inset: 15pt,
  width: 100%,
  [
    #grid(
      columns: (auto, 1fr),
      gutter: 10pt,
      align(center + horizon)[
        #circle(radius: 12pt, fill: rgb("#0284C7"))[#text(fill: white, weight: "bold", size: 14pt)[?]]
      ],
      [
        #text(weight: "bold", fill: rgb("#0C4A6E"), size: 12pt)[Model Text: What Makes You Laugh?]
        #v(0.5em)
        #text(size: 11pt, style: "italic")[
          "Are you looking for a laugh? I love to watch comedies a lot because it makes me laugh. The comedy I love the most is the Chinese Running Man. I enjoy watching and laughing it with my family. In the show, famous actors and actresses must overcome some challenging quests... The storylines are very interesting and they always tickles my funny bone. Laughing out loud is great! Laughing can help us to release stress and make us feel better. It may also make us more attractive too!"
        ]
      ],
    )
  ],
)

#v(1cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  block(width: 100%, height: auto, inset: 10pt, stroke: (left: 2pt + maroon), [
    *3. The Opinion (Content)*
    #v(0.5em)
    Find phrases showing *Strong Opinion* ("I love...", "My favorite...").
    #v(0.5em)
    #line(length: 100%, stroke: 0.5pt + gray-line)
    #v(0.5em)
    #line(length: 100%, stroke: 0.5pt + gray-line)
  ]),
  block(width: 100%, height: auto, inset: 10pt, stroke: (left: 2pt + maroon), [
    *4. The Glue (Cohesion)*
    #v(0.5em)
    Find 2 *Linking Words* (e.g., because, such as).
    #v(0.5em)
    #line(length: 100%, stroke: 0.5pt + gray-line)
    #v(0.5em)
    #line(length: 100%, stroke: 0.5pt + gray-line)
  ]),
)

#v(1fr)

// ==========================================
// PAGE 2 FLOW: LANGUAGE TOOLS
// ==========================================
#block(breakable: false)[
  #section_header("Task 2: Vocabulary Upgrade")
  #grid(
    columns: (1fr, 1fr),
    gutter: 1cm,
    block(stroke: 1pt + maroon, radius: 4pt, inset: 15pt, width: 100%, height: auto)[
      #text(weight: "bold", fill: maroon)[Describing Articles (Standard)] \
      *Use for B1 Track*
      #v(0.5em)
      - Hilarious
      - Gripping
      - Dull
      - Heartwarming
      #v(1em)
      #line(length: 100%, stroke: 0.5pt + gray-line)
      #v(1em)
      #line(length: 100%, stroke: 0.5pt + gray-line)
    ],
    block(stroke: 1pt + maroon, radius: 4pt, inset: 15pt, width: 100%, height: auto)[
      #text(weight: "bold", fill: maroon)[Challenge (Advanced / B2)] \
      *Use for Describing Complexity*
      #v(0.5em)
      - Intricate Plot
      - One-dimensional (Char)
      - Poignant / Moving
      - Clichéd
      #v(1em)
      #line(length: 100%, stroke: 0.5pt + gray-line)
      #v(1em)
      #line(length: 100%, stroke: 0.5pt + gray-line)
    ],
  )
]

#v(1cm)

#block(breakable: false)[
  #section_header("Task 3: The Hook Strategy")
  #grid(
    columns: (1fr, 1fr),
    gutter: 1cm,
    [
      *Standard (B1): The Question* \
      Ask the reader something personal to grab attention.
      #v(0.5em)
      *Ex*: "Do you like reading articles?"
    ],
    [
      *Advanced (B2): The Scene/Drama* \
      Drop the reader into the middle of the action or make a bold statement.
      #v(0.5em)
      *Ex*: "It was past midnight when I finally put the book down."
    ],
  )
  #v(0.5cm)
  *Draft your improved opening sentence here:*
  #v(1cm)
  #line(length: 100%, stroke: 0.5pt + slate-dark)
  #v(1.5cm)
  #line(length: 100%, stroke: 0.5pt + slate-dark)
]

// ==========================================
// PAGE 3 FLOW: THE BLUEPRINT
// ==========================================
#block(breakable: false)[
  #section_header("Task 4: Article Plan")
  #block(fill: rgb("#FFF9C4"), inset: 15pt, radius: 4pt, width: 100%)[
    *Differentiation Check - Which track are you on?*
    #v(0.5em)
    #checkbox("B1 Standard Track: Focus on the article topic and basic details.") \
    #v(0.5em)
    #checkbox("B2 Advanced Track: Focus on *why* it is unusual, describe the material, and explain.")
  ]
]

#v(0.5cm)

// WRITING TASK QUESTIONS
#grid(
  columns: (1fr, 1fr),
  gutter: 0.8cm,
  block(
    stroke: (left: 3pt + rgb("#0284C7")),
    fill: rgb("#F0F9FF"),
    inset: 12pt,
    radius: (top-right: 4pt, bottom-right: 4pt),
  )[
    #text(weight: "bold", fill: rgb("#0C4A6E"), size: 11pt)[B1 Writing Task]
    #v(0.3em)
    #text(weight: "bold", size: 10pt)[Articles wanted: Your favorite stories!]
    #v(0.3em)
    #text(
      size: 9pt,
    )[Write an article telling us what you like to read the most: books, manga, comics, or something else?]
    #v(0.3em)
    #text(size: 9pt)[• Do you think it's good to read a lot? Why?]
    #v(0.3em)
    #text(size: 8pt, style: "italic")[The best articles will be published next month.]
  ],
  block(
    stroke: (left: 3pt + rgb("#7C3AED")),
    fill: rgb("#F5F3FF"),
    inset: 12pt,
    radius: (top-right: 4pt, bottom-right: 4pt),
  )[
    #text(weight: "bold", fill: rgb("#5B21B6"), size: 11pt)[B2 Writing Task]
    #v(0.3em)
    #text(weight: "bold", size: 10pt)[Articles wanted: Unusual Stories!]
    #v(0.3em)
    #text(size: 9pt)[We're looking for articles about unusual material you have read: books, mangas, or anything else.]
    #v(0.3em)
    #text(size: 9pt)[• Have you, or a friend, ever read anything that you thought was really unusual?]
    #v(0.2em)
    #text(size: 9pt)[• Describe the reading material and explain why it was so unusual.]
    #v(0.3em)
    #text(size: 8pt, style: "italic")[The best articles will be published in our next issue.]
  ],
)

#v(0.5cm)

#block(stroke: 1pt + maroon, radius: 4pt, inset: 20pt, width: 100%)[
  #align(center)[#text(size: 14pt, weight: "bold", fill: maroon)[MY PLAN]]
  #v(0.4cm)

  *Title:* #box(width: 1fr, repeat(".", gap: 2pt))
  #v(0.6cm)

  *Paragraph 1: Introduction*
  #grid(
    columns: (auto, 1fr),
    gutter: 0.5em,
    row-gutter: 1.2em,
    [• Name of Article / Subject:], box(width: 1fr, repeat(".", gap: 2pt)),
    [• Genre / Type:], box(width: 1fr, repeat(".", gap: 2pt)),
    [• Hook Strategy:], box(width: 1fr, repeat(".", gap: 2pt)),
  )
  #v(1cm)

  *Paragraph 2: The Core Description*
  #grid(
    columns: (auto, 1fr),
    gutter: 0.5em,
    row-gutter: 1.2em,
    [• The Place (B1) / Description (B2):], box(width: 1fr, repeat(".", gap: 2pt)),
    [], box(width: 1fr, repeat(".", gap: 2pt)),
    [• Why? (Detail / Reason):], box(width: 1fr, repeat(".", gap: 2pt)),
    [], box(width: 1fr, repeat(".", gap: 2pt)),
  )
  #v(1cm)

  *Paragraph 3: The Assessment*
  #grid(
    columns: (auto, 1fr),
    gutter: 0.5em,
    row-gutter: 1.2em,
    [• Comparison / Uniqueness:], box(width: 1fr, repeat(".", gap: 2pt)),
    [], box(width: 1fr, repeat(".", gap: 2pt)),
    [• Supporting Idea:], box(width: 1fr, repeat(".", gap: 2pt)),
    [], box(width: 1fr, repeat(".", gap: 2pt)),
  )
  #v(1cm)

  *Conclusion*
  #grid(
    columns: (auto, 1fr),
    gutter: 0.5em,
    row-gutter: 1.2em,
    [• Final thought:], box(width: 1fr, repeat(".", gap: 2pt)),
  )
]

// ==========================================
// PAGE 4 FLOW: SUCCESS CRITERIA
// ==========================================
#block(breakable: false)[
  #section_header("Task 5: Final Checklist")
  #v(0.5cm)
  #grid(
    columns: (1fr, 1fr),
    gutter: 1cm,
    block(fill: light-bg, inset: 15pt, radius: 4pt)[
      #text(weight: "bold", fill: maroon)[B1 Checklist]
      #v(0.5em)
      #checkbox("~100 words")
      #v(0.5em)
      #checkbox("Answered 3 questions")
      #v(0.5em)
      #checkbox("Used paragraphs")
      #v(0.5em)
      #checkbox("Used linking words")
    ],
    block(fill: light-bg, inset: 15pt, radius: 4pt)[
      #text(weight: "bold", fill: maroon)[B2 Checklist]
      #v(0.5em)
      #checkbox("140-190 words")
      #v(0.5em)
      #checkbox("Detailed description")
      #v(0.5em)
      #checkbox("Complex vocabulary")
      #v(0.5em)
      #checkbox("Engaging style (hook)")
    ],
  )
]

#v(1cm)

#text(weight: "bold")[Peer Feedback Notes:]

#v(0.5cm)
#line(length: 100%, stroke: 0.5pt + slate-dark)
#v(1.5cm)
#line(length: 100%, stroke: 0.5pt + slate-dark)
#v(1.5cm)
#line(length: 100%, stroke: 0.5pt + slate-dark)
#v(1.5cm)
#line(length: 100%, stroke: 0.5pt + slate-dark)
