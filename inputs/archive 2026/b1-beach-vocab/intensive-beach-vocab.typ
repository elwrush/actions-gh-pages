#import "@local/bell-sheets:0.1.0": *

#set enum(numbering: n => [*#n.*])

// Page Setup
#set page(
  margin: (x: 1.5cm, y: 1.5cm),
  header: none,
  footer: align(right, context counter(page).display())
)

// Document-wide Typography Standard: Arial 13pt
#set text(font: "Arial", size: 13pt, weight: "regular")
#let body_leading = 0.55em
#set par(leading: body_leading, justify: false)

// --- PAGE 1: Branded Header ---
#intensive_header()
#v(0cm)

#hero_strap(
  "At the Beach",
  "Vocabulary and Beach Activities",
  hero_image: image("images/hero.jpg"),
  badges: ("B1", "VOCABULARY") // NO 46 MINS Badge
)

#v(0.1cm)

// --- Section 1 (Single Column, Arial 13pt) ---
== AT THE COAST
Many people *spend* their holiday at the *coast* [the land close to the sea], where there are a lot of *seaside resorts* [towns by the sea for tourists] and they can go to the beach every day. Generally people prefer beaches that are *sandy* [with lots of sand], where you can go for a *stroll* [a casual walk] along the *shore* [the place where the sea meets the land] in the *sunshine* [when it is sunny]. On the beach, you also sometimes get a *breeze* [a nice gentle wind] that blows off the sea.

#v(0.1cm)
#align(left, image("images/coast_diagram_final.png", width: 45%))
#v(0.1cm)

#v(0.1cm)

