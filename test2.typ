#set page(height: 10cm)
#set enum(numbering: "1.")

Test 1: line
+ #line(length: 3cm)

Test 2: box with stroke
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))

Test 3: box with baseline
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 25%)

Test 4: underline of h
+ #underline(extent: 2pt, offset: 4pt)[#h(3cm)]

Test 5: box with content space
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black))[#v(1em)]
