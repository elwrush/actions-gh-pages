#import "../../lib/typst/lib.typ": *
#import "@preview/meander:0.3.1"

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 2cm, x: 2cm))
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.55em, justify: true)

// --- BRANDING ---
#intensive_header()

// --- HERO SECTION ---
#hero_strap(
  "Car-Free Zones",
  "Navigating the Urban Center",
  hero_image: image("images/hero_image.jpg"),
  badges: ("B1", "Listening", "Car-Free Zones")
)

#v(0.5cm)

// --- YOUR MISSION ---
#block(
  fill: pale-pink,
  stroke: 1pt + maroon,
  inset: 12pt,
  radius: 4pt,
  width: 100%,
  [
    #text(weight: "bold", fill: maroon, size: 14pt)[YOUR MISSION]
    #v(0.2cm)
    #text(size: 10pt, style: "italic")[In your B1 Preliminary for Schools exam, you often have to identify specific details and opinions in a discussion. Today, you will master the art of the 'Advantage Audit'.]
    #v(0.4cm)
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 15pt,
      align: center,
      [
        #v(5pt)
        #text(size: 9pt, weight: "bold")[MAP THE ZONE]
      ],
      [
        #v(5pt)
        #text(size: 9pt, weight: "bold")[DECODE PROS/CONS]
      ],
      [
        #v(5pt)
        #text(size: 9pt, weight: "bold")[NAVIGATE STREETS]
      ]
    )
  ]
)

#v(0.5cm)

#meander.reflow({
  import meander: *

  // Map Obstacle - Large and Visible
  placed(
    top + right,
    dy: 0.5cm,
    boundary: contour.margin(12pt),
    block(
      width: 7cm,
      stroke: 1.5pt + maroon,
      inset: 12pt,
      fill: white,
      image("images/workbook_map.png", width: 100%)
    )
  )

  container()

  content[
    #task_header(1, "The Urban Grid")
    #text(style: "italic")[Look at the map. The gray streets are a car-free zone. What are the advantages and disadvantages of this sort of area in a city?]

    #v(0.5cm)
    #block(breakable: false)[
      #text(weight: "bold", fill: maroon)[ADVANTAGES] \
      #v(0.6cm)
      #line(length: 100%, stroke: 0.5pt + gray-line)
      #v(0.6cm)
      #line(length: 100%, stroke: 0.5pt + gray-line)
    ]

    #v(0.3cm)
    #block(breakable: false)[
      #text(weight: "bold", fill: maroon)[DISADVANTAGES] \
      #v(0.6cm)
      #line(length: 100%, stroke: 0.5pt + gray-line)
      #v(0.6cm)
      #line(length: 100%, stroke: 0.5pt + gray-line)
    ]

    #v(0.8cm)
    #task_header(2, "The Advantage Audit")
    #text(style: "italic")[Listen to a host mother talking about the map with an exchange student. Complete the chart with the advantages and disadvantages of the car-free zone that they mention.]
  ]
})

#v(0.5cm)
#rect(width: 100%, stroke: 0.5pt + gray-line, inset: 10pt)[
  #text(weight: "bold", fill: maroon)[ADVANTAGES]
  #v(0.8cm)
  #line(length: 100%, stroke: 0.5pt + gray-line)
  #v(0.8cm)
  #line(length: 100%, stroke: 0.5pt + gray-line)
  #v(0.8cm)
  #line(length: 100%, stroke: 0.5pt + gray-line)
  
  #v(0.5cm)
  #text(weight: "bold", fill: maroon)[DISADVANTAGES]
  #v(0.8cm)
  #line(length: 100%, stroke: 0.5pt + gray-line)
  #v(0.8cm)
  #line(length: 100%, stroke: 0.5pt + gray-line)
]

#v(0.5cm)

// --- TASK 3: LANGUAGE FOCUS ---
#task_header(3, "The Map Code")
#text(style: "italic")[Choose the correct words to complete the navigation phrases.]

#v(0.5cm)
#set enum(numbering: "a)")
#grid(
  columns: (1fr, 1fr),
  gutter: 15pt,
  [
    + According *by / to / by* the scale 
    + *check / look / watch* the key 
    + *go for / at / in* this direction 
    + *go east along / for / with* this road
  ],
  [
    + *look out to / for / at* the supermarket 
    + *what for / is / does* this symbol mean 
    + *take / do / have* a shortcut
  ]
)

#v(1cm)

// --- TASK 4: DIALOGUE COMPLETION ---
#task_header(4, "Urban Dialogue")
#text(style: "italic")[Complete the dialogue with phrases a-g from the previous task.]

#v(0.5cm)
#block(breakable: false, width: 100%)[
  #set par(leading: 1.2em) // Double spacing for handwriting
  *Kim*: Look, there's a castle on the north side of town. That's where I want to go. \
  #v(0.4cm)
  *Rob*: Oh, OK. But you can't go straight north from the bus station, so first, you have to [1] #box(width: 3.5cm, line(length: 100%, stroke: 0.5pt + gray-line)). \
  #v(0.4cm)
  *Kim*: OK, that's to the right on the map. But [2] #box(width: 3.5cm, line(length: 100%, stroke: 0.5pt + gray-line)) – the tree? \
  #v(0.4cm)
  *Rob*: Let's [3] #box(width: 3.5cm, line(length: 100%, stroke: 0.5pt + gray-line)). Oh, it means a park. \
  #v(0.4cm)
  *Kim*: That way looks very long. We can [4] #box(width: 3.5cm, line(length: 100%, stroke: 0.5pt + gray-line)) and save time. \
  #v(0.4cm)
  *Rob*: Oh, I think you're right. [5] #box(width: 3.5cm, line(length: 100%, stroke: 0.5pt + gray-line)), it's about two kilometers to the park. \
  #v(0.4cm)
  *Kim*: Right. So we should [6] #box(width: 3.5cm, line(length: 100%, stroke: 0.5pt + gray-line)) and turn left there. \
  #v(0.4cm)
  *Rob*: OK. And if we [7] #box(width: 3.5cm, line(length: 100%, stroke: 0.5pt + gray-line)), we'll pass a soccer field.
]

#v(1cm)

// --- FINAL WRITING / ROLEPLAY PREP ---
#task_header(5, "City Navigators")
#text(style: "italic")[Choose ONE of the following situations. Prepare a short dialogue using the map and the navigation phrases from today.]
- You're at the bus station and want to get to the theater.
- You're at the bus station and want to get to the beach.
- You're at the bus station and want to visit the park and the restaurant.

#writing_lines_dynamic()
