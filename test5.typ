#set page(height: 5cm)
#set enum(numbering: "1.")

Test 1: line with margin
+ #box(baseline: 50%)[#line(length: 3cm)]

Test 2: box with baseline
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 0%)

Test 3: box with baseline 50%
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 50%)

Test 4: just line
+ #line(length: 3cm)

Test 5: box with content space and baseline
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), baseline: 25%)[ ]

Test 6: box with outset
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt))
