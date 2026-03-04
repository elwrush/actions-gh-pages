#import "../../lib/typst/lib.typ": *
#import "@preview/fontawesome:0.6.0": *

#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 1.5cm, x: 2cm),
)
#set text(font: "Arial", size: 12pt, fill: rgb("#333333"))
#set par(leading: 0.55em, justify: true)

// --- HEADER ---
#intensive_header()

#v(0.5cm)

// --- HERO STRAP ---
#hero_strap(
  "The Food of the Future",
  "How do we choose what we eat? Explore the science of future foods.",
  hero_image: image("images/hero_image.jpg"),
  badges: ("B1", "Reading", "Future Foods")
)

#v(0.5cm)

// --- MISSION ---
#block(
  fill: pale-pink,
  inset: 15pt,
  radius: 4pt,
  stroke: 1pt + maroon,
  [
    #text(weight: "bold", fill: maroon, size: 14pt)[YOUR MISSION]
    #v(0.3em)
    In your PET for Schools exam, you often have to read social media posts or articles about modern trends. This lesson helps you practice scanning for specific info and understanding new words from context.
    
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 10pt,
      align: center,
      [#fa-magnifying-glass(fill: maroon, size: 20pt) \ *Scan* for foods],
      [#fa-book-open(fill: maroon, size: 20pt) \ *Infer* meaning],
      [#fa-comment-dots(fill: maroon, size: 20pt) \ *Evaluate* choices]
    )
  ]
)

#v(0.5cm)

// --- READING TEXT (SOCIAL MEDIA STYLE) ---
#task_header(1, "The Social Media Feed")

#block(
  width: 100%,
  stroke: 0.5pt + gray,
  inset: 15pt,
  radius: 8pt,
  fill: white,
  [
    #stack(spacing: 15pt,
      // Post 1
      grid(columns: (40pt, 1fr), gutter: 10pt,
        circle(radius: 20pt, fill: maroon, align(center + horizon, text(fill: white, weight: "bold")[FP])),
        stack(spacing: 4pt,
          text(weight: "bold")[foodyperson] + text(fill: gray, size: 9pt)[ • 2h ago],
          text(fill: maroon, weight: "bold")[[1]] + [ I've found the food of the future, and it's here today! Has anyone else tried making snack bars with *algae*? I know Japanese food (which I love, by the way) uses sea plants – algae and others. But this is the first time I've used it in a snack bar recipe!],
        )
      ),
      
      // Reply 1
      grid(columns: (40pt, 1fr), gutter: 10pt,
        circle(radius: 20pt, fill: slate-dark, align(center + horizon, text(fill: white, weight: "bold")[EM])),
        stack(spacing: 4pt,
          text(weight: "bold")[emmy2003] + text(fill: gray, size: 9pt)[ • 1h ago],
          text(fill: maroon, weight: "bold")[[2]] + [ Haven't tried it. What's the flavor like? It's hard to tell from the picture.],
        )
      ),

      // Post 2
      grid(columns: (40pt, 1fr), gutter: 10pt,
        circle(radius: 20pt, fill: maroon, align(center + horizon, text(fill: white, weight: "bold")[FP])),
        stack(spacing: 4pt,
          text(weight: "bold")[foodyperson] + text(fill: gray, size: 9pt)[ • 45m ago],
          text(fill: maroon, weight: "bold")[[3]] + [ They're made with lots of nuts and seeds in addition to the algae, and the sweetener is orange juice! So they're nutty, and a bit sweet. To be honest, the flavor is *unexceptional* for a snack bar – you know, nothing special. \#superhealthy],
        )
      ),

      // Reply 2
      grid(columns: (40pt, 1fr), gutter: 10pt,
        circle(radius: 20pt, fill: rgb("#0ea5e9"), align(center + horizon, text(fill: white, weight: "bold")[AH])),
        stack(spacing: 4pt,
          text(weight: "bold")[ahmed101] + text(fill: gray, size: 9pt)[ • 30m ago],
          text(fill: maroon, weight: "bold")[[4]] + [ Why is algae the food of the future?],
        )
      ),

      // Post 3
      grid(columns: (40pt, 1fr), gutter: 10pt,
        circle(radius: 20pt, fill: maroon, align(center + horizon, text(fill: white, weight: "bold")[FP])),
        stack(spacing: 4pt,
          text(weight: "bold")[foodyperson] + text(fill: gray, size: 9pt)[ • 20m ago],
          text(fill: maroon, weight: "bold")[[5]] + [ Traditional farming has a big carbon footprint. Algae doesn't. Also it's very easy to grow, and doesn't use a lot of fresh water. Algae even grows in the ocean and it's a great source of protein.],
        )
      ),

      // Reply 3
      grid(columns: (40pt, 1fr), gutter: 10pt,
        circle(radius: 20pt, fill: slate-dark, align(center + horizon, text(fill: white, weight: "bold")[EM])),
        stack(spacing: 4pt,
          text(weight: "bold")[emmy2003] + text(fill: gray, size: 9pt)[ • 15m ago],
          text(fill: maroon, weight: "bold")[[6]] + [ Apparently insects are also a great source of protein. And you can buy protein bars made with insects. I've heard they're "perfect protein." The *crickets* are made into flour. You can buy the flour online, so you can try baking with it, too.],
        )
      ),

      // Post 4
      grid(columns: (40pt, 1fr), gutter: 10pt,
        circle(radius: 20pt, fill: maroon, align(center + horizon, text(fill: white, weight: "bold")[FP])),
        stack(spacing: 4pt,
          text(weight: "bold")[foodyperson] + text(fill: gray, size: 9pt)[ • 10m ago],
          text(fill: maroon, weight: "bold")[[7]] + [ I've heard of another meat that isn't made from animals. There's a company called The Impossible Burger that creates meat from plant sources. Everything is made up of *molecules* – tiny pieces of chemicals. They've figured out which molecules make up meat, and they get those from plants.],
          text(fill: maroon, weight: "bold")[[8]] + [ The secret ingredient is a molecule called "heme." That's what gives red meat its color and flavor. They *extract* heme from plants, and put it into their food product to make it look, feel, and taste like beef.],
        )
      )
    )
  ]
)

// --- COMPREHENSION TASKS ---
#task_header(2, "Vocabulary in Context")
#text(style: "italic")[Read the reading strategy and answer the questions about the words in bold.]

#grid(
  columns: (1fr, 1fr),
  gutter: 20pt,
  [
    #block(breakable: false, [
      1. *algae* 
      a) What type of word is it? 
      #v(0.8cm)
      #line(length: 100%, stroke: 0.5pt + gray)
    ])
    #block(breakable: false, [
      b) What synonym is used? 
      #v(0.8cm)
      #line(length: 100%, stroke: 0.5pt + gray)
    ])
    
    #block(breakable: false, [
      2. *unexceptional* 
      a) What part of speech is it? 
      #v(0.8cm)
      #line(length: 100%, stroke: 0.5pt + gray)
    ])
    #block(breakable: false, [
      b) What does the prefix tell you? 
      #v(0.8cm)
      #line(length: 100%, stroke: 0.5pt + gray)
    ])
  ],
  [
    #block(breakable: false, [
      3. *crickets* 
      a) What part of speech is it? 
      #v(0.8cm)
      #line(length: 100%, stroke: 0.5pt + gray)
    ])
    #block(breakable: false, [
      b) What word explains it? 
      #v(0.8cm)
      #line(length: 100%, stroke: 0.5pt + gray)
    ])
    
    #block(breakable: false, [
      4. *extract* 
      a) What part of speech is it? 
      #v(0.8cm)
      #line(length: 100%, stroke: 0.5pt + gray)
    ])
    #block(breakable: false, [
      b) What opposite is used? 
      #v(0.8cm)
      #line(length: 100%, stroke: 0.5pt + gray)
    ])
  ]
)

