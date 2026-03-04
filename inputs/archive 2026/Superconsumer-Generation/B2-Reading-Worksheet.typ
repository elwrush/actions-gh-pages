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
  badges: ("B2", "Reading"),
  image_align: top
)

#v(0.5em)
#block(fill: maroon.lighten(95%), inset: 8pt, radius: 2pt, width: 100%)[
  *Reflective Discussion:* How has your personal consumption behavior changed in the digital era? Do you prioritize convenience over local support?
]

#v(0.5em)

*1. Is the Dubai Mall for everyone?* \
Extending over a staggering million square meters and housing more than 1,200 individual retail outlets, the Dubai Mall is truly gargantuan even by ambitious global standards. Every week, approximately 750,000 visitors flock to this architectural marvel, finding nearly every conceivable product to satisfy their increasingly diverse requirements. Consequently, these colossal mega-malls serve as the quintessential hub for Generation Y—the most formidable, discerning, and fiscally active demographic of consumers the global market has ever witnessed in its history.

#v(0.3cm)

*2.* #box(width: 10cm, stroke: (bottom: 1pt)) \
The term "Generation Y" typically classifies a broad group of individuals born between the late 1970s and the mid-1990s. Their formative years and transition into adulthood have coincided with profound financial shifts in the way we perceive and spend our money. Furthermore, members of this particular demographic are increasingly exhibiting sophisticated and globalized financial behaviors that transcend national borders and cultural boundaries, potentially reshaping the global economic landscape for decades to come.

#v(0.3cm)

*3.* #box(width: 10cm, stroke: (bottom: 1pt)) \
In stark contrast to their parents' generation, who frequently enjoyed personal relationships with independent local shopkeepers while growing up, Generation Y individuals are far more inclined to patronize massive multinational corporations such as Walmart. This retail titan shows no indication of slowing its aggressive expansion; it grew from 8,500 locations in 15 countries in 2011 to a staggering 11,500 outlets across 28 nations by 2015. That same year, Walmart's annual revenue reached nearly 500 billion U.S. dollars—a figure that actually exceeds the Gross Domestic Product (GDP) of 165 different countries combined.

#v(0.3cm)

*4.* #box(width: 10cm, stroke: (bottom: 1pt)) \
While Generation Y consumers enjoy an unprecedented array of choices at monolithic shopping centers, their options are even more extensive in the digital realm. Over the course of a mere decade, online retail has undergone exponential and disruptive growth. In the United Kingdom, for instance, consumer e-commerce spending rose from £800 million in 2000 to a remarkable £114 billion by 2015. Amazon, currently the most dominant global online retailer, manages such an immense inventory that its products must be housed in colossal distribution centers, some of which are comparable in physical scale to ten professional soccer pitches.

#v(0.3cm)

*5.* #box(width: 10cm, stroke: (bottom: 1pt)) \
Generation Y represents the primary focus for modern corporations due to their significant purchasing power and distinct attitudes toward consumption. Within the United States, this demographic possesses an estimated \$170 billion in disposable income, with 31% earning enough to sustain their desired lifestyles and personal goals. Nevertheless, they are frequently cited by experts as the most challenging group to target effectively. A significant proportion of Generation Y asserts that they are largely indifferent to traditional advertising. Instead, one in three relies heavily on blogs and independent reviews to inform their purchasing decisions. Although they resist overt influence and remain skeptical of marketing slogans, they paradoxically expect brands to engage with them transparently and personally via social media platforms.

#v(0.3cm)

*6.* #box(width: 10cm, stroke: (bottom: 1pt)) \
As Generation Y consumers continue to mature and their individual wealth increases, it becomes progressively vital for corporations to develop a deep and nuanced understanding of their preferences. If a company can successfully leverage modern technology to customize its products and services, it stands to secure the long-term loyalty of some of the most affluent, demanding, and technologically literate customers in human history.

#v(0.5cm)

// --- QUESTIONS ---
#pagebreak()
#badge("B2 Reading Questions")
#v(0.5em)

#block(breakable: false)[
  *Task 2:* #strong[Select the most appropriate heading for paragraphs 2–6 from the list below.]
]

#v(0.4cm)
#block(inset: 12pt, stroke: 0.5pt + maroon, radius: 3pt, width: 100%, fill: maroon.lighten(98%))[
  #grid(columns: (1fr, 1fr), row-gutter: 0.4cm,
    [*A.* Refining Gen Y Identification], [*B.* Expansion of Multinational Titans],
    [*C.* Digital Commerce Revolution], [*D.* Navigating Marketing Resistance],
    [*E.* Projecting Future Dominance], []
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
  *Task 3:* #strong[Evidence Analysis. Explain the significance of these data points.]
]

#v(0.5cm)
#let items = (
  "1. Million square meters / 1,200 outlets",
  "2. late 1970s and the mid-1990s",
  "3. 500 billion U.S. dollars",
  "4. \$170 billion (US context)"
)

#for item in items [
  #block(breakable: false)[
    *#item* #writing_lines_fixed(3, line-spacing: 0.9cm)
    #v(0.5cm)
  ]
]

#v(1cm)
#block(breakable: false)[
  *Task 4:* #strong[Determine if the following statements are True, False, or Not Given.]
]

#v(0.5cm)
#grid(columns: (1fr, 4cm), row-gutter: 0.5cm, column-gutter: 1cm,
  [1. The passage suggests shopping malls are becoming obsolete.], [T / F / NG],
  [2. Gen Y behaviors differ across global territories.], [T / F / NG],
  [3. Personal shopper relationships are a feature of the current generation.], [T / F / NG],
  [4. Amazon's inventory scale is compared to professional sports facilities.], [T / F / NG],
  [5. Gen Y consumers value transparency and social media interaction.], [T / F / NG],
)

// ==========================================
// 3. FULL ANSWER KEY (New Page)
// ==========================================
#pagebreak()
#badge("B2 Answer Key")
#v(0.5cm)

#block(inset: 8pt, fill: rgb("#F8FAFC"), radius: 4pt, width: 100%)[
  *Key Summary:* #h(1em) *(T2)* 2:A, 3:B, 4:C, 5:D, 6:E #h(2em) *(T4)* 1:F, 2:F, 3:F, 4:T, 5:T
]

#v(0.5cm)
#set text(size: 11pt)
#grid(columns: (1fr), row-gutter: 1.2em,
  [*P2:* Identification based on chronological limits.],
  [*P3:* Walmart's status as a "retail titan" and expansion.],
  [*P4:* Scalability of digital commerce vs physical space.],
  [*P5:* Resisting overt influence while demanding engagement.],
  [*P6:* Loyalty of affluent and technology-literate customers.],
  [*Q1 (F):* Malls are "quintessential hubs", not becoming obsolete.],
  [*Q2 (F):* Text describes "sophisticated and globalized" behaviors.],
  [*Q3 (F):* This describes the parents' generation.],
  [*Q4 (T):* Explicit comparison to soccer pitches for scale.],
  [*Q5 (T):* "Value transparency and personally engage via social media".]
)
