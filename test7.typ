#set page(height: 5cm)
#set enum(numbering: "1.")

Test 1: baseline 100% line
+ #box(baseline: 100%)[#line(length: 3cm)]

Test 2: baseline 0% line
+ #box(baseline: 0%)[#line(length: 3cm)]

Test 3: underline text spaces
+ #underline(stroke: 0.75pt + black, offset: 2pt)[#h(3cm)]

Test 4: box with bottom stroke and h
+ #box(width: 3cm, stroke: (bottom: 0.75pt + black))[#h(3cm)]

Test 5: box with bottom stroke, height 1em, baseline 1em
+ #box(width: 3cm, height: 1em, stroke: (bottom: 0.75pt + black), baseline: 100%)
