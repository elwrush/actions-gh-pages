#import "../../lib/typst/lib.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 1.5cm, x: 1.5cm))
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#intensive_header()

#hero_strap(
  "The Heroic Journey",
  "Relative Clauses & Emergency Essentials",
  hero_image: image("/images/storyteller.jpg"),
  badges: ("B1", "Grammar", "Heroes")
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
    Today we are training for the #strong[Cambridge B1 Preliminary (PET)] exam. In the Reading and Writing sections, you must identify and describe relationships between people, places, and events. Mastering relative clauses will make your descriptions precise and professional.

    #v(0.5em)
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 10pt,
      [🎯 *Identify* the correct relative pronouns for people, things, and time.],
      [📝 *Master* vocabulary for emergencies and heroic actions.],
      [🗣️ *Combine* complex sentences to describe historical and fictional heroes.]
    )
  ]
)

#block(breakable: false, [
  #task_header(1, "The Wise Storyteller")
  #v(0.3cm)
  #text(size: 11pt)[Read the story of Nasreddin Hodja. Choose the correct relative pronouns to complete the text.]
  #v(0.3cm)
  #block(
    fill: rgb("#f5f5f5"),
    stroke: 0.5pt + rgb("#cccccc"),
    inset: 12pt,
    radius: 4pt,
    [
      #set par(leading: 0.8em, justify: true)
      Nasreddin Hodja was a wise man and storyteller #strong[who / which] lived in the 13th century. He's famous because there are thousands of stories #strong[where / which] he's a kind of comic hero. In one story, he searches for a ring #strong[which / who] he had lost in his house. After searching briefly inside the house, #strong[where / which] he's sure the ring is, he goes to look outside. His wife asks him, "Why are you looking outside? You lost the ring inside the house!" Without stopping his search, Nasreddin answers, "Because this is #strong[when / where] the light is the best – I can see better here!" Why do we call someone #strong[which / who] makes such a silly mistake a comic hero? Because even at times #strong[who / when] he makes silly mistakes, he believes in himself. Comic heroes always manage to show us the funny side of situations #strong[which / where] make most people angry or upset.
    ]
  )
])

#v(0.5cm)

#block(breakable: false, [
  #task_header(2, "Emergency Response")
  #v(0.3cm)
  #text(size: 11pt)[Match the emergency phrases (1-5) to their definitions (a-e).]
  #v(0.3cm)

  #grid(
    columns: (1fr, 1fr),
    gutter: 20pt,
    [
      1. got into trouble \
      2. got lost \
      3. severe weather \
      4. went missing \
      5. crowd
    ],
    [
      a. very bad \
      b. had problems \
      c. large group of people \
      d. were absent \
      e. couldn't find the way
    ]
  )
  
  #v(0.5cm)
  
  #grid(
    columns: (1fr, 1fr, 1fr),
    row-gutter: 0.8cm,
    [1. #box(width: 2.5cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]],
    [2. #box(width: 2.5cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]],
    [3. #box(width: 2.5cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]],
    [4. #box(width: 2.5cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]],
    [5. #box(width: 2.5cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]],
  )
])

#v(0.5cm)

#block(breakable: false, [
  #task_header(3, "The Heroic Connection")
  #v(0.3cm)
  #text(size: 11pt)[Combine the sentences using non-defining relative clauses. Remember to use commas!]
  #v(0.3cm)

  #set enum(numbering: "1.")
  #set par(leading: 1.5em)
  + Rosa Parks refused to give up her seat. She is known as "the first lady of civil rights". (who) \
    #box(width: 100%, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
    #box(width: 100%, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
  
  + Shakespeare is one of the world's most famous playwrights. His plays influenced the English language. (whose) \
    #box(width: 100%, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]

  + Marie Curie was the first woman to win a Nobel Prize. She won the prize in 1903. (which) \
    #box(width: 100%, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
    #box(width: 100%, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]
])

#pagebreak()

#block(breakable: false, [
  #task_header(4, "My Real-Life Hero")
  #v(0.3cm)
  #text(size: 11pt)[Who is a hero in your life? Describe them using at least three relative clauses (who, which, where, when, or whose). Is it their courage, intelligence, or kindness that makes them a hero?]
  #v(0.3cm)

  #writing_lines_dynamic()
])
