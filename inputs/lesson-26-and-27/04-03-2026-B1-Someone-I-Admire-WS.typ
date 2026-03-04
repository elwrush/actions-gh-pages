#import "/lib/typst/lib.typ": *

#set page(
  paper: "a4",
  margin: (top: 1cm, bottom: 1.5cm, x: 2cm),
)
#set text(font: "Arial", size: 12pt, fill: rgb("#333333"))
#set par(leading: 0.55em, justify: false)
#set enum(numbering: n => [*#n.*])

#intensive_header()

#hero_strap(
  "Someone I Admire",
  "Building a profile and supporting your opinion with facts.",
  hero_image: image("images/hero.jpg"),
  badges: ("B1", "Writing", "Heroes")
)

#v(0.2cm)

// --- YOUR MISSION (The Cambridge Hook) ---
#block(
  width: 100%,
  fill: pale-pink,
  stroke: 1.5pt + maroon,
  inset: 12pt,
  radius: 4pt,
  [
    #text(fill: maroon, weight: "bold", size: 14pt)[YOUR MISSION]
    #v(0.2cm)
    #text(size: 10.5pt, style: "italic")[
      In the B1 Preliminary (PET) Writing exam, you must clearly express and support your opinions. Today, you will build a detailed profile of an admirable person and draft a 225-word description that provides facts and real-life examples to back up your views.
    ]
    #v(0.4cm)
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 10pt,
      align: center,
      stack(spacing: 5pt, text(size: 18pt)[🎯], [*Identify*], [Traits]),
      stack(spacing: 5pt, text(size: 18pt)[✍️], [*Use*], [Adverbs]),
      stack(spacing: 5pt, text(size: 18pt)[📊], [*Support*], [Facts]),
    )
  ]
)

// --- TASK 1: THE ADJECTIVE MAP ---
#block(breakable: true, [
  #task_header(1, "The Admirable Profile")
  #v(0.2cm)
  Choose a person you admire. List three admirable traits and provide a supporting fact for each.
  
  #v(0.3cm)
  #grid(
    columns: (1fr, 2fr),
    gutter: 1cm,
    [*Admirable Trait*], [*Supporting Fact / Example*],
    line(length: 100%, stroke: 0.5pt + maroon), line(length: 100%, stroke: 0.5pt + maroon),
    v(0.6cm), v(0.6cm),
    line(length: 100%, stroke: 0.5pt + maroon), line(length: 100%, stroke: 0.5pt + maroon),
    v(0.6cm), v(0.6cm),
    line(length: 100%, stroke: 0.5pt + maroon), line(length: 100%, stroke: 0.5pt + maroon),
  )
])

// --- TASK 2: ATTITUDE ADVERBS ---
#block(breakable: true, [
  #task_header(2, "Adding Attitude")
  #v(0.2cm)
  Rewrite these sentences using: _Amazingly, Surprisingly, Remarkably, Fortunately, Clearly, Generously._
  
  #v(0.3cm)
  + She won the gold medal despite her injury.
    #v(0.6cm)
    #line(length: 100%, stroke: 0.5pt + gray-line)
  
  + He survived the crash without any scratches.
    #v(0.6cm)
    #line(length: 100% , stroke: 0.5pt + gray-line)
  
  + They decided to donate all their money to charity.
    #v(0.6cm)
    #line(length: 100%, stroke: 0.5pt + gray-line)

  + He found his missing passport just before the flight.
    #v(0.6cm)
    #line(length: 100%, stroke: 0.5pt + gray-line)

  + The team managed to win the game in the final minute.
    #v(0.6cm)
    #line(length: 100%, stroke: 0.5pt + gray-line)

  + She has written ten books by the age of twenty.
    #v(0.6cm)
    #line(length: 100%, stroke: 0.5pt + gray-line)
])

#pagebreak()

// --- IDENTITY BLOCK & TASK 3 ---
#identity_block()

#v(0.4cm)

#block(breakable: false, [
  #task_header(3, "First Draft")
  #v(0.2cm)
  Write your first draft of a description of a person you admire (approx. 225 words). Remember to state your opinion clearly, use attitude adverbs, and support your points with facts.
])

#v(0.4cm)

#block(width: 100%, height: 1fr)[
  #writing_lines_dynamic(line-spacing: 1.1cm)
]

#pagebreak()

#block(width: 100%, height: 1fr)[
  #writing_lines_dynamic(line-spacing: 1.1cm)
]
