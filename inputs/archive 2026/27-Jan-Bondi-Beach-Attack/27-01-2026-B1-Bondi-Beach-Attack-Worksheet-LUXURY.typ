#import "@local/elwrush:0.1.0": *

#show: luxury_worksheet.with(
  title: "Bondi Beach Attack",
  level: "B1",
  skill: "Critical Listening"
)

#task_card(1, "The Vocabulary of Crisis", "Match the terms to their contextual definitions.")[
  #v(0.4cm)
  #grid(
    columns: (1fr, 1fr),
    gutter: 20pt,
    [1. *Targeted*], [A. To remove a person's weapon.],
    [2. *Tight-knit*], [B. A specific, intended aim.],
    [3. *Disarm*], [C. Feeling excessive pressure.],
    [4. *Overwhelmed*], [D. Closely integrated community.],
  )
  #v(0.5cm)
  #text(size: 9pt, fill: slate-light)[*Notes:* Write the matching letter in your notebook.]
]

#task_card(2, "Gist & Atmosphere", "Listen to (00:00 - 01:00) and identify the central event.")[
  *What occurred at Bondi Beach, and who was the primary demographic gathered there?*
  
  #v(1cm)
  #dynamic_writing_lines()
]

#task_card(3, "The Hero’s Response", "Detail the actions of Ahmed Al Ahmed in the crisis.")[
  #block(breakable: false)[
    *Describe the physical intervention described in the report:* \
    #v(0.8cm) #line(length: 100%, stroke: 0.5pt + slate-light.lighten(50%))
  ]
]

#task_card(4, "Community Reflection", "Discuss the psychological importance of community integration.")[
  *Why is it important to have a "tight-knit" community during difficult times?*
  
  #v(1cm)
  #dynamic_writing_lines()
]
