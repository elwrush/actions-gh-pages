#import "../../lib/typst/lib.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 1.5cm, x: 1.5cm))
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#intensive_header()

#hero_strap(
  "The Grammar Repair Shop",
  "Mastering 'Used To' vs 'Would' for Past Habits",
  hero_image: image("hero.jpg"),
  badges: ("B1", "Grammar", "Past Habits")
)

#v(0.5cm)

#block(
  width: 100%,
  fill: rgb("#fceceb"),
  stroke: 1.5pt + maroon,
  inset: 15pt,
  radius: 4pt,
  [
    #text(weight: "bold", fill: maroon, size: 14pt)[YOUR MISSION]
    #v(0.3em)
    In your B1 Preliminary (PET) exam, you often have to describe past experiences and habits in the Speaking and Writing sections. Mastering the difference between 'used to' and 'would' will make your descriptions much more natural and precise.

    #v(0.5em)
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 10pt,
      [🎯 *Identify* the difference between past states and past actions.],
      [📝 *Repair* sentences by choosing the most precise grammatical structure.],
      [🗣️ *Produce* accurate descriptions of your own childhood habits.]
    )
  ]
)

#v(0.5cm)

#task_header(1, "Complete the Dialogue")
#block(breakable: false, [
  #text(size: 11pt)[Complete the dialogue with the correct form of *used to* and short answers.]
  #v(0.3cm)
  #set par(leading: 1.2em)
  *Amy:* Have you ever lived abroad? \
  *Ben:* Yes, I have. I lived in China for a few years. \
  *Amy:* (1) #box(width: 4cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]] (you / go) to school in China? \
  *Ben:* Yes, I (2) #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]. \
  *Amy:* Wow, that's really cool. Why were you there? \
  *Ben:* My mother (3) #box(width: 4cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]] (work) for a company that had an office in Shanghai. \
  *Amy:* Shanghai? That's so interesting. \
  *Ben:* But you (4) #box(width: 4cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]] (live) abroad, too, right? Was it Germany? \
  *Amy:* No, we didn't live there. But we (5) #box(width: 4cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]] (visit) my grandparents there every summer.
])

#v(0.8cm)

#task_header(2, "The Replacement Challenge")
#block(breakable: false, [
  #text(size: 11pt)[Read the text about Two Super-Smart Kids. Decide if the numbered *used to* phrases can be replaced with *would* or *wouldn't*. If possible, write *would* or *wouldn't*. If not possible (because it is a state verb), write a dash (---).]
  #v(0.3cm)

  #block(
    fill: rgb("#f5f5f5"),
    stroke: 0.5pt + rgb("#cccccc"),
    inset: 12pt,
    radius: 4pt,
    [
      #set par(leading: 0.8em, justify: true)
      *Taylor Wilson* (1) used to dream of being a scientist. As a young child, he (2) used to read books about kids who liked science - books like Ken Silverstein's _The Radioactive Boy Scout_. He became fascinated by radiation. So, he (3) didn't use to spend his weekends being lazy, like some of his friends. Instead, he (4) used to go around his hometown on the weekends, searching for natural radioactivity. He (5) used to live in Arkansas, in the US, but his family moved to Nevada so he could attend a school for gifted students. At the age of 14, he built a nuclear reactor!

      When she was a child, *Brittany Wenger's* parents (6) used to tell her that she was going to be great one day. At school, she (7) used to spend a lot of time in the computer lab, learning to code. But she (8) didn't use to ignore her other subjects - she (9) used to get good grades in everything. Brittany (10) used to live with her family in Ohio, but now she studies computer science at Duke University.
    ]
  )

  #v(0.3cm)
  #grid(
    columns: (1fr, 1fr),
    gutter: 20pt,
    [
      #set enum(numbering: "1.")
      #set par(leading: 1.2em)
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
    ],
    [
      #set enum(numbering: "1.", start: 6)
      #set par(leading: 1.2em)
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
      + #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
    ]
  )
])

#v(0.8cm)

#task_header(3, "Sentence Repair")
#block(breakable: false, [
  #text(size: 11pt)[Complete the sentences with *used to / didn't use to* or *would / wouldn't*. For some sentences, both forms are possible.]
  #v(0.3cm)

  #set enum(numbering: "1.")
  #set par(leading: 1.5em)
  + In the summer, the kids in the neighborhood #box(width: 4cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]] often stay up late playing outside.
  + The students at my new school #box(width: 4cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]] be strangers, but now they're friends.
  + Before I got a bike, I #box(width: 4cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]] cycle to school. I walked every day.
  + My dad #box(width: 4cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]] work as a lawyer, but then he retrained to become a teacher.
  + We #box(width: 4cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]] live in a house, we lived in an apartment.
])