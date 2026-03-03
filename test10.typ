#set page(height: 5cm)
#set enum(numbering: "1.")

Test 1: hide a inside box
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))[#hide[a]]

Test 2: hide a inside box WITHOUT outset
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black))[#hide[a]]

Test 3: empty box with height
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), height: 1em)

Test 4: line with text baseline
+ #box(baseline: 20%)[#line(length: 3cm, stroke: 0.75pt + black)]

Test 5: box with spacing inside
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black))[#v(0.8em)]

Test 6: box with invisible text
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black))[#text(fill: none)[a]]
