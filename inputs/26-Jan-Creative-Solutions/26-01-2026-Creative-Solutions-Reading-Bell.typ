#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 2cm, x: 2cm),
)
#set text(font: "Arial", size: 10.5pt, fill: rgb("#333333"))
#set par(leading: 1em, justify: true)

// BRAND COLORS
#let maroon = rgb("#A62D26")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#666666")

// --- COMPONENTS ---

#let bell_header() = {
  image("../../images/bell-header.jpg", width: 100%)
  v(0.5cm)
}

#let cinematic_title(title, image_path) = {
  block(width: 100%, height: 4.5cm, radius: 4pt, clip: true, [
    #image(image_path, width: 100%, height: 100%, fit: "cover")
    #place(center + horizon, 
      block(fill: rgb(166, 45, 38, 200), inset: 15pt, radius: 4pt,
        text(fill: white, size: 28pt, weight: "black", tracking: 0.1em)[#upper(title)]
      )
    )
  ])
  v(0.5cm)
}



#let city_box(title, image_path, body) = {
  block(width: 100%, stroke: 0.5pt + gray-line, radius: 4pt, clip: true, [
    #image(image_path, width: 100%, height: 3cm, fit: "cover")
    #block(inset: 10pt, [
      #text(weight: "bold", size: 13pt, fill: maroon)[#title]
      #v(0.4em)
      #body
    ])
  ])
}

// --- DOCUMENT ---

#bell_header()

#cinematic_title("Creative Solutions", "hero.png")

#text(weight: "bold", size: 12pt)[Task 1: Predictions]
#v(0.2cm)
#block(width: 100%, fill: maroon.lighten(90%), inset: 10pt, radius: 4pt, [
  Look at the title and pictures. What is the main problem the text is about? Circle one:
  #v(0.4em)
  #align(center)[#text(weight: "bold")[city noise \u{00A0} | \u{00A0} finding a job \u{00A0} | \u{00A0} high prices \u{00A0} | \u{00A0} pollution \u{00A0} | \u{00A0} stress \u{00A0} | \u{00A0} traffic]]
])

#v(0.8cm)

#grid(columns: (1fr, 1fr), gutter: 1.5cm,
  [
    #city_box("1. Curitiba, Brazil", "curitiba.png", [
      Over 40 years ago, one city in Brazil made one quick and important decision to reduce the number of cars. In just 72 hours, Curitiba turned its main business street into a pedestrian street. At first the project was not popular, but over time people saw it as positive. 
      
      The city later made 52 other roads pedestrian-only. People are using these areas for outdoor markets, concerts, and other events. The city has 16 parks and over a thousand green spaces. In 1970, each person had one square meter of green space, but today they have 52. 
    ])
  ],
  [
    #city_box("2. Murcia, Spain", "murcia.png", [
      In Murcia, a city in Spain, you can give your car to the city government if you don't want to use it. The idea is to get more public transportation in the city, and less car traffic. The city wants people to use its new, greener trams. 
      
      When they exchange their car, they get a free lifetime pass to use on any tram. Murcia is using its old cars in art projects around the city. The city wants to show the bad side of cars and the challenges of parking.
    ])
  ]
)

#v(0.5cm)

#city_box("3. La Paz, Bolivia", "la_paz.png", [
  La Paz, Bolivia, is one of the highest cities in the world, and it has some of the worst traffic. There are not enough vans to move passengers and the buses are often full. For the people who travel downtown from El Alto, a neighborhood up on a mountain, the trip is long, crowded, and tiring. 
  
  But a new cable car is making the trip easier. It is cutting travel time to just minutes while it saves many people over an hour of travel time each day. People go to and from downtown, high above the traffic. There is hope that the new cable car will reduce the number of cars on the road as well as reduce air pollution.
])

#v(0.8cm)

