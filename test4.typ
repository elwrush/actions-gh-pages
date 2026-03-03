#set page(height: 5cm)
#set enum(numbering: "1.")
#grid(
  columns: (1fr, 1fr),
  [
    + #box(width: 3cm, stroke: (bottom: 0.75pt + black))
    + #box(width: 3cm, stroke: (bottom: 0.75pt + black))[#v(1em)]
    + #underline(offset: 4pt)[#h(3cm)]
    + #underline(offset: 2pt)[#h(3cm)]
    + #box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 25%)[ ]
  ]
)