#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr),
  column-gutter: 8pt,
  align: center + horizon,
  [#image("images/act_surfing_final.png", width: 100%)],
  [#image("images/act_windsurfing_final.png", width: 100%)],
  [#image("images/act_diving.png", width: 100%)],
  [#image("images/act_volleyball_final.png", width: 100%)],
  [#image("images/act_sunbathing.png", width: 100%)],
  [#text(size: 10pt)[*surfing*]],
  [#text(size: 10pt)[*windsurfing*]],
  [#text(size: 10pt)[*diving*]],
  [#text(size: 10pt)[*playing\ volleyball*]],
  [#text(size: 10pt)[*sunbathing*]]
)

#v(0.1cm)

== BEACH ACTIVITIES
Volleyball is a popular beach game and some people enjoy water sports such as *surfing*, *windsurfing* or *diving*. If the sea is *calm*, you can *go for a swim*, but a lot of people just want to lie on the beach and *sunbathe* and get a nice *(sun)tan*. However, there are now worries about the dangers of *sunbathing*. People who lie in the sun without any *protection* can get *sunburn*, and worse still, they are *at risk of* getting skin cancer. Doctors now *recommend* that people do not sit in the sun without using *sunscreen*. It may be safer just to sit in the *shade*.

#v(0.1cm)

#v(0.2cm)

// Reset to standard text
#set text(size: 13pt)

// Language Help Block (Pale Pink)
#block(
  fill: pale-pink,
  inset: 15pt,
  radius: 4pt,
  width: 100%,
  [
    #text(weight: "bold", fill: maroon)[LANGUAGE HELP]\
    #v(0.2cm)
    We can *go for a walk*, a *drive* (a journey in the car for pleasure), a *swim*, a *coffee* [drink some coffee], a *drink* (often an alcoholic drink, e.g. wine, beer). We can also *have a swim*, a *coffee*, a *drink*.\
    #v(0.1cm)
    _We went for a drive along the coast._\
    _I had a coffee at Caffee Nero._\
    _Let's go for a drink tonight._
  ]
)

#v(0.2cm)

// --- TASK SECTION (Single Column) ---
#task_header(1, "Words beginning with 'sun'")
Write down four more words beginning with *sun*.
#v(1.2cm)
#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr),
  column-gutter: 15pt,
  [sun *shine*],
  [sun #box(width: 1fr, stroke: (bottom: 1pt + black))],
  [sun #box(width: 1fr, stroke: (bottom: 1pt + black))],
  [sun #box(width: 1fr, stroke: (bottom: 1pt + black))],
  [sun #box(width: 1fr, stroke: (bottom: 1pt + black))]
)

#v(1.2cm)

#pagebreak()

#task_header(2, "Matching")
Match the words in the top row with the words in the bottom row by drawing lines.
#v(0.8cm)
#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  row-gutter: 2.5cm,
  align: center + top,
  [sun], [wind], [seaside], [sit in the], [sandy], [rough],
  [shade], [sea], [surfing], [tan], [resort], [beach]
)

#v(1.2cm)

#task_header(3, "Identify the Activity")
Look at the illustrations and identify the beach activity each person is doing.
#v(0.4cm)
#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr),
  column-gutter: 15pt,
  row-gutter: 10pt,
  // --- ROW 1: IMAGES (Horizontal Alignment Base) ---
  align(center + bottom, image("images/act_volleyball_final.png", width: 70%)),
  align(center + bottom, image("images/act_sunbathing.png", width: 70%)),
  align(center + bottom, image("images/act_surfing_final.png", width: 70%)),
  align(center + bottom, image("images/act_diving.png", width: 70%)),
  align(center + bottom, image("images/act_windsurfing_final.png", width: 70%)),
  
  // --- ROW 2: LABELS / LINEFILLS ---
  align(center + top, [*1.* _playing volleyball_]),
  align(center + top, [*2.* #box(width: 1fr, height: 0.6cm, stroke: (bottom: 1pt + black))]),
  align(center + top, [*3.* #box(width: 1fr, height: 0.6cm, stroke: (bottom: 1pt + black))]),
  align(center + top, [*4.* #box(width: 1fr, height: 0.6cm, stroke: (bottom: 1pt + black))]),
  align(center + top, [*5.* #box(width: 1fr, height: 0.6cm, stroke: (bottom: 1pt + black))]),
)

#v(1.2cm)

#task_header(4, "Word Choice")
Cross out the wrong answer.
#v(0.6cm)
#set enum(spacing: 0.6cm)
+ The beach was (*a* lovely / *b* #strike[calm] / *c* sandy / *d* dirty)
+ We went for a (*a* drive / *b* shop / *c* drink / *d* stroll)
+ The sea was (*a* sandy / *b* calm / *c* rough / *d* cold)
+ I enjoy (*a* surfing / *b* diving / *c* getting sunburn / *d* windsurfing)
+ We walked (*a* along the beach / *b* by the shore / *c* on the waves / *d* on the sand)
+ The beach was (*a* near the cliffs / *b* by the breeze / *c* by the rocks / *d* very sandy)

#v(1.2cm)

#task_header(5, "Sentence Completion")
Complete the sentences.
#v(1.0cm)
#set enum(spacing: 0.6cm)
+ I love sunbathing, so I can get a nice #underline[*suntan*].
+ Doctors #box(width: 5cm, stroke: (bottom: 1pt + black)) that you stay out of the sun completely in the middle of the day.
+ We used to sunbathe for hours, but then we didn't know we were at #box(width: 1fr, stroke: (bottom: 1pt + black)) \ of getting skin cancer.
+ I always take a beach umbrella to give me #box(width: 5cm, stroke: (bottom: 1pt + black)) from the sun when it is very hot.
+ In the city it feels like there's no air, but you often get a nice #box(width: 4cm, stroke: (bottom: 1pt + black)) by the sea.
+ I love going for a #box(width: 5cm, stroke: (bottom: 1pt + black)) along the beach, especially in the evening when it's quiet.
+ I don't like sitting in the sun; I prefer to sit in the #box(width: 5cm, stroke: (bottom: 1pt + black)).
+ We decided to #box(width: 4cm, stroke: (bottom: 1pt + black)) a swim before lunch.

#v(1.2cm)

#task_header(6, "Over to You")
Answer the questions.
#v(0.6cm)
#set enum(spacing: 0.9cm)
+ Do you ever spend time at seaside resorts? Where do you go, and how often?
+ Do you enjoy any of the beach activities mentioned above? Which ones?
+ Do you like sunbathing? Why? / Why not?
+ Do you get a suntan easily? Have you ever had sunburn? Do you often use sunscreen?
+ What do you like to do in the evening after a day on the beach?

#v(0.6cm)

#pagebreak()

#block(width: 100%, stroke: 1pt + maroon, inset: 20pt, radius: 4pt)[
  #text(size: 16pt, weight: "bold", fill: maroon)[ANSWER KEY]
  #v(0.5cm)
  #set text(size: 13pt)
  
  *Task 1: Words beginning with 'sun'* \
  Possible answers: sunshine (given), sunbathe, suntan, sunburn, sunscreen, sunblock, suncream.

  #v(0.3cm)
  *Task 2: Matching* \
  sun – tan; wind – surfing; seaside – resort; sit in the – shade; sandy – beach; rough – sea.

  #v(0.3cm)
  *Task 3: Identify the Activity* \
  #set enum(spacing: 0.1cm)
  + playing volleyball (given)
  + sunbathing
  + surfing
  + diving
  + windsurfing

  #v(0.3cm)
  *Task 4: Word Choice (Wrong answer crossed out)* \
  + calm
  + shop
  + sandy
  + getting sunburn
  + on the waves
  + by the breeze

  #v(0.3cm)
  *Task 5: Sentence Completion* \
  + suntan (given)
  + recommend
  + risk
  + protection
  + breeze
  + stroll
  + shade
  + have / go for.

  #v(0.3cm)
  *Task 6: Over to You* \
  Students' own answers.
]
