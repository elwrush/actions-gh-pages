#import "/lib/typst/lib.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 1.5cm, x: 2cm))
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: true)

// Standard List Spacing
#set enum(spacing: 1.2em, indent: 0.5em)
#set list(spacing: 0.8em, indent: 1.5em)

#intensive_header()

#v(0.2cm)

#hero_strap(
  "Legendary Cities",
  "Atlantis, El Dorado, and Shangri-La",
  hero_image: image("/inputs/29-Jan-Reading-Part-6/images/atlantis.png"),
  badges: ("B1", "Reading")
)

#v(0.2cm)

#task_header(1, "The Language of Legends")
_Match the words to their definitions._

#v(0.5em)

#grid(
  columns: (1fr, 2.5fr),
  gutter: 15pt,
  [
    1. *philosopher* #h(1fr) [ ] \
    2. *earthquake* #h(1fr) [ ] \
    3. *ritual* #h(1fr) [ ] \
    4. *fictional* #h(1fr) [ ] \
    5. *paradise* #h(1fr) [ ]
  ],
  [
    a. a ceremony or series of acts that is always performed in the same way. \
    b. a person who studies ideas about knowledge, truth, and the meaning of life. \
    c. a place or state of great happiness where everything is exactly as you would like. \
    d. a sudden shaking of a part of the Earth's surface. \
    e. not real; existing only in stories.
  ]
)

#v(0.2cm)

#task_header(2, "Reading: Lost Cities")

#v(0.5cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 20pt,
  block(
    stroke: 1pt + maroon,
    inset: 8pt,
    fill: white,
    [
      #image("/inputs/29-Jan-Reading-Part-6/images/el-dorado.png", width: 100%)
      #text(size: 8pt, style: "italic", fill: maroon)[The legendary city of gold...]
    ]
  ),
  block(
    stroke: 1pt + maroon,
    inset: 8pt,
    fill: white,
    [
      #image("/inputs/29-Jan-Reading-Part-6/images/shangri-la.png", width: 100%)
      #text(size: 8pt, style: "italic", fill: maroon)[The secret paradise of the mountains.]
    ]
  )
)

#v(0.5cm)

#set text(size: 11.5pt)
#set par(leading: 0.8em, first-line-indent: 1em)

#text(fill: maroon, weight: "bold")[[1]] More than 2,000 years ago, the Greek philosopher Plato wrote about the city of Atlantis. Long before his own time, he said, a rich, powerful military city had existed on an island in the Atlantic Ocean. Life was happy there, but Atlantis attacked other countries unfairly. One day, a huge earthquake struck, and Atlantis disappeared beneath the sea.

#text(fill: maroon, weight: "bold")[[2]] But Plato’s story wasn’t written as history – it was a lesson about fairness. However, people have long talked of the city as though it actually existed, and some are still looking for it. Although the undersea remains of ancient cities have been found near India, Japan, and Greece, Atlantis will never be found.

#text(fill: maroon, weight: "bold")[[3]] Europeans traveling to South America in the 1500s were looking for a legendary city of gold: El Dorado. They believed it was well hidden, and full of precious metal and jewels – and they wanted to find it.

#text(fill: maroon, weight: "bold")[[4]] Where had the story come from? A group of native people known as the Muisca had ceremonies where leaders were covered in gold dust before washing in a lake and throwing small pieces of gold into the water. Outsiders knew about the ritual, and the story of “The Gold One” (El Dorado in Spanish) spread, and with it the idea of a city of gold – though it never actually existed. Local people may have used the story to try to get rid of invaders, telling them that the city did indeed exist, but that it was far away, and they must go looking for it.

#text(fill: maroon, weight: "bold")[[5]] The story said that in the Kunlun Mountains of Central China, there existed a happy secret city where people lived to be hundreds of years old. However, unlike Atlantis and El Dorado, we know that the city is fictional. Why? Because it comes from a 1933 novel by James Hilton, called *Lost Horizon*. It’s the story of a British diplomat who is taken to Shangri-La after his plane crashes in the mountains.

#text(fill: maroon, weight: "bold")[[6]] Although they expected to be rescued and returned home, he and his companions instead decide to stay, because the city is a paradise. So, while no one has ever actually searched for Shangri-La, we use the name to describe any beautiful, remote paradise that feels cut off from the world.




#task_header(3, "Summary Completion")
_Complete the summary with names, dates, or locations from the text._

#v(1em)

#let gap = box(width: 3.5cm, stroke: (bottom: 0.5pt + black), baseline: 25%)

#block(
  fill: pale-pink,
  inset: 15pt,
  radius: 4pt,
  [
    #set par(leading: 1.5em)
    Plato wrote about Atlantis over 1 #gap years ago, describing it as a powerful, war-like city that was destroyed by an 2 #gap. Atlantis was just a story; however, real undersea cities have been found near 3 #gap, 4 #gap, and 5 #gap.
    
    When Europeans arrived in South America in the 6 #gap, they were searching for a city of gold. The legend was based on the rituals of the 7 #gap, a group of native people, but the city didn't actually exist.
    
    Shangri-La was said to be in China's 8 #gap Mountains, according to a novel called 9 #gap. The city first appeared in this book, which was published in 10 #gap.
  ]
)

#v(1.5em)

#task_header(4, "Detailed Reading")
_Choose the correct answer._

#v(0.5em)

+ What does Plato's story about Atlantis tell us?
  #set enum(numbering: "a.", spacing: 0.6em)
  + It's a detailed written history of the city.
  + It's a lesson about the importance of fairness.
  + It describes where to find the ruins today.
  + It explains how to build a powerful military.

+ Nowadays, ... Atlantis.
  #set enum(numbering: "a.", spacing: 0.6em)
  + some people are still looking for
  + no one believes in
  + tourists visit the ruins of
  + some people want to rebuild

+ It seemed to Europeans that the Muisca ... gold.
  #set enum(numbering: "a.", spacing: 0.6em)
  + wanted to steal their
  + had a lot of
  + expected to sell their
  + had never seen

+ Shangri-La is a name that comes from ....
  #set enum(numbering: "a.", spacing: 0.6em)
  + ancient Chinese stories
  + early British explorers
  + maps from the 1800s
  + a work of fiction

#v(1.5em)

#pagebreak()

#identity_block()

#v(0.5cm)

#task_header(5, "Writing: Your Shangri-La")
_What would your dream city look like? What would it have? What would it NOT have? Write 60-80 words._

#v(0.5em)

#writing_lines_dynamic()

#v(1cm)

#pagebreak()

#line(length: 100%, stroke: 0.5pt + maroon)
#align(center)[
  #text(size: 14pt, weight: "bold", fill: maroon)[ANSWER KEY]
]

#v(0.5cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 20pt,
  [
    *Task 1* \
    1. b, 2. d, 3. a, 4. e, 5. c \
    *Task 3* \
    1. 2,000, 2. earthquake, 3. India, 4. Japan, 5. Greece, 6. 1500s, 7. Muisca, 8. Kunlun, 9. Lost Horizon, 10. 1933
  ],
  [
    *Task 4* \
    1. b, 2. a, 3. b, 4. d \
    *Task 5* \
    Check for: adjectives (remote, beautiful, peaceful) and B1 level grammar.
  ]
)
