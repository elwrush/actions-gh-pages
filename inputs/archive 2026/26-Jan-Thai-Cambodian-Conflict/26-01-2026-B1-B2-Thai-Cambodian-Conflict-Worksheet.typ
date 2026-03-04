
#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 2cm, x: 2cm),
)
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.8em, justify: true)

#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#666666")

// --- COMPONENTS ---

#let section_header(title) = {
  block(width: 100%, inset: (bottom: 0.5cm), [
    #text(weight: "bold", size: 14pt, fill: maroon)[#title]
    #v(-0.3cm)
    #line(length: 100%, stroke: 1.5pt + maroon)
  ])
}

#let identity_block() = {
  block(width: 100%, inset: (bottom: 1em), [
    #grid(
      columns: (auto, 1fr, auto, 4cm),
      gutter: 1em,
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

// --- DOCUMENT ---

#v(0.5cm)
#align(center)[#image("images/bell-header.jpg", width: 100%)]
#v(0.3cm)
#align(center)[
  #text(weight: "bold", size: 18pt)[The Thai-Cambodian Frontier Conflict] \
  #text(style: "italic", size: 12pt)[B1/B2 Integrated Skills]
]
#v(0.8cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  [
    #section_header("Task 1: The Situation")
    #block(radius: 4pt, clip: true)[#image("images/preah_vihear.jpg", width: 100%, height: 4.5cm, fit: "cover")]
    #v(0.4cm)
    Discuss the following with your partner:
    1. Look at the temple above. What do you know about the *Thai-Cambodian border*?
    2. Have you ever heard of the *Preah Vihear Temple*? Why is it a point of conflict?
    3. What does it mean to "flee"? Why would thousands of people do this?
  ],
  [
    #section_header("Vocabulary: Power Words")
    *Match the words to their meanings:*
    #v(0.4cm)
    #stack(spacing: 0.5cm,
      [1. **Mitigate** #h(1fr) [ #box(width: 0.6cm, stroke: (bottom: 1pt)) ]],
      [2. **Retaliate** #h(1fr) [ #box(width: 0.6cm, stroke: (bottom: 1pt)) ]],
      [3. **Ceasefire** #h(1fr) [ #box(width: 0.6cm, stroke: (bottom: 1pt)) ]],
      [4. **Evacuate** #h(1fr) [ #box(width: 0.6cm, stroke: (bottom: 1pt)) ]],
      [5. **Fractious** #h(1fr) [ #box(width: 0.6cm, stroke: (bottom: 1pt)) ]]
    )
    #v(0.4cm)
    #text(size: 9pt)[
      A. Move people to a safe place. \
      B. Make something less severe. \
      C. Hit back after being attacked. \
      D. Irritable and quarrelsome. \
      E. A temporary stop in fighting.
    ]
  ]
)

#pagebreak()

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  [
    #section_header("Task 2: The Complication")
    #image("images/cover_temple.png", width: 100%, height: 4cm, fit: "cover")
    #v(0.4cm)
    Watch the BBC Video (https://youtu.be/7vJxJyTWBmc). 
    
    *Question:* Is the situation currently resolving or escalating?
    #box(width: 100%, height: 1.2cm, stroke: 0.5pt + gray-line)
  ],
  [
    #section_header("Task 3: Detailed Analysis")
    #text(weight: "bold", fill: maroon)[B1: The Human Impact] \
    Identify three ways ordinary people are affected:
    1. #box(width: 1fr, repeat("."))
    2. #box(width: 1fr, repeat("."))
    3. #box(width: 1fr, repeat("."))
    
    #v(0.4cm)
    #text(weight: "bold", fill: maroon)[B2: The Diplomatic Friction] \
    Identify who made the following claims:
    - *"Targeting military sites"* \
    #box(width: 1fr, repeat("."))
    - *"Denied provoking violence"* \
    #box(width: 1fr, repeat("."))
  ]
)

#v(1cm)

#pagebreak()

#section_header("Task 4: The Resolution Task (Negotiation)")
#block(radius: 4pt, clip: true)[#image("images/shelter.jpg", width: 100%, height: 6cm)]
#v(0.6cm)

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  [
    #block(fill: rgb("#F8FAFC"), inset: 12pt, radius: 4pt, stroke: 1pt + maroon)[
      #text(weight: "bold", fill: maroon)[Role A: Humanitarian Aid (B1)] \
      The ceasefire has failed. Your team must propose a **3-step aid plan** for the families in the shelters.
      
      *Consider:*
      - Food and clean water
      - Medical help for "fragile people"
      - Temporary schools for students
    ]
  ],
  [
    #block(fill: rgb("#F8FAFC"), inset: 12pt, radius: 4pt, stroke: 1pt + maroon)[
      #text(weight: "bold", fill: maroon)[Role B: Mediation Memo (B2)] \
      Your team must draft a **3-point diplomatic protocol** to reduce blame and restart the transition.
      
      *Consider:*
      - Avoiding "accusatory language"
      - Neutral third-party observers
      - Joint border committee roles
    ]
  ]
)

