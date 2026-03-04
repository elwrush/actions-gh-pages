
// ============================================================
// B1 INTENSIVE READING: THE FOOD OF INDONESIA
// ============================================================

#set page(
  paper: "a4",
  margin: (top: 1cm, bottom: 2cm, x: 1.5cm),
)
#set text(font: "Arial", size: 11.5pt, fill: rgb("#1A1A1A"))
#set par(leading: 0.75em, justify: true)

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let dark-gray = rgb("#404040")

// ==========================================
// 1. COMPONENTS
// ==========================================

#let intensive_header() = {
  align(center)[
    #block(
      width: 100%,
      inset: (top: 0.5cm),
      [
        #image("/images/intensive-header.jpg", width: 100%)
      ],
    )
  ]
  v(0.2cm)
}

#let section_header(title) = {
  v(0.5cm)
  block(width: 100%, [
    #text(weight: "bold", fill: maroon, size: 13pt)[#title]
    #v(-0.3cm)
    #line(length: 100%, stroke: 1pt + maroon)
    #v(0.2cm)
  ])
}

// ==========================================
// CONTENT
// ==========================================

#intensive_header()

#v(0.2cm)
#text(size: 24pt, weight: "bold", fill: maroon)[The food of Indonesia]
#v(0.4cm)

// TASK 1: BEFORE READING
#box(width: 100%, stroke: 1pt + maroon, inset: 12pt, fill: maroon.lighten(95%))[
  #text(weight: "bold", fill: maroon, size: 12pt)[Task 1: Before you Read] \
  #text(style: "italic")[Look at the picture on the screen and heading. What is the text's purpose?]
  #v(0.2cm)
  #list(
    [To give an overview of the Indonesian food industry],
    [To compare the Indonesian food industry with food in the rest of the world],
  )
]

#v(0.6cm)

// READING PASSAGE (FULL WIDTH, NO INDENT)
#set par(first-line-indent: 0pt)

#text(weight: "bold", fill: maroon)[1] Situated in a warm, tropical region, Indonesia has a lot of rain and sunshine and therefore has the perfect climate for a long growing season. The country also has large areas of good-quality soil. Both factors make Indonesia an excellent region for a successful farming economy. A large percentage of the population works in the farming industry and the country gets a lot of income from this. There is a large range of farms, but most belong to three types: small farms growing rice for domestic use, small farms growing crops for export, and large, foreign-owned or privately-owned farms that also mostly export food.

#v(0.8em)
#text(weight: "bold", fill: maroon)[2] Indonesia's climate makes it ideal for planting and growing most popular crops. Indonesia is one of the world's largest producers of many different kinds of food. It is a known producer of palm oil and spices like cloves and cinnamon. It is also one of the biggest producers of other key foods consumers frequently buy such as cocoa, coffee, and tea. Growing plants to eat is obviously important, yet many farmers also plant other crops of high value such as natural rubber.

#v(0.8em)
#text(weight: "bold", fill: maroon)[3] The farming industry is clearly important for the country's economy, however, it has also influenced the local food culture and customs. Indonesia has a long history of cooking with herbs and spices. The Betawi, who are a local group in the region of Jakarta, are responsible for many of the street foods. Kerak Telor, which is possibly their most famous dish, is made of rice, coconut, onions, shrimp, and egg and fried into a cake. With thousands of street food stalls selling dishes for under one U.S. dollar they form an important part of the economy.

#v(0.8em)
#text(weight: "bold", fill: maroon)[4] As Indonesia has become richer and more urban the local diets have gradually changed. In particular, the amount of dairy, meat, and sugar people eat has grown. Many of these products and other processed foods and drink are often imported. A lot of people still prefer to shop in traditional local stores for their groceries, but supermarkets are selling an increasing amount of food to urban people. These stores mostly sell processed foods and often have better refrigerators to keep the dairy and meat products people demand.

#v(0.8em)
#text(weight: "bold", fill: maroon)[5] As lifestyles and diets change there are many challenges facing the Indonesian food industry. In the past, the country produced enough rice and sugar for everyone, but now it needs to import these foods. An increasing population, more land being used for crops people do not eat, and growing industries are all placing pressure on the future of food in Indonesia.

#v(0.8cm)

// TASK 2: GLOBAL READING
#section_header("Task 2: Global Reading")
#text(
  size: 10pt,
)[*Summaries* give an overview of the main ideas in a text. Read the topic sentences and identify the supporting information and important words to help you summarize the main ideas.]

