#set page(height: 5cm)
#set enum(numbering: "1.")

Test 1: hide a inside box
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]

Test 2: hide a inside box WITHOUT outset
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black))[#hide[a]]

Test 3: transparent text
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#text(fill: rgb("00000000"))[a]]

Test 4: spacing box
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#v(0.8em)]

Test 5: space string
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[\ ]
