#import "/lib/typst/lib.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 1.5cm, x: 2cm))
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: true)

// Standard List Spacing
#set enum(spacing: 1.5em, indent: 0.5em)
#set list(spacing: 0.8em, indent: 1.5em)

#intensive_header()

#v(0.5cm)

#align(center)[
  #text(size: 18pt, weight: "bold", fill: maroon)[DIGITAL INFLUENCE & THE GENERATION GAP]
]

#v(0.5cm)

#task_header(1, "Listening Strategy")

#block(
  fill: pale-pink,
  inset: 12pt,
  radius: 4pt,
  width: 100%,
  [
    #text(weight: "bold", fill: maroon)[Listening strategy: Answering multiple-choice questions] \
    When you have a multiple-choice listening task, underline key words in each question before you look at the options.
  ]
)

#v(1em)

+ What's the main topic of today's show?
  #set enum(numbering: "a.", spacing: 0.6em)
  + psychology
  + parent–teen relationships
  + medical issues
  + teen friendship

+ What does Dr. Schmidt do?
  #set enum(numbering: "a.", spacing: 0.6em)
  + helps families to improve communication
  + researches how teens learn
  + advises schools on teenage issues
  + studies how teens use media

+ What does the host say about YouTube?
  #set enum(numbering: "a.", spacing: 0.6em)
  + Parents want to stop their teenage children from watching YouTube.
  + Parents think their children learn a lot from YouTube.
  + Teens don't believe what they hear on YouTube.
  + YouTubers have a lot of influence on teens.

+ What does Dr. Schmidt's research show?
  #set enum(numbering: "a.", spacing: 0.6em)
  + Parents influence teenagers in some ways.
  + YouTubers influence parents through their teenage children.
  + Parents don't understand teenagers.
  + Teens don't understand adults.

+ What does Dr. Schmidt say about education, finance, health and well-being?
  #set enum(numbering: "a.", spacing: 0.6em)
  + Parents and teenagers can't communicate about these topics.
  + YouTubers help teenagers understand these important issues.
  + Teenagers consider their parents' opinions when making decisions about these topics.
  + Teenagers don't want to think about them.

#v(1.5em)

#task_header(2, "Listening for Detail")
_Listen and write your answers to the questions. Then compare your answers with the options and choose the closest one._

#v(1em)

#task_header(3, "Check Your Answers")
_Listen again and check your answers._

#v(1.5em)

#task_header(4, "Speaking")
Complete the dialogue with phrases a–g.

#v(0.5em)

#grid(
  columns: (1fr, 1fr),
  gutter: 8pt,
  [a. Have you ever considered], [e. Perhaps you could],
  [b. OK, you've persuaded me.], [f. Sorry, I'm not convinced],
  [c. it really helped], [g. You might not realize this, but],
  [d. I know someone], []
)

#v(1cm)

// Define a gapfill rule box
#let gap = box(width: 3.5cm, stroke: (bottom: 0.5pt + black), baseline: 25%)

// Increase leading for double spacing in this block
#block(inset: (left: 10pt), [
  #set par(leading: 1.5em)
  *Art*: Have you seen this ad for the archery club? I went last week, and it was great. 1 #gap doing something like that? \
  *Bea*: Archery? No, it isn't for me. I'm not very good at sports. \
  *Art*: I think it's different from other sports. 2 #gap a few kids from our class go – not just me. 3 #gap who tried it last year and she said 4 #gap her feel more confident about sports. \
  *Bea*: 5 #gap I just can't see myself trying to shoot a target with an arrow! \
  *Art*: You should try it. 6 #gap just come for a trial session and see if you like it. I love it! And we always have pizza afterwards! \
  *Bea*: 7 #gap I'll go to the next meeting. When is it?
])

#v(1.5em)

#task_header(5, "Dialogue Writing")
Write a dialogue. Choose one of the situations or use your own idea. Use phrases from exercise 4.
- Try to convince your friend to take up a hobby that you enjoy.
- Try to persuade your friend to listen to a new musical group.
- Try to get a friend to read a book that you really like.

#pagebreak()

#v(0.5cm)

#align(center)[#text(size: 14pt, weight: "bold", fill: maroon)[AUDIO TRANSCRIPT]]

#v(0.5cm)

#set text(size: 10.5pt)
#set par(leading: 0.8em)

*Tom*: OK, welcome back to *Tom's World*. I'm Tom Adams, and this podcast is about my world – and I hope, your world, too. Today I'm looking at family life – specifically at teens and whether or not teenagers and their parents can ever really understand each other. So, while I'm an expert on being a teenager – because I am one – I thought I'd ask another expert. I'm here today with psychologist Doctor Lisa Schmidt, who studies teenagers – specifically teenagers and media – the internet, video games, TV, and so on. Hello, Dr. Schmidt! \
*Dr. Schmidt*: Hello. Thanks for having me on the show. \
*Tom*: We're happy to have you here. So, we're talking today about the generation gap, and what some parents would call the trouble with teenagers. Doctor Schmidt, we've heard a lot recently about how YouTube is one of the main influences on young people today, and how parents are worried about that. It's where we look for the latest styles, and for a lot of products we buy. It seems that the biggest influence in our lives comes from the YouTubers we follow. Do you agree with that analysis? \
*Dr. Schmidt*: Well ... yes and no. I mean, I don't deny the importance of online personalities in the lives of young people, but my own research shows that there's more to the story. \
*Tom*: Oh, really? \
*Dr. Schmidt*: Yes. You might not realize this, but even today, parents are still a big influence on their kids in some very important ways. \
*Tom*: Sorry, I'm not convinced. I mean – if my mom tried to tell me what to wear ... \
*Dr. Schmidt*: Well, sure. I mean, for questions of clothes and style, of course teens turn to the internet a lot. But what about personal finances – looking after your money? Or education? Have you considered talking with your parents about your choice of university? \
*Tom*: Of course. We talk about it a lot – because they're going to pay for it. But that's different. \
*Dr. Schmidt*: Exactly. What my research shows is that when it comes to some big things in life – career choice, education, finance, health and well-being – parents actually still have a lot of influence, and a lot of parents and teens communicate often about these topics. \
*Tom*: Now that *is* interesting. \
*Dr. Schmidt*: I think so. Everyone's always ready to say that the generation gap means parents and teens simply can't communicate, or that parents have no influence. But we can see that in some very important areas, kids still listen to their parents. Well, that's what my research shows, anyway. \
*Tom*: I hadn't thought about it that way before. I wonder if we can go into this a little more deeply ....
