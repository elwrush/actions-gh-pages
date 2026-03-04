#import "/skills/generating-worksheets/templates/grammar_repair_worksheet_gold.typ": *
#import "@preview/meander:0.3.1"

#show: doc => integrated_header(
  doc,
  title: "The History of Roblox",
  date: "26-01-26",
  level: "A2",
  time: "46 mins",
  program: "Bell",
  header_image: "/images/bell-header.jpg"
)

#identity_block()

#v(1cm)

// Meander Layout with Text Wrapping
#meander.reflow({
  import meander: *

  // Image: Thai students playing Roblox
  placed(
    center + top,
    dy: 2cm, // Push down slightly into the text
    // Removed circular contour to allow rectangular wrapping for the photo
    image("thai-students-roblox.png", width: 8cm)
  )

  // Two columns for the text
  container(width: 48%)
  container(width: 48%, dx: 52%)
  
  content[
    #set text(size: 11pt, font: "Arial")
    #set par(justify: true)

    *What is Roblox?* 
    Roblox is a very popular online game platform. It allows users to create their own games and play games created by other people. It is not just one game. It is a place where you can find millions of different experiences.

    *How it Started* 
    Two men, David Baszucki and Erik Cassel, started the company. They launched a beta version called "DynaBlocks" in 2004. They tested it with a small group of people. In 2005, they changed the name to Roblox. The name "Roblox" comes from combining two words: "robots" and "blocks".

    *Growth and Success* 
    The official website launched on September 1, 2006. At first, the community was small. But it grew quickly. In 2013, Roblox added a feature called "Developer Exchange". This let game developers exchange their virtual money (Robux) for real money. This was a big change. It meant people could actually earn a living by making games on Roblox.

    *Roblox Today* 
    Today, millions of people play Roblox every day. You can do almost anything. You can adopt pets in "Adopt Me!", build houses in "Bloxburg", or work in a pizza place. It is a fun way to play and chat with friends online. Roblox is more than just a game; it is a global community where creativity has no limits.
  ]
})

#v(1cm)

// Exercises
#block(
  fill: rgb("#F0F0F0"),
  inset: 12pt,
  radius: 4pt,
  width: 100%,
  [
    *Task 1: True or False* 
    Read the text and write T (True) or F (False).
    
    1. David Baszucki and Erik Cassel started Roblox. #box(width: 1cm, stroke: (bottom: 1pt + black)) 
    2. The first name of the game was "Robots". #box(width: 1cm, stroke: (bottom: 1pt + black)) 
    3. The official website launched in 2006. #box(width: 1cm, stroke: (bottom: 1pt + black)) 
    4. You cannot earn real money on Roblox. #box(width: 1cm, stroke: (bottom: 1pt + black)) 
    5. Roblox has only one game you can play. #box(width: 1cm, stroke: (bottom: 1pt + black))
  ]
)

#v(1cm)

#block(
  fill: rgb("#E6EEF5"),
  inset: 12pt,
  radius: 4pt,
  width: 100%,
  [
    *Task 2: Vocabulary Matching* 
    Match the words with their meanings.

    #grid(
      columns: (1fr, 1fr),
      gutter: 1cm,
      [
        1. Platform 
        2. Launch 
        3. Developer 
        4. Virtual 
        5. Community
      ],
      [
        a. To start something new 
        b. A group of people together 
        c. On a computer, not real life 
        d. A place for software and games 
        e. A person who makes software
      ]
    )
    #v(0.5cm)
    1. #box(width: 1cm, stroke: (bottom: 1pt + black)) 
    2. #box(width: 1cm, stroke: (bottom: 1pt + black)) 
    3. #box(width: 1cm, stroke: (bottom: 1pt + black)) 
    4. #box(width: 1cm, stroke: (bottom: 1pt + black)) 
    5. #box(width: 1cm, stroke: (bottom: 1pt + black)) 
  ]
)

#v(1cm)

#block(
  stroke: 1pt + rgb("#A62D26"),
  inset: 12pt,
  radius: 4pt,
  width: 100%,
  [
    *Task 3: Short Writing* 
    Answer the question in a short paragraph (30-50 words).
    
    *If you could create your own Roblox game, what would it be about? Give it a name and describe what players can do.*
    
    #v(1cm)
    #repeat[
      #line(length: 100%, stroke: (paint: gray, dash: "dotted"))
      #v(0.85cm)
    ]
    #line(length: 100%, stroke: (paint: gray, dash: "dotted"))
  ]
)

#pagebreak()

// Answer Key
#align(center)[= Answer Key]

*Task 1: True or False*
1. True
2. False (It was DynaBlocks)
3. True
4. False (You can earn money via Developer Exchange)
5. False (There are millions of games)

*Task 2: Vocabulary Matching*
1. d
2. a
3. e
4. c
5. b