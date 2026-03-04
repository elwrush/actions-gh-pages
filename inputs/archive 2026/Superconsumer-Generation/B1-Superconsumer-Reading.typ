#import "@local/bell-sheets:0.1.0": *

#set page(margin: (x: 2cm, top: 1.25cm, bottom: 1.25cm))
#set text(font: "Arial", size: 14pt)
#set par(leading: 0.55em, justify: true)

// ==========================================
// 1. HEADER & HERO
// ==========================================
#bell_header()

#hero_strap(
  "The Superconsumer Generation",
  "Analyzing the spending power and habits of Generation Y",
  hero_image: image("mall_hero.jpg"),
  badges: ("B1", "Reading"),
  image_align: top
)

#v(0.5em)
#block(fill: maroon.lighten(95%), inset: 8pt, radius: 2pt, width: 100%)[
  *Discuss these questions with a partner.* \
  1. Where do you shop most often? Do you shop in different places to other people in your family?
  2. What was the last thing you bought from a store?
]

#v(0.5em)

*1. Is the Dubai Mall for everyone?* \
At over a million square meters, and with over 1,200 stores, the Dubai Mall is huge in mall terms. The 750,000 people who visit it every week can find almost any product that meets their demands. Such mega-malls could be seen as a natural home for Generation Y, the biggest-spending and most demanding generation of consumers the world has ever seen.

#v(0.3cm)

*2.* #box(width: 10cm, stroke: (bottom: 1pt)) \
Generation Y is the name given to the group of people born between the late 1970s and mid-1990s. Their lives have happened at the same time as huge financial changes in the way we spend our money, and members of this group are demonstrating more and more financial behaviors across a range of countries and cultures.

#v(0.3cm)

*3.* #box(width: 10cm, stroke: (bottom: 1pt)) \
While their parents' generation knew many store owners personally when they were growing up, members of Generation Y are more likely to buy from huge multinational companies like Walmart. The biggest group of stores on the planet shows no signs of stopping. They grew from 8,500 stores in 15 countries in 2011 to over 11,500 stores in 28 different countries in 2015. That year Walmart made sales of just under 500 billion U.S. dollars, which is bigger than the GDP of 165 countries.

#v(0.3cm)

*4.* #box(width: 10cm, stroke: (bottom: 1pt)) \
While consumers of the Generation Y period can choose from a huge range of products at giant shopping malls, they have even more choice online. In just over a decade, Internet shopping saw huge growth. In the U.K., for example, consumers spent £800 million online in 2000; by 2015 this had grown to £114 billion. Amazon, the world's largest online store, sells such a wide variety of products they have to be kept in huge buildings the size of ten soccer fields.

#v(0.3cm)

*5.* #box(width: 10cm, stroke: (bottom: 1pt)) \
Gen Y-ers are the main target for many companies because of their spending power and attitude to shopping. In the U.S. alone, as a group they have \$170 billion to spend and 31% earn enough money to live the life they choose. Unfortunately for companies, they are considered the hardest group to sell to. A large portion of Generation Y claim they are not influenced by advertising. Instead, one in three read blogs to seek suggestions and reviews before deciding what to buy. The group does not like to be influenced and are unlikely to believe any advertising message, but they do expect companies to personally interact with them on social media.

#v(0.3cm)

*6.* #box(width: 10cm, stroke: (bottom: 1pt)) \
The older and richer Gen Y consumers become, the more important it is for companies to understand them. If a company can use technology to personalize its products and services, it might just gain some of the richest technology-loving customers in history.

// ==========================================
// 2. QUESTIONS (New Page)
// ==========================================
#pagebreak()
#badge("B1 Reading Questions")
#v(0.5em)

#block(breakable: false)[
  *Task 2:* #strong[Match the headings below with paragraphs 2–6. Paragraph 1 is an example.]
]

#v(0.4cm)
#block(inset: 12pt, stroke: 0.5pt + maroon, radius: 3pt, width: 100%, fill: maroon.lighten(98%))[
  #grid(columns: (1fr), row-gutter: 0.4cm,
    [*A.* Reading the future of shopping?],
    [*B.* Who is Generation Y?],
    [*C.* Why is Gen Y hard to influence?],
    [*D.* Are large stores still growing?],
    [*E.* How fast is online shopping growing?]
  )
]

#v(0.6cm)
#grid(columns: (1fr, 1fr), row-gutter: 0.8cm, column-gutter: 2cm,
  [Paragraph 1: #h(0.2cm) #text(style: "italic")[Example]],
  [Paragraph 4: #h(0.2cm) #box(width: 1fr, stroke: (bottom: 0.5pt))],
  [Paragraph 2: #h(0.2cm) #box(width: 1fr, stroke: (bottom: 0.5pt))],
  [Paragraph 5: #h(0.2cm) #box(width: 1fr, stroke: (bottom: 0.5pt))],
  [Paragraph 3: #h(0.2cm) #box(width: 1fr, stroke: (bottom: 0.5pt))],
  [Paragraph 6: #h(0.2cm) #box(width: 1fr, stroke: (bottom: 0.5pt))]
)

#v(1cm)
#block(breakable: false)[
  *Task 3:* #strong[Read the text again. Explain what the following numbers and terms refer to.]
]

#v(0.5cm)
#let items = (
  "1. A million square meters",
  "2. 750,000",
  "3. 15 and 28",
  "4. £800 million / £114 billion",
  "5. one in three"
)

#for item in items [
  #block(breakable: false)[
    *#item* #writing_lines_fixed(3, line-spacing: 0.9cm)
    #v(0.5cm)
  ]
]

#v(1cm)
#block(breakable: false)[
  *Task 4:* #strong[Read the sentences and circle True, False, or Not Given.]
]

#v(0.5cm)
#grid(columns: (1fr, 4cm), row-gutter: 0.5cm, column-gutter: 1cm,
  [1. Almost as many people go to the Dubai Mall every week as live in Dubai.], [T / F / NG],
  [2. Gen Y-ers were all born in the 1980s.], [T / F / NG],
  [3. People spend more on the Internet than in stores.], [T / F / NG],
  [4. 31% of Gen Y have enough money to live their desired lives.], [T / F / NG],
  [5. Gen Y-ers are not important consumers.], [T / F / NG],
)

// ==========================================
// 3. FULL ANSWER KEY (New Page)
// ==========================================
#pagebreak()
#badge("B1 Answer Key")
#v(0.5cm)

#block(inset: 8pt, fill: rgb("#F8FAFC"), radius: 4pt, width: 100%)[
  *Key Summary:* #h(1em) *(T2)* 2:B, 3:D, 4:E, 5:C, 6:A #h(2em) *(T4)* 1:NG, 2:F, 3:NG, 4:T, 5:F
]

#v(0.5cm)
#set text(size: 11pt)
#grid(columns: (1fr), row-gutter: 1.2em,
  [*P2:* Gen Y birth years (late 70s to mid-90s).],
  [*P3:* Walmart's physical expansion across 28 countries.],
  [*P4:* Online spending growth £800M -> £114B.],
  [*P5:* Attitude: Resist ads, trust blogs, want social interaction.],
  [*P6:* Importance: Technology-loving customers of the future.],
  [*Q1 (NG):* 750,000 visitors mentioned, but not the city population.],
  [*Q2 (F):* Born late 70s to mid-90s (includes late 70s and early 90s).],
  [*Q3 (NG):* Online spending increased, but total store sales not given.],
  [*Q4 (T):* "31% earn enough money to live the life they choose".],
  [*Q5 (F):* Described as "biggest-spending" and "target" generation.]
)
