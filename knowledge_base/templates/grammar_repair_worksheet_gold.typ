
// ============================================================
// GOLD STANDARD TEMPLATE: GRAMMAR REPAIR WORKSHEET (V13)
// ============================================================
// Structure:
// - Page 1: Diagnostic/Target Identification
// - Pages 2-4: CEFR-specific Writing Tasks (A2, B1, B2)
// Styling:
// - Integrated Maroon branding strap (Printer safe)
// - Enlarged logos (Bell SVG, ACT PNG)
// - 1.5 Line spacing for writing areas
// - Strict 1-page-per-level (15 line limit)
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
#let gray-line = rgb("#E0E0E0")

// ==========================================
// 1. COMPONENTS
// ==========================================

// PAGE 1 HEADER (GAP STYLE - INTEGRATED STRAP)
#let integrated_header() = {
  // 1. Integrated Branding Strap (Inside margins for printer safety)
  block(
    width: 100%,
    height: 1.5cm, // Enlarged for visual impact
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
        text(fill: white, size: 10.5pt, weight: "bold", tracking: 0.05em)[
          BELL LANGUAGE CENTRE #h(0.5em) | #h(0.5em) THE GRAMMAR REPAIR SHOP
        ],
      )
    ],
  )

  v(0.2cm)
  line(length: 100%, stroke: 1.5pt + maroon)
  v(0.6cm)
}

// STUDENT IDENTITY (On every task page)
#let identity_block() = {
  block(width: 100%, inset: (bottom: 1em), [
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

// TASK CARD
#let task_card(level, title, bg_context, prompt, constraints) = {
  block(
    width: 100%,
    stroke: 1pt + maroon,
    radius: 4pt,
    clip: true,
    below: 0.8cm,
    [
      #block(fill: maroon, width: 100%, inset: 10pt, [
        #grid(
          columns: (auto, 1fr),
          text(fill: white, weight: "bold")[#level], align(right)[#text(fill: white, weight: "bold")[#title]],
        )
      ])
      #block(fill: white, inset: 12pt, width: 100%, [
        #text(size: 10pt, style: "italic", weight: "bold", fill: slate-dark)[#bg_context]
        #v(0.4em)
        #text(size: 11pt)[#prompt]
        #v(0.6em)
        #line(length: 100%, stroke: 0.5pt + gray-line)
        #v(0.4em)
        #text(size: 9pt, fill: slate-dark)[#constraints]
      ])
    ],
  )
}

// RADAR CHECKBOXES
#let radar_box(items) = {
  block(
    width: 100%,
    fill: rgb("#fff1f2"),
    stroke: (paint: maroon, dash: "dashed", thickness: 0.5pt),
    inset: 10pt,
    radius: 4pt,
    [
      #text(weight: "bold", fill: maroon)[Self-Correction Radar:]
      #h(1em)
      #(
        items
          .map(it => [
            #box(width: 10pt, height: 10pt, stroke: 1pt + maroon, radius: 2pt, baseline: 25%)
            #h(4pt)
            #text(size: 10pt)[#it]
            #h(1.2em)
          ])
          .join()
      )
    ],
  )
}

// WRITING LINES (Strict count to avoid spillover)
#let writing_lines(count: 15) = {
  v(0.4cm)
  for _ in range(count) {
    line(length: 100%, stroke: 0.5pt + slate-dark)
    v(0.55cm)
  }
}

// ==========================================
// 2. DOCUMENT LAYOUT
// ==========================================

// --- PAGE 1: REPAIR TARGETS ---
#integrated_header()

#text(size: 18pt, weight: "bold", fill: maroon)[Identify your top three repair targets]
#v(0.4em)
#text[Review your personal feedback report. What are the three most important errors you need to fix today?]

#v(1cm)

#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 1cm,
  ..range(1, 4).map(i => block(
    width: 100%,
    height: 3.5cm,
    fill: rgb("#F8FAFC"),
    radius: 6pt,
    inset: 12pt,
    stroke: 1pt + gray-line,
    [
      #text(weight: "bold", fill: maroon, size: 14pt)[Target #i]
      #v(1fr)
      #line(length: 100%, stroke: 1pt + maroon)
    ],
  ))
)

#v(1.5cm)
#align(center)[#text(
  style: "italic",
  fill: slate-dark,
  size: 11pt,
)[Turn to the next page and select the task for your assessed level.]]

// --- PAGE 2: LEVEL A2 ---
#pagebreak()
#identity_block()

#task_card(
  "Level A2 / A2+",
  "The Secret Recipe",
  "Magazine Announcement: What's Your Favorite Snack?",
  "Write an article about a simple dish you love to cook. Describe the ingredients and the steps to make it.",
  "Target: 50+ words | Time: 20 minutes",
)

#radar_box(("Used 'First', 'Then', 'Finally'?", "Checked is/am/are?"))

#writing_lines(count: 15)

// --- PAGE 3: LEVEL B1 ---
#pagebreak()
#identity_block()

#task_card(
  "Level B1 / B1+",
  "The Masterchef Warning",
  "Magazine Announcement: Cooking Secrets & Traps",
  "Write an article about a dish you love. Describe the success secret, but warn us about ONE common mistake (The Trap!).",
  "Target: 70+ words | Time: 20 minutes",
)

#radar_box(("Explained the 'Trap'?", "Articles (a/an/the)?", "Plurals ending in 's'?"))

#writing_lines(count: 15)

// --- PAGE 4: LEVEL B2 ---
#pagebreak()
#identity_block()

#task_card(
  "Level B2",
  "Signature Dishes",
  "Magazine Section: The Young Gourmet",
  "Write a professional description of a signature dish you have perfected. Describe the complexity of the process and the final experience.",
  "Target: 100+ words | Time: 20 minutes",
)

#radar_box(("Complex transitions used?", "Correct word forms?"))

#writing_lines(count: 15)