#v(0.5cm)

#align(left, block(
  width: 60%,
  stroke: 1pt + maroon,
  radius: 4pt,
  clip: true,
  image("images/algae_bars.jpg")
))

#task_header(3, "Fact Check")
#text(style: "italic")[Decide if the sentences are True (T) or False (F). Correct the false ones.]

#grid(
  columns: (auto, 1fr, auto),
  gutter: 10pt,
  align: horizon,
  [1.], [The food in the photo is typical Japanese food.], [T / F],
  [2.], [Using orange juice makes the bars unexceptional.], [T / F],
  [3.], [Cricket flour contains a lot of protein.], [T / F],
  [4.], [Heme for artificial beef is extracted from real beef.], [T / F]
)

#v(0.5cm)

#task_header(4, "Deep Understanding")
#text(style: "italic")[Find the sentence(s) in the conversation that give you this information.]

#block(breakable: false, [
  1. Is growing algae better for the environment than traditional farming? 
  #v(0.8cm)
  #line(length: 100%, stroke: 0.5pt + gray)
])

#block(breakable: false, [
  2. Is there any evidence that The Impossible Burger tastes like "real" beef? 
  #v(0.8cm)
  #line(length: 100%, stroke: 0.5pt + gray)
])

#v(0.5cm)

#pagebreak()

// --- STUDENT IDENTITY BLOCK (Moved before the Writing Task) ---
#identity_block()

#v(0.5cm)

// --- EXTENSION WRITING ---
#task_header(5, "Future Food Review")
#text(style: "italic")[Choose ONE of the foods from the text (algae bars, cricket flour, or the plant-based burger). Write a short social media review (40-60 words) imagining you have just tried it. Mention the flavor, texture, and why it's good for the planet.]

#writing_lines_dynamic()
