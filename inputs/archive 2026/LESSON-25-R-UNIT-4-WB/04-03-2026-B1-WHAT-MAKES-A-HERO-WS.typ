#import "../../lib/typst/lib.typ": *

#set page(paper: "a4", margin: (top: 1cm, bottom: 1.5cm, x: 2cm))
#set text(font: "Arial", size: 13pt, fill: rgb("#333333"))
#set par(leading: 0.55em, justify: false)

// --- INTENSIVE BRANDING HEADER ---
#intensive_header()

// --- HERO STRAP WITH BADGES ---
#hero_strap(
  "What Makes a Hero?",
  "Unsung heroes achieve great things without recognition.",
  hero_image: image("images/hero.jpg"),
  badges: ("CEFR B1", "READING", "UNSUNG HEROES")
)

#v(0.5cm)

// --- MISSION MANDATE ---
#block(
  fill: rgb("#fceceb"),
  stroke: 1.5pt + maroon,
  inset: 15pt,
  radius: 4pt,
  width: 100%,
  [
    #text(weight: "bold", fill: maroon, size: 16pt)[YOUR MISSION]
    #v(0.3em)
    #text(size: 11pt, style: "italic")[Today's mission develops the 'Identifying Facts and Opinions' sub-skill, which is critical for *B1 Preliminary (PET)* Part 4. You must distinguish between evidence-based facts and personal beliefs.]
    #v(0.8cm)
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 20pt,
      [#text(weight: "bold", fill: maroon)[RECOGNIZE]\ 5 key heroic vocabulary terms.],
      [#text(weight: "bold", fill: maroon)[SCAN]\ Find 3 heroes in 120 seconds.],
      [#text(weight: "bold", fill: maroon)[ANALYZE]\ Separate fact from opinion.],
    )
  ]
)

#v(0.8cm)

// --- TASK 1: VOCABULARY ---
#task_header("1", "HEROIC TERMS")
#v(0.3cm)
#text[Match the vocabulary items to their definitions.]
#v(0.5cm)
#grid(
  columns: (auto, 1fr, auto),
  gutter: 15pt,
  [1. *recognition*], [#box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]], [a organized journey for a particular purpose],
  [2. *determination*], [#box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]], [b public praise or thanks for your actions],
  [3. *expedition*], [#box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]], [c very brave; having courage],
  [4. *courageous*], [#box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]], [d something difficult you have successfully done],
  [5. *achievement*], [#box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]], [e the ability to continue despite difficulties],
)

#v(1cm)

// --- TASK 2: UNSUNG HEROES (TEXT) ---
// Rule: No page break before Task 2 (per user instructions)
#task_header("2", "UNSUNG HEROES")
#v(0.3cm)

#block(breakable: false, [
  *Part 1: Gist Reading* \
  Read the first paragraph. What is the article about? Choose the best option:
  #v(0.3cm)
  #set enum(numbering: "1.")
  + People who are called heroes, but didn't do anything special. [#box(width: 1cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]]
  + Heroes who are not very famous or well known. [#box(width: 1cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]]
  + Qualities that every hero should have. [#box(width: 1cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]]
])

#v(0.5cm)

#block(breakable: false, [
  *Part 2: Speed Scan* \
  Scan the full text. Match the hero to their specific field:
  #v(0.3cm)
  #grid(
    columns: (1fr, 1fr, 1fr),
    gutter: 15pt,
    [1. Junko Tabei], [2. Svetlana Savitskaya], [3. Scott Fahlman],
    [#box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]],
    [#box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]],
    [#box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]],
    [(Space)], [(Internet)], [(Mountain)],
  )
])

#v(0.8cm)

#block(breakable: false, [
#text(fill: maroon, weight: "bold")[[1]] Heroes are recognized as courageous leaders - people who help others or make the world a better place. We read about them in the news. They receive awards. Unsung heroes, on the other hand, achieve great things, but don't receive much recognition for their actions.

#text(fill: maroon, weight: "bold")[[2]] When she was very young, Junko Tabei (1939-2016) was not strong or healthy. But she had a dream: to climb mountains. In 1975, she became the first woman to climb Mount Everest, the world's tallest peak. She continued until she'd climbed the "seven summits." Such a courageous climber should be a world-famous hero!

#text(fill: maroon, weight: "bold")[[3]] Svetlana Savitskaya (1948-) began skydiving at 16. In 1981, she became the second woman in space. Maybe this is why she isn't very famous. After retiring, she entered politics. More people should know about this incredible woman and her achievements!

#text(fill: maroon, weight: "bold")[[4]] Computer scientist Scott Fahlman suggested that people mark jokes with a smiling face :-) on September 19, 1982. I think this makes him a hero of modern communication.
])

#v(1cm)

// --- TASK 3: FACT OR OPINION ---
#task_header("3", "FACT VS OPINION")
#v(0.5cm)
#text[Decide if the statements below are Facts (F) or Opinions (O) based on the text.]
#v(0.5cm)

#set enum(numbering: n => [*#n.*])
+ Svetlana Savitskaya set 23 world records for speed. [#box(width: 1cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]]
+ Junko Tabei was the first woman to climb Mount Everest. [#box(width: 1cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]]
+ Scott Fahlman is a hero of modern communication. [#box(width: 1cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]]
+ Svetlana is more incredible than other astronauts. [#box(width: 1cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]]
+ Junko Tabei's life in the mountains was amazing. [#box(width: 1cm, stroke: (bottom: 0.75pt + black), baseline: 15%)[]]

#pagebreak()

// --- IDENTITY BLOCK & EXTENSION ---
#identity_block()
#v(0.5cm)

#task_header("4", "MY UNSUNG HERO")
#v(0.5cm)
#text[Who is an 'unsung hero' in your life or community? Write a paragraph explaining why they are heroic. Use at least two vocabulary words from Task 1 (e.g., *determination*, *courageous*).]

#v(0.5cm)

// OFFICIAL TYPST FIX: Dynamic fill-to-bottom using fractional grid rows
// This fills the remaining page space with ruled lines without spilling over.
#block(width: 100%, height: 1fr)[
  #grid(
    columns: (100%),
    rows: (1.1cm), // Standard handwriting spacing
    gutter: 0pt,
    stroke: (bottom: 0.5pt + gray),
    ..for _ in range(25) { ([ ],) } // Oversupply rows; block(height: 1fr) with clip:true (default) handles the rest
  )
]
