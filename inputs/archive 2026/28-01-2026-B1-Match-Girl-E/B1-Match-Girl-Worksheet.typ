#import "@local/bell-sheets:0.1.0": *

#set page(margin: (x: 2cm, top: 1.25cm, bottom: 1.25cm))
#set text(size: 14pt)

#let quiz = json("match_girl_leveled_quizzes.json")
#let b1_questions = quiz.tasks.filter(t => t.level == "B1").map(t => t.questions).flatten()

// ==========================================
// 1. HEADER & STORY 
// ==========================================
#bell_header()

#hero_strap(
  "The Little Match Girl",
  "A Vision of Hope in the Cold",
  hero_image: image("assets/match_girl_1.jpg"),
  image_align: top
)

#v(0.5em)
#block(fill: maroon.lighten(95%), inset: 8pt, radius: 2pt, width: 100%)[
  *Introduction (B1)* - "The Little Match Girl" by Hans Christian Andersen (1845) explores the contrast between extreme poverty and the persistence of hope.
]

#v(0.5em)

#let text_b1 = read("little_match_girl_b1.txt")
#let paras = text_b1.split(regex("\r?\n\s*\r?\n")).filter(p => p.trim() != "")

#for p in paras [
  #eval(p.replace("[", "\[").replace("]", "\]"), mode: "markup")
  #v(0.3cm)
]

// ==========================================
// 2. QUESTIONS (New Page)
// ==========================================
#pagebreak()
#badge("B1 Reading Questions")
#v(0.5em)

#for (i, q) in b1_questions.enumerate() [
  #block(breakable: false)[
    *#(i+1).* #strong[#q.query] \
    #enum(numbering: "A.", ..q.choices)
    #v(0.15cm)
  ]
]

// ==========================================
// 3. FULL ANSWER KEY (New Page)
// ==========================================
#pagebreak()
#badge("B1 Answer Key (Full)")
#v(0.5em)

#let b1_summary = b1_questions.enumerate().map(((i, q)) => [*(#(i+1))* #("A", "B", "C", "D").at(q.answer)])

#block(inset: 8pt, fill: rgb("#F8FAFC"), radius: 4pt, width: 100%)[
  *Key Summary:* #h(1em) #b1_summary.join(h(1.5em))
]

#v(0.5cm)
#set text(size: 11pt)
#for (i, q) in b1_questions.enumerate() [
  #block(breakable: false)[
    *Q#(i+1): #q.query* \
    *Answer:* #("A", "B", "C", "D").at(q.answer) \
    *Explanation:* #q.explanation \
    #v(0.2cm)
  ]
]
