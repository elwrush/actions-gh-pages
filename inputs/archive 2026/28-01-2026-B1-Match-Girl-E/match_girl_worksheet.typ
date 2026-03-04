
#import "@local/bell-sheets:0.1.0": *

#set page(margin: (x: 2cm, top: 1.25cm, bottom: 1.25cm))
#set text(size: 10.5pt)

#bell_header()

// B1 Narrative - Page 1
#hero_strap(
  "The Little Match Girl",
  "A Vision of Hope in the Cold",
  hero_image: image("assets/match_girl_1.jpg"),
  image_align: top
)

#v(0.5em)
#badge("Part 1: B1 Intermediate")
#v(0.5em)

#block(fill: maroon.lighten(95%), inset: 8pt, radius: 2pt, width: 100%)[
  *Introduction (Level B1)* - "The Little Match Girl" is a famous story by Hans Christian Andersen from Denmark (1845). It poignantly explores the contrast between extreme poverty and the persistence of hope.
]

#v(0.2cm)

#let text_b1 = read("little_match_girl_b1.txt")
#eval(text_b1.replace("[", "\[").replace("]", "\]"), mode: "markup")

#v(0.5cm) 
#badge("B1 Questions")
#v(0.5em)

#let quiz = json("match_girl_leveled_quizzes.json")

#let b1_questions = quiz.tasks.filter(t => t.level == "B1").map(t => t.questions).flatten()
#for (i, q) in b1_questions.enumerate() [
  #block(breakable: false)[
    *#(i+1).* #q.query \
    #enum(numbering: "A.", ..q.choices)
    #v(0.15cm)
  ]
]

#pagebreak()
#badge("Part 2: B1 Critical Thinking")
#v(0.5em)

#identity_block_sat()

#v(0.3cm)
*Writing Prompt:* Should we help the poor? Or should they just take care of themselves? Explain your answer with reasons and examples.

#writing_lines_dynamic(line-spacing: 0.9cm)

#pagebreak()

// B2 Narrative
#hero_strap(
  "The Little Match Girl",
  "A Vision of Hope in the Cold",
  hero_image: image("assets/match_girl_2.jpg"),
  image_align: center
)

#v(0.5em)
#badge("Part 3: B2 Upper Intermediate")
#v(0.5em)

#block(fill: maroon.lighten(95%), inset: 8pt, radius: 2pt, width: 100%)[
  *Introduction (Level B2)* - This classic 1845 narrative by Hans Christian Andersen remains a profound exploration of Victorian social inequality and the stark contrast between human suffering and spiritual transcendence.
]

#v(0.2cm)

#let text_b2 = read("little_match_girl_b2.txt")
#eval(text_b2.replace("[", "\[").replace("]", "\]"), mode: "markup")

#v(0.5cm) 
#badge("B2 Questions")
#v(0.5em)

#let b2_questions = quiz.tasks.filter(t => t.level == "B2").map(t => t.questions).flatten()
#for (i, q) in b2_questions.enumerate() [
  #block(breakable: false)[
    *#(i+1).* #q.query \
    #enum(numbering: "A.", ..q.choices)
    #v(0.15cm)
  ]
]

#pagebreak()

#badge("Part 4: B2 Philosophical Reflection")
#v(0.5em)

#identity_block_sat()

#v(0.3cm)
*Writing Prompt:* Evaluate the social responsibility of the community. Should intervention for the impoverished be a personal moral choice or a collective societal obligation? Support your argument with evidence from the text.

#writing_lines_dynamic(line-spacing: 0.9cm)

#pagebreak()

#badge("B1 Answer Key")
#v(0.5em)

#let b1_summary = b1_questions.enumerate().map(((i, q)) => [*(#(i+1))* #("A", "B", "C", "D").at(q.answer)])

#block(inset: 8pt, fill: rgb("#F8FAFC"), radius: 4pt, width: 100%)[
  *Summary:* #h(1em) #b1_summary.join(h(2em))
]

#v(0.5cm)
#set text(size: 9.5pt)
#for (i, q) in b1_questions.enumerate() [
  *Q#(i+1): #q.query* \
  *Answer:* #("A", "B", "C", "D").at(q.answer) \
  *Explanation:* #q.explanation \
  #v(0.2cm)
]

#pagebreak()

#badge("B2 Answer Key")
#v(0.5em)

#let b2_summary = b2_questions.enumerate().map(((i, q)) => [*(#(i+1))* #("A", "B", "C", "D").at(q.answer)])

#block(inset: 8pt, fill: rgb("#F8FAFC"), radius: 4pt, width: 100%)[
  *Summary:* #h(1em) #b2_summary.join(h(2em))
]

#v(0.5cm)
#set text(size: 9.5pt)
#for (i, q) in b2_questions.enumerate() [
  *Q#(i+1): #q.query* \
  *Answer:* #("A", "B", "C", "D").at(q.answer) \
  *Explanation:* #q.explanation \
  #v(0.2cm)
]
