#set page(height: 5cm)
#set enum(numbering: "1.")

Test 1: baseline 0pt
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 0pt)

Test 2: repeat text space
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black))[#hide[#repeat[ ]]]

Test 3: baseline with text
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 0pt)[#hide[1.]]

Test 4: line shifted
+ #box(width: 3cm)[#line(length: 3cm, stroke: 0.75pt + black)]
