
#import "@preview/meander:0.3.1"

// ============================================================
// BESPOKE FULL-WIDTH WORKSHEET: THE SUPERCONSUMER GENERATION
// Designed by Antigravity for Bell Language Centre
// ============================================================

#set page(
  paper: "a4",
  margin: (top: 1cm, bottom: 1.5cm, x: 2cm),
)
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.75em, justify: true)

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#666666")
#let pale-pink = rgb("#fceceb")

// --- UNIFIED STYLE FOR NUMBERS ---
#let p_num(n, underscores: true, title: "") = {
  text(font: "Arial", weight: "bold", fill: maroon, size: 12pt)[
    #n. #if underscores [#box(width: 8cm)[#repeat("_")]] else [#title]
  ]
}

// --- COMPONENTS ---

#let bell_header() = {
  v(0.2cm)
  align(center)[
    #image("../../images/bell-header.jpg", width: 100%)
  ]
  v(0.2cm)
}

#let hero_strap(title, subtitle) = {
  block(
    width: 100%,
    height: 5.5cm,
    radius: 4pt,
    clip: true,
    [
      #image("mall_hero.jpg", width: 100%, height: 100%, fit: "cover")
      #place(
        bottom + left,
        block(
          width: 100%,
          fill: rgb("#8B1538CC"),
          inset: 18pt,
          [
            #text(fill: white, weight: "bold", size: 24pt)[#upper(title)]
            #v(-10pt)
            #text(fill: white, size: 12pt, style: "italic")[#subtitle]
          ]
        )
      )
    ]
  )
}

#let task_header(num, title) = {
  block(breakable: false, width: 100%, inset: (top: 12pt, bottom: 6pt), [
    #stack(dir: ltr, spacing: 12pt,
      box(fill: maroon, inset: 5pt, radius: 2pt, text(fill: white, weight: "bold", size: 9pt)[TASK #num]),
      align(horizon, text(weight: "bold", fill: maroon, size: 12pt)[#upper(title)])
    )
  ])
}

#let identity_block() = {
  block(width: 100%, inset: (y: 1.5em), [
    #grid(
      columns: (auto, 1fr, auto, 4cm),
      gutter: 1.5em,
      text(weight: "bold", fill: maroon)[Name:],
      line(start: (0pt, 0.8em), length: 100%, stroke: 0.5pt + black),
      text(weight: "bold", fill: maroon)[Student ID:],
      grid(
        columns: (1fr, 1fr, 1fr, 1fr, 1fr),
        gutter: 4pt,
        ..range(5).map(_ => box(width: 100%, height: 1.2em, stroke: (bottom: 1pt + black)))
      ),
    )
  ])
}

#let rule_line = line(length: 100%, stroke: 0.5pt + gray-line)
#let writing_lines(count) = {
  let line-spacing = 1.1cm
  v(0.5cm)
  stack(spacing: line-spacing, ..range(count).map(_ => rule_line))
}

// --- DOCUMENT ---

// PAGE 1
#bell_header()
#hero_strap("The Superconsumer Generation", "Analyzing the spending power and habits of Generation Y")

#task_header("1", "Before You Read")
#block(fill: pale-pink, width: 100%, inset: 15pt, radius: 4pt, [
  *Discuss these questions with a partner.*
  1. Where do you shop most often? Do you shop in different places to other people in your family?
  2. What was the last thing you bought from a store?
])

#v(0.8cm)

#p_num(1, underscores: false, title: "A mall for a new generation of consumers")
#v(4pt)
At over a million square meters, and with over 1,200 stores, the Dubai Mall is huge in mall terms. The 750,000 people who visit it every week can find almost any product that meets their demands. Such mega-malls could be seen as a natural home for Generation Y, the biggest-spending and most demanding generation of consumers the world has ever seen.

#v(0.6cm)
#p_num(2)
#v(4pt)
Generation Y is the name given to the group of people born between the late 1970s and mid-1990s. Their lives have happened at the same time as huge financial changes in the way we spend our money, and members of this group are demonstrating more and more financial behaviors across a range of countries and cultures.

#v(0.6cm)
#p_num(3)
#v(4pt)
While their parents' generation knew many store owners personally when they were growing up, members of Generation Y are more likely to buy from huge multinational companies like Walmart. The biggest group of stores on the planet shows no signs of stopping. They grew from 8,500 stores in 15 countries in 2011 to over 11,500 stores in 28 different countries in 2015. That year Walmart made sales of just under 500 billion U.S. dollars, which is bigger than the GDP of 165 countries.