#v(1cm)
#text(weight: "bold")[Your Group's Proposed Steps:]
#v(0.5cm)

#let line-spacing = 0.85cm
#let rule-line = line(length: 100%, stroke: 0.5pt + gray-line)
#context {
  let current-pos = here().position()
  let available = page.height - page.margin.bottom - current-pos.y
  let lines = int((available - 1cm) / line-spacing)
  stack(spacing: line-spacing, ..range(lines).map(_ => rule-line))
}

#pagebreak()
#section_header("Transcript: BBC News Report")
#set par(leading: 1.2em)
#text(size: 9.5pt)[
  #strong[PRESENTER [00:00]:] Several hundred thousand people in Thailand and Cambodia have been ordered to evacuate as a new wave of fighting erupted between the Southeast Asian neighbors. Both sides are blaming each other for starting the fighting. Thailand's air force said it struck Cambodian military targets along the disputed border, describing them as heavy weapons and combat personnel that could be a threat. Cambodia has denied provoking violence and has asked observers from the regional block ASEAN to investigate the Thai claims and urged them not to retaliate.

  #strong[PRESENTER [00:40]:] Well, let's speak now to Panisha Amocha who is following developments for us at the BBC. What is the latest?

  #strong[PENANISHA [00:50]:] So we recently just have the press conference from Thailand's Prime Minister who said that he believed in Thai military forces. According to the data that we received, the Thai military has deployed air strikes to target the Cambodian military sites and military positions. While in Cambodia, they said that they have not retaliated against Thailand at the moment. 

  #strong[PENANISHA [01:17]:] This confrontation is one of the most severe since the ceasefire back in July. We have seen images from both Thai and Cambodian sides of people in the border areas who have had to evacuate. A lot of people have moved to shelters or even to their relatives' houses, but there are still a lot of fragile people who have health issues who are still affected. Schools have been shut, meaning students cannot go to school on either side.

  #strong[PRESENTER [01:54]:] Okay. So both sides are taking steps to keep people safe in the meantime, but there is concern about what might happen next and how far this could escalate. What are people saying about that?

  #strong[PENANISHA [02:08]:] We have seen the Malaysian Prime Minister, Anwar Ibrahim, express concern about two hours ago that these confrontations will escalate. He has been trying to talk to the heads of state of both countries to try to negotiate and mitigate the conflict. On the Thai side, I've talked to a few local residents; they want this confrontation to end. This is not just happening now; it has affected their lives for many months. They have to stay in their houses and then evacuate to shelters; they cannot work. We can imagine that similar situations are happening on the Cambodian side as well.

  #strong[PENANISHA [02:55]:] What we really want to see is the two countries talk things out. They have a joint border committee to talk to each other, but it has been proven time and time again that this means is really not useful. When we have a third party, for example, the Malaysian Prime Minister, ASEAN, or even the US, trying to mitigate this, the two countries really want it to be effective.

  #strong[PRESENTER [03:23]:] Okay, Panisha. Thank you very much for bringing us right up to date. We have got a live page that's running at the moment on the BBC website and the news app as you can see here with the very latest details. We're keeping a very close eye on that fractious situation between the two countries.
]

#pagebreak()
#section_header("Answer Key")
#v(0.5cm)
#strong[Vocabulary Matching:] 1-B, 2-C, 3-E, 4-A, 5-D. \
#v(0.5cm)
#strong[Task 2 (Complication):] Escalating (violence and air strikes). \
#v(0.5cm)
#strong[Task 3 (B1):] 1. Evacuating to shelters; 2. Schools shut; 3. Health issues for fragile people. \
#v(0.5cm)
#strong[Task 3 (B2):] Thai military / Prime Minister; Cambodian government.
