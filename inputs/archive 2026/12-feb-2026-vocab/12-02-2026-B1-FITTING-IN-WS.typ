#import "/lib/typst/lib.typ": *

#set page(
  paper: "a4",
  margin: (x: 1.5cm, y: 1.5cm),
)
#set text(font: "Arial", size: 13pt, fill: slate-dark)
#set par(leading: 0.55em, justify: false)

// GAP-FILL HELPER
#let gap(w) = box(width: w, stroke: (bottom: 1pt + gray-line), baseline: 20%)

// 1. BRANDING HEADER
#intensive_header()
#v(0.1cm)

// 2. HERO STRAP & BADGES
#hero_strap(
  "Fitting In",
  "Genius, Peer Pressure, and Emotional Intelligence",
  hero_image: image("images/genius_hero.jpg"),
  badges: ("B1", "Vocabulary", "Fitting In")
)

#v(0.5cm)

// 3. YOUR MISSION (Cambridge Hook)
#block(
  width: 100%,
  fill: pale-pink,
  stroke: 1pt + maroon,
  inset: 15pt,
  radius: 4pt,
  [
    #text(fill: maroon, weight: "bold", size: 16pt)[YOUR MISSION]
    #v(0.2cm)
    In your *B1 Preliminary (PET) for Schools* exam, you often have to understand texts about people's lives and their feelings. Today, you will explore the lives of famous geniuses and learn how to describe emotions and social groups using nouns and verbs.

    #v(0.3cm)
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 10pt,
      align: center,
      [#text(size: 20pt)[🧠]\ *Master Vocab*],
      [#text(size: 20pt)[📝]\ *Form Nouns*],
      [#text(size: 20pt)[😊]\ *Read Emotions*]
    )
  ]
)

#v(0.4cm)

// 4. TASK 1: DISCUSSION
#task_header(1, "The Social Pressure")
How much do you agree with these sentences? (1 = completely disagree; 5 = completely agree). Discuss with your partner.

#v(0.3cm)
#block(breakable: false, [
  #set enum(numbering: n => [*#n.*], spacing: 1.5em)
  + Peer pressure is always bad. #h(1fr) [ . . . . . ]
  + Great leaders rarely follow the crowd. #h(1fr) [ . . . . . ]
  + Conformists are boring. #h(1fr) [ . . . . . ]
  + Rebels are usually dangerous. #h(1fr) [ . . . . . ]
  + Standing out in a crowd is a bad thing. #h(1fr) [ . . . . . ]
  + Everyone should do their own thing sometimes. #h(1fr) [ . . . . . ]
])

#v(0.5cm)

// 5. TASK 2: READING - EINSTEIN
#task_header(2, "The Genius of Doing Your Own Thing")
Choose the correct words (a, b, or c) to complete the text about Albert Einstein.

#v(0.3cm)
#block(breakable: false, width: 100%, [
  #set par(leading: 2em) // Mandatory double-spacing for handwriting (approx 0.9cm)
  #text(fill: maroon, weight: "bold")[[1]] All of us, but especially teens, often feel *1.* #gap(3cm) pressure – that feeling that we should *2.* #gap(3cm) the crowd, do what everyone else is doing, and try not to be different. It can feel difficult to *3.* #gap(3cm) out in a crowd, to be the only one who looks, thinks, or feels a certain way.

  #v(0.2cm)
  #text(fill: maroon, weight: "bold")[[2]] However, while it isn't easy being *4.* #gap(3cm), you are not alone in the world. When you *5.* #gap(3cm) against everyone around you, you have something in *6.* #gap(3cm) with many great thinkers, including the scientific genius Albert Einstein.

  #v(0.2cm)
  #text(fill: maroon, weight: "bold")[[3]] While he was able to work with others well and share his ideas, he didn't always *7.* #gap(3cm) to their ideas of science or how a scientist should behave. He didn't always follow the rules – he was not *8.* #gap(3cm), and he didn't try to be like anyone but himself. So, go ahead – *9.* #gap(3cm) your own thing and fit in with Einstein.
])