#v(0.6cm)

#pagebreak()
// PAGE 2
#meander.reflow({
  import meander: *
  
  placed(
    top + right,
    block(
      width: 6.5cm,
      radius: 6pt,
      clip: true,
      image("phone_pixabay.jpg", width: 100%)
    )
  )

  container()

  content[
    #set text(size: 10pt)
    #p_num(4) \
    While consumers of the Generation Y period can choose from a huge range of products at giant shopping malls, they have even more choice online. In just over a decade, Internet shopping saw huge growth. In the U.K., for example, consumers spent £800 million online in 2000; by 2015 this had grown to £114 billion. Amazon, the world's largest online store, sells such a wide variety of products they have to be kept in huge buildings the size of ten soccer fields.

    #v(0.8cm)
    #p_num(5) \
    Gen Y-ers are the main target for many companies because of their spending power and attitude to shopping. In the U.S. alone, as a group they have \$170 billion to spend and 31% earn enough money to live the life they choose. Unfortunately for companies, they are considered the hardest group to sell to. A large portion of Generation Y claim they are not influenced by advertising. Instead, one in three read blogs to seek suggestions and reviews before deciding what to buy. The group does not like to be influenced and are unlikely to believe any advertising message, but they do expect companies to personally interact with them on social media.

    #v(0.8cm)
    #p_num(6) \
    The older and richer Gen Y consumers become, the more important it is for companies to understand them. If a company can use technology to personalize its products and services, it might just gain some of the richest technology-loving customers in history.
  ]
})

#v(0.5cm)

#task_header("2", "Global Reading")
*Match the headings below with paragraphs 2–6.*
#grid(columns: (auto, 1fr), row-gutter: 1.5em, column-gutter: 1cm,
  [The growth of online sales:], [#box(width: 3cm)[#repeat("_")]],
  [The growth of large stores:], [#box(width: 3cm)[#repeat("_")]],
  [Generation Y’s future importance:], [#box(width: 3cm)[#repeat("_")]],
  [What is Generation Y?:], [#box(width: 3cm)[#repeat("_")]],
  [Generation Y is hard to influence:], [#box(width: 3cm)[#repeat("_")]]
)

#pagebreak()

// PAGE 3
#v(0.5cm)

#task_header("3", "Close Reading")
*Read the text again. What do the following numbers refer to?*
#grid(columns: (auto, 1fr), row-gutter: 2.5em, column-gutter: 0.8cm,
  [1. A million square meters:], [#box(width: 100%)[#repeat("_")]],
  [2. 750,000:], [#box(width: 100%)[#repeat("_")]],
  [3. 15 and 28:], [#box(width: 100%)[#repeat("_")]],
  [4. £800 million and £114 billion:], [#box(width: 100%)[#repeat("_")]],
  [5. one in three:], [#box(width: 100%)[#repeat("_")]]
)

#v(1cm)

#task_header("4", "True, False, or Not Given")
#block(width: 100%, stroke: 0.5pt + gray-line, inset: 15pt, radius: 4pt, [
  #grid(columns: (1fr, 4cm), gutter: 12pt,
    [1. Visitors at Dubai Mall match Dubai's population.], [T / F / NG],
    [2. Gen Y-ers were all born in the 1980s.], [T / F / NG],
    [3. People spend more on the Internet than in stores.], [T / F / NG],
    [4. 31% of Gen Y have enough money for their desired life.], [T / F / NG],
    [5. Gen Y-ers are not important consumers.], [T / F / NG],
  )
])

#pagebreak()

// PAGE 4: ANSWER KEY
#v(3cm)
#align(center + horizon)[
  #block(width: 80%, fill: maroon, inset: 20pt, radius: 4pt, [
    #text(fill: white, weight: "bold", size: 14pt)[ANSWER KEY (TEACHER)] \
    #v(1cm)
    #text(fill: white, size: 12pt, weight: "bold")[Task 2 (Global Matching):] \
    #text(fill: white.darken(5%), size: 11pt)[4. Online growth | 3. Large stores | 6. Future status | 2. What is Gen Y? | 5. Hard to influence] \
    #v(0.5cm)
    #text(fill: white, size: 12pt, weight: "bold")[Task 4 (True/False/Not Given):] \
    #text(fill: white.darken(5%), size: 11pt)[1. NG | 2. F | 3. NG | 4. T | 5. F]
  ])
]

#pagebreak()

// PAGE 5: REFLECTION
#bell_header()
#task_header("5", "Critical Thinking")
#block(fill: pale-pink, inset: 20pt, radius: 6pt, width: 100%, [
  #text(size: 14pt, weight: "bold", fill: maroon)[Think about how you shop and how your parents’ and grandparents’ generations shopped. Are they different from you? Why?]
])

#v(1.5cm)
#identity_block()
#v(1cm)
#text(weight: "bold", fill: maroon, size: 12pt)[Your response (min. 70 words):]
#writing_lines(10)

#pagebreak()

// PAGE 6 & 7 (B2 EXTENSION)
#block(width: 100%, fill: maroon, inset: 15pt, [
  #text(weight: "bold", fill: white, size: 20pt)[B2 READING EXTENSION]
  #h(1fr)
  #text(size: 11pt, style: "italic", fill: white)[Differentiated Input]
])