#v(0.8cm)
#text(weight: "bold")[1 Skim the text and check (✔) the things that are mentioned.]
#v(0.5cm)
#grid(
  columns: (1fr, 1fr),
  row-gutter: 0.8cm,
  [#box(width: 12pt, height: 12pt, stroke: 1pt + dark-gray) challenges in the past],
  [#box(width: 12pt, height: 12pt, stroke: 1pt + dark-gray) changes to jobs],

  [#box(width: 12pt, height: 12pt, stroke: 1pt + dark-gray) challenges today],
  [#box(width: 12pt, height: 12pt, stroke: 1pt + dark-gray) local dishes],

  [#box(width: 12pt, height: 12pt, stroke: 1pt + dark-gray) changes to diet/shopping],
  [#box(width: 12pt, height: 12pt, stroke: 1pt + dark-gray) money for farmers],

  [#box(width: 12pt, height: 12pt, stroke: 1pt + dark-gray) plants and crops],
)

#v(1.5cm)
#block(breakable: false)[
  #text(weight: "bold")[2 Use your answers from Task 1 (Mentioned items) to complete a summary of the text.]
  #v(0.8cm)
  #set par(leading: 1.5em)
  Indonesia has a lot of rain and sunshine and produces different ¹ #box(width: 4cm, stroke: (bottom: 0.5pt + black)). These traditionally influence the food and a lot of herbs and spices are used in ² #box(width: 4cm, stroke: (bottom: 0.5pt + black)). \ #v(0.4cm)
  However, ³ #box(width: 4.5cm, stroke: (bottom: 0.5pt + black)) and ⁴ #box(width: 4.5cm, stroke: (bottom: 0.5pt + black)) habits are changing. Today people eat more processed foods. \ #v(0.4cm)
  People often buy groceries in local stores, but they also use supermarkets. One of the main ⁵ #box(width: 4cm, stroke: (bottom: 0.5pt + black)) for the food industry ⁶ #box(width: 4cm, stroke: (bottom: 0.5pt + black)) is the increasing population. It means more foods have to be imported.
]

#pagebreak()
// TASK 3: CLOSE READING
#section_header("Task 3: Close Reading")
#text(size: 10pt, style: "italic")[Read the text again. Write T (True), F (False), or NG (Not Given) for each sentence.]
#v(0.8cm)
#let tf_items = (
  "Very few people now work in farming in Indonesia.",
  "Indonesia does not produce any meat products.",
  "Herbs and spices are quite new in Indonesian cooking.",
  "People now eat more processed foods.",
  "Indonesia can produce all of the rice and sugar it needs today.",
)
#for (i, item) in tf_items.enumerate() {
  grid(
    columns: (1fr, auto),
    gutter: 1em,
    [#text(weight: "bold")[#(i + 1).] #item], [#box(width: 1.5cm, stroke: (bottom: 0.5pt + black))],
  )
  v(0.4cm)
}

#pagebreak()
// TASK 4: CRITICAL THINKING
#section_header("Task 4: Critical Thinking")
#text(size: 10pt, style: "italic")[Discuss these questions in a group.]
#v(0.8cm)
#text(
  weight: "bold",
)[1 What changes in diet have there been in Indonesia? Have you had similar changes in diet in your country?]
#v(0.4cm)
#text(size: 11pt, style: "italic", fill: maroon)[The diet in Indonesia has changed to ...]
#v(0.8cm)
#line(length: 100%, stroke: 0.5pt + dark-gray)
#v(0.4cm)
#text(size: 11pt, style: "italic", fill: maroon)[The diet in my country ...]
#v(0.8cm)
#line(length: 100%, stroke: 0.5pt + dark-gray)

#v(0.6cm)
#text(weight: "bold")[2 Why do you think people eat more processed foods today? What health problems might it cause?]
#v(0.4cm)
#text(size: 11pt, style: "italic", fill: maroon)[People's diets have changed because ...]
#v(0.8cm)
#line(length: 100%, stroke: 0.5pt + dark-gray)
#v(0.4cm)
#text(size: 11pt, style: "italic", fill: maroon)[Eating more processed foods can cause ...]
#v(0.8cm)
#line(length: 100%, stroke: 0.5pt + dark-gray)

// ==========================================
// ANSWER KEY
// ==========================================
#pagebreak()
#v(1cm)
#block(width: 100%, fill: slate-dark, inset: 12pt, [
  #text(fill: white, weight: "bold", size: 12pt)[ANSWER KEY (For Teacher Reference)]
])
#v(0.5cm)

#text(weight: "bold", fill: maroon)[Task 1: Before you Read] \
a (To give an overview of the Indonesian food industry)

#v(0.5cm)
#text(weight: "bold", fill: maroon)[Task 2: Global Reading] \
*1 Mentioned:* challenges today, local dishes, changes to diet and shopping, plants and crops, changes to jobs.
*2 Summary:* 1. plants/crops, 2. local dishes/cooking, 3. diet, 4. shopping, 5. challenges, 6. today.

#v(0.5cm)
#text(weight: "bold", fill: maroon)[Task 3: Close Reading] \
1. F, 2. F/NG, 3. F, 4. T, 5. F.

#v(0.5cm)
#text(weight: "bold", fill: maroon)[Task 4: Critical Thinking] \
Open answers.