#block(breakable: false)[
  #text(weight: "bold", size: 12pt, fill: maroon)[Task 2: Global Reading]
  #v(0.4em)
  Skim the text and write the correct heading for each city profile (1-3). One heading is extra.
  #v(0.4em)
  #align(center)[#block(stroke: 1pt + maroon, inset: 8pt, radius: 4pt, [Exchange your cars \u{00A0} | \u{00A0} High in the sky \u{00A0} | \u{00A0} Putting pedestrians first \u{00A0} | \u{00A0} Solar-powered cars])]

  #v(0.2cm)
  #stack(spacing: 0.8cm,
    [1. Curitiba: #box(width: 1fr, stroke: (bottom: 1pt + black))],
    [2. Murcia: #box(width: 1fr, stroke: (bottom: 1pt + black))],
    [3. La Paz: #box(width: 1fr, stroke: (bottom: 1pt + black))]
  )
]

#v(1cm)

#block(breakable: false)[
  #text(weight: "bold", size: 12pt, fill: maroon)[Task 3: Close Reading - Which City?]
  #v(0.4em)
  Read the text. Which city does each statement describe? Check (\u{2713}).

  #table(
    columns: (1fr, auto, auto, auto),
    inset: 8pt,
    align: horizon,
    stroke: 0.5pt + gray-line,
    fill: (x, y) => if y == 0 { maroon } else if calc.even(y) { rgb("#F3F4F6") } else { white },
    [*Statement*], [*Curitiba*], [*Murcia*], [*La Paz*],
    [1. Its buses are often full.], [], [], [],
    [2. Drivers cannot drive on 52 roads.], [], [], [],
    [3. People ride trams for free if they give up their cars.], [], [], [],
    [4. People hope the solution reduces air pollution.], [], [], [],
    [5. It has more than 1,000 green spaces.], [], [], [],
  )
]

#v(1cm)

#block(breakable: false)[
  #text(weight: "bold", size: 12pt, fill: maroon)[Task 4: True or False]
  #v(0.4em)
  1. Curitiba made its main business street only for pedestrians. #h(1fr) [ T / F ]
  2. People cannot drive cars in Curitiba's streets anymore. #h(1fr) [ T / F ]
  3. People in Murcia can turn in any car if it is paid for. #h(1fr) [ T / F ]
  4. Murcia sends the old cars to other cities in Spain. #h(1fr) [ T / F ]
  5. El Alto is located in downtown La Paz. #h(1fr) [ T / F ]
  6. The cable car helps people get downtown faster. #h(1fr) [ T / F ]
]

#v(1cm)

#block(breakable: false)[
  #text(weight: "bold", size: 12pt, fill: maroon)[Task 5: Sentence Completion]
  #v(0.4em)
  Complete each sentence with *one or two words* from the text.
  1. People in Curitiba saw the pedestrian-only street as #box(width: 1fr, stroke: (bottom: 1pt + black)).
  2. Curitiba is working hard to save its #box(width: 1fr, stroke: (bottom: 1pt + black)).
  3. Murcia #box(width: 3cm, stroke: (bottom: 1pt + black)) its old cars in art projects around the city.
  4. Murcia wants to show the #box(width: 4cm, stroke: (bottom: 1pt + black)) of cars.
  5. La Paz hopes its cable car will #box(width: 3cm, stroke: (bottom: 1pt + black)) the number of cars.
]

#v(1cm)

#block(width: 100%, fill: maroon.lighten(95%), stroke: 1pt + maroon, inset: 15pt, radius: 4pt, [
  #text(weight: "bold", size: 12pt, fill: maroon)[Critical Thinking]
  #v(0.4em)
  1. Can any of these solutions work in your city? Why?
  2. What is another way to reduce the number of cars on our streets?
])

#pagebreak()
#text(weight: "bold", size: 14pt, fill: maroon)[Answer Key]
#v(0.5cm)
*Task 1:* traffic
*Task 2:* 1. Putting pedestrians first | 2. Exchange your cars | 3. High in the sky (Extra: Solar-powered cars)
*Task 3:* 1. La Paz | 2. Curitiba | 3. Murcia | 4. La Paz | 5. Curitiba
*Task 4:* 1. T | 2. F | 3. F | 4. F | 5. F | 6. T
*Task 5:* 1. positive | 2. natural environment | 3. is using | 4. bad side | 5. reduce