#set par(leading: 1.25em)

#v(0.6cm)
#p_num(1, underscores: false, title: "(B2 Extension)") \
Extending over a staggering million square meters and housing more than 1,200 individual retail outlets, the Dubai Mall is truly gargantuan even by ambitious global standards. Every week, approximately 750,000 visitors flock to this architectural marvel, finding nearly every conceivable product to satisfy their increasingly diverse requirements. Consequently, these colossal mega-malls serve as the quintessential hub for Generation Y—the most formidable, discerning, and fiscally active demographic of consumers the global market has ever witnessed in its history.

#v(0.6cm)
#p_num(2, underscores: false, title: "(B2 Extension)") \
The term "Generation Y" typically classifies a broad group of individuals born between the late 1970s and the mid-1990s. Their formative years and transition into adulthood have coincided with profound financial shifts in the way we perceive and spend our money. Furthermore, members of this particular demographic are increasingly exhibiting sophisticated and globalized financial behaviors that transcend national borders and cultural boundaries, potentially reshaping the global economic landscape for decades to come.

#v(0.6cm)
#p_num(3, underscores: false, title: "(B2 Extension)") \
In stark contrast to their parents' generation, who frequently enjoyed personal relationships with independent local shopkeepers while growing up, Generation Y individuals are far more inclined to patronize massive multinational corporations such as Walmart. This retail titan shows no indication of slowing its aggressive expansion; it grew from 8,500 locations in 15 countries in 2011 to a staggering 11,500 outlets across 28 nations by 2015. That same year, Walmart's annual revenue reached nearly 500 billion U.S. dollars—a figure that actually exceeds the Gross Domestic Product (GDP) of 165 different countries combined.

#v(0.6cm)
#p_num(4, underscores: false, title: "(B2 Extension)") \
While Generation Y consumers enjoy an unprecedented array of choices at monolithic shopping centers, their options are even more extensive in the digital realm. Over the course of a mere decade, online retail has undergone exponential and disruptive growth. In the United Kingdom, for instance, consumer e-commerce spending rose from £800 million in 2000 to a remarkable £114 billion by 2015. Amazon, currently the most dominant global online retailer, manages such an immense inventory that its products must be housed in colossal distribution centers, some of which are comparable in physical scale to ten professional soccer pitches.

#v(0.6cm)
#p_num(5, underscores: false, title: "(B2 Extension)") \
Generation Y represents the primary focus for modern corporations due to their significant purchasing power and distinct attitudes toward consumption. Within the United States, this demographic possesses an estimated \$170 billion in disposable income, with 31% earning enough to sustain their desired lifestyles and personal goals. Nevertheless, they are frequently cited by experts as the most challenging group to target effectively. A significant proportion of Generation Y asserts that they are largely indifferent to traditional advertising. Instead, one in three relies heavily on blogs and independent reviews to inform their purchasing decisions. Although they resist overt influence and remain skeptical of marketing slogans, they paradoxically expect brands to engage with them transparently and personally via social media platforms.

#v(0.6cm)
#p_num(6, underscores: false, title: "(B2 Extension)") \
As Generation Y consumers continue to mature and their individual wealth increases, it becomes progressively vital for corporations to develop a deep and nuanced understanding of their preferences. If a company can successfully leverage modern technology to customize its products and services, it stands to secure the long-term loyalty of some of the most affluent, demanding, and technologically literate customers in human history.