#v(0.4cm)
#grid(
  columns: (40pt, 1fr, 1fr, 1fr),
  row-gutter: 12pt,
  column-gutter: 15pt,
  [*1*], [a rebel], [b peer], [c common],
  [*2*], [a follow], [b stand], [c conform],
  [*3*], [a have], [b be], [c stand],
  [*4*], [a a conformist], [b an outsider], [c a rebel],
  [*5*], [a rebel], [b conform], [c are],
  [*6*], [a common], [b pressure], [c crowd],
  [*7*], [a follow], [b conform], [c be],
  [*8*], [a a crowd], [b a conformist], [c a rebel],
  [*9*], [a have], [b be], [c do]
)

#v(0.6cm)

// 6. TASK 3: NOUN FORMATION - STELLA YOUNG
#task_header(3, "What we can learn from Stella Young")
Complete the text with the correct form (*verb* or *noun*) of the verbs in parentheses.

#v(0.3cm)
#block(breakable: false, width: 100%, [
  #set par(leading: 2em) // Mandatory double-spacing for handwriting
  #text(fill: maroon, weight: "bold")[[1]] Because she looked so different from most people, Stella Young's *1* #gap(3cm) (appear) often caused a *2* #gap(3cm) (react). She was a wheelchair user, weighed about 40 kilograms, and though she was an adult, she was the size of a child.

  #v(0.2cm)
  #text(fill: maroon, weight: "bold")[[2]] She spent her career as a writer and comedian trying to help people *3* #gap(3cm) (understand) disability. She noticed from a young age that people would *4* #gap(3cm) (treat) her differently. And people would look at her with an *5* #gap(3cm) (express) of sadness, when she herself felt that she had a great life.
])

#v(0.6cm)

// 7. TASK 4: EMOTIONS
#task_header(4, "How we read each other's emotions")
Complete the text with the correct form (verb or noun) of the words below.
#v(0.2cm)
#align(center)[*appear* #h(1cm) *express* #h(1cm) *practice* #h(1cm) *react* #h(1cm) *treat* #h(1cm) *understand*]
#v(0.2cm)

#block(breakable: false, width: 100%, [
  #set par(leading: 2em) // Mandatory double-spacing for handwriting
  #text(fill: maroon, weight: "bold")[[1]] When you feel emotion, your face *1* #gap(3.5cm). You can *2* #gap(3.5cm) trying to hide your feelings, but it's almost impossible to stop the smile that *3* #gap(3.5cm) in your eyes, even if your mouth and lips don't show it.

  #v(0.4cm)
  #text(fill: maroon, weight: "bold")[[2]] And this is important, because the way we *4* #gap(3.5cm) one another is based partly on the emotion that we read on others' faces. Scientific *5* #gap(3.5cm) is improving constantly. Scientists believe that the *6* #gap(3.5cm) on your face could indicate one of four emotions: happiness, sadness, fear, or anger.
])

#pagebreak()

// 8. IDENTITY BLOCK FOR WRITING TASK
#identity_block()
#v(0.5cm)

// 9. EXTENSION TASK: WRITING
#task_header(5, "Your Inner Genius")
#text(style: "italic", size: 12pt)[Critical Thinking & Extension Writing Task]

#v(0.4cm)
#block(
  width: 100%,
  stroke: 1pt + maroon,
  inset: 15pt,
  radius: 4pt,
  [
    Albert Einstein said: *"The person who follows the crowd will usually go no further than the crowd. The person who walks alone is likely to find himself in places no one has ever been before."*

    #v(0.3cm)
    Write a short paragraph (50-80 words) about a time when you decided *not to follow the crowd*. 
    - Why did you make that choice? 
    - How did it make you feel?
    - Use at least *three* nouns and verbs from today's lesson (e.g., *rebel, outsider, reaction, expression*).
  ]
)

#writing_lines_dynamic()
