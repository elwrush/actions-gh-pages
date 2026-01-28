
#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 1.5cm, x: 2cm),
)
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.8em, justify: true)

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#666666") // Dark Gray for printer safety

// ==========================================
// 1. INTENSIVE HEADER (PRINTER SAFE)
// ==========================================
#align(center)[
  #v(0.5cm) // Top padding
  #image("../../images/intensive-header.jpg", width: 100%)
]
#v(0.3cm)

// ==========================================
// 2. STUDENT IDENTITY
// ==========================================
#block(width: 100%, inset: (bottom: 1em), [
  #grid(
    columns: (auto, 1fr, auto, 4cm),
    gutter: 1em,
    text(weight: "bold", fill: maroon)[Name:],
    line(start: (0pt, 0.8em), length: 100%, stroke: 0.5pt + black),
    text(weight: "bold", fill: maroon)[Student ID:],
    grid(
      columns: (1fr, 1fr, 1fr, 1fr, 1fr),
      gutter: 4pt,
      ..range(5).map(_ => box(width: 100%, height: 1.2em, stroke: (bottom: 1pt + black)))
    ),
  )
])

// ==========================================
// 3. COMPONENTS
// ==========================================
#let task_header(number, title) = {
  v(0.8cm)
  block(width: 100%, breakable: false, [
    #text(weight: "bold", fill: maroon, size: 14pt)[TASK #number: #title]
    #v(0.2cm)
    #line(length: 100%, stroke: 1.5pt + maroon)
    #v(0.4cm)
  ])
}

// ==========================================
// START WORKSHEET
// ==========================================

#task_header(1, "Pre-Listening Vocabulary")
Match the words (1-5) with their meanings (A-E). Write the letter in the box.

#v(0.5cm)

#grid(
  columns: (2cm, 5cm, 1fr, 2cm),
  gutter: 1cm,
  text(weight: "bold")[1.], [Targeted], [A. To remove a weapon from someone.], box(width: 100%, height: 1.2em, stroke: 1pt + black),
  text(weight: "bold")[2.], [Receiving treatment], [B. A very close and supportive community. ], box(width: 100%, height: 1.2em, stroke: 1pt + black),
  text(weight: "bold")[3.], [Disarm], [C. Feeling like something is too much to handle.], box(width: 100%, height: 1.2em, stroke: 1pt + black),
  text(weight: "bold")[4.], [Overwhelmed], [D. Being cared for by doctors in a hospital.], box(width: 100%, height: 1.2em, stroke: 1pt + black),
  text(weight: "bold")[5.], [Tight-knit], [E. Something aimed at a specific person or place.], box(width: 100%, height: 1.2em, stroke: 1pt + black),
)

#task_header(2, "Gist Listening")
#emph[Listen to the first part of the news report (00:00 - 01:00).] \
*What happened at Bondi Beach, and why were people gathered there?*

#v(2.5cm)
#line(length: 100%, stroke: 0.5pt + gray-line)
#v(1.5cm)
#line(length: 100%, stroke: 0.5pt + gray-line)

#task_header(3, "Listening for Detail")
#emph[Listen to the next part (01:00 - 02:15) and answer the questions.]

#block(breakable: false)[
  1. How many people were killed in the attack? \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + gray-line)
]

#v(0.8cm)

#block(breakable: false)[
  2. What is the status of the two gunmen? \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + gray-line)
]

#v(0.8cm)

#block(breakable: false)[
  3. Where did some people hide to stay safe? \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + gray-line)
]

#v(0.8cm)

#block(breakable: false)[
  4. How did Ahmed Al Ahmed help during the attack? \
  #v(0.8cm) #line(length: 100%, stroke: 0.5pt + gray-line)
]

#v(0.5cm)

#task_header(4, "Understanding Advice")
#emph[Listen to the advice for feeling better (02:15 - 03:30). Tick (#text(fill: maroon)[✓]) the boxes for advice mentioned in the report.]

#v(0.5cm)

#grid(
  columns: (auto, 1fr),
  gutter: 1.5em,
  box(width: 1.2em, height: 1.2em, stroke: 1pt + black), [Speak with a trusted adult if you feel worried.],
  box(width: 1.2em, height: 1.2em, stroke: 1pt + black), [Stay updated constantly by watching the news all day.],
  box(width: 1.2em, height: 1.2em, stroke: 1pt + black), [Take a break from the media if you need to relax.],
  box(width: 1.2em, height: 1.2em, stroke: 1pt + black), [Remember that it's unusual for this to happen here.],
  box(width: 1.2em, height: 1.2em, stroke: 1pt + black), [Look for the positive actions people are taking.],
)

#v(0.5cm)

#task_header(5, "Reflection")
*Why is it important to have a "tight-knit" community during difficult times? Write 2-3 sentences.*

#v(1.5cm) // The Gap
#let line-spacing = 1.1cm
#let rule-line = line(length: 100%, stroke: 0.5pt + gray-line)

#stack(spacing: line-spacing, ..range(5).map(_ => rule-line))

#v(0.8cm)

// ==========================================
// TRANSCRIPT
// ==========================================
#block(width: 100%, fill: maroon, inset: 10pt, [
  #text(fill: white, weight: "bold", size: 12pt)[TRANSCRIPT]
])

#v(0.1cm)
#text(size: 11pt)[
  #set par(leading: 0.6em, spacing: 1em)
  *REN [00:05]*: Ren here and welcome to this special edition of Newsbreak. BTN is meant to be on holidays just like many of you, but we're here today because of some very sad news you might have heard about where at least 15 people have died after an attack at Bondi Beach. Here's Michelle to explain what's going on.

  *MICHELLE [00:25]*: Today, people are laying flowers to honor the victims of a deadly terror attack that happened on Sunday, the 14th of December at Bondi Beach in Sydney. Two men with guns fired at an event in a park where members of Sydney's Jewish community had gathered to celebrate Hanukkah, an ancient Jewish festival.

  *REPORTER [00:46]*: It's our responsibility to wrap our arms around that wounded community and let them know that ordinary Australians, regular Australians are in their corner and thinking of them this morning after this terrible, terrible targeted attack on what should have been a joyful event.

  *CITIZEN [01:03]*: It's a very sad day for Australia, man. Like you know, like I've been in the country for 31 years. I never believed this could have happened something like that in Australia.

  *MICHELLE [01:11]*: At least 15 people have been killed and more than 40 are in hospital receiving treatment. Officials have confirmed that one gunman is dead and the other has been arrested. At the scene, emergency services responded quickly with police in the water, up above, and on the ground. Throughout all of this, there have been reports of acts of kindness and bravery.

  *SURVIVOR [01:37]*: We ran to the side of the surf club and then somebody came and opened the change room door and was ushering people inside. We just ran inside there and they closed the door and they said, "You're safe. You're safe."

  *MICHELLE [01:49]*: And one local man named Ahmed Al Ahmed has been called a hero by the New South Wales premier after he helped disarm one gunman.

  *CHRIS MINNS [01:58]*: To the brave responders, first responders, and including ordinary citizens who acted yesterday—thank you for what you do. People rushing towards danger to show the best of the Australian character. That's who we are.

  *REN [02:17]*: Trying to make sense of what happened and why can be really confusing and it's normal to feel overwhelmed and upset. But there are some things you can do that can help make you feel better. For starters, it's important to remember that this is in the news because for Australia, it's an incredibly rare event. And seeing something like this being talked about doesn't mean it will happen to you. Police say they've stopped the active threat and that they want everyone to feel safe.

  *REN [02:47]*: During and after events like this, news providers often highlight the most frightening images to get people's attention, which can make already upsetting events look even worse. But it's also important to focus on the good things happening. There are already examples of people coming together to help each other.

  *REN [03:04]*: Sharing how you feel and asking questions can also be a big help. If there's something you're worried about, you can talk to your parents, your teacher, or your friends. And there are also organizations you can reach out to if you need help, like Kids Helpline. And remember, if you need a break from the news, it's always okay to switch off—it doesn't mean you don't care.

  *POLITICIAN [03:30]*: Leaders here in Australia and around the world have reacted to the attack.

  *PETER DUTTON [03:35]*: What we saw yesterday was an act of pure evil, an act of anti-Semitism, an act of terrorism on our shores. This is a time where all Australians need to wrap our arms around Jewish Australians. These events will profoundly test and change our nation.

  *REPORTER [03:54]*: World leaders have also spoken out, including US President Donald Trump.

  *DONALD TRUMP [03:58]*: In Australia, as you know, there was a terrible attack. I just want to pay my respects to everybody. We pray for them and we pray for those who've lost their lives.

  *REPORTER [04:07]*: While many, including King Charles and UK Prime Minister Keir Starmer, have posted messages of support. During all this, people have been banding together, doing whatever they can to help and support one another. Take a look.

  *MICHELLE [04:23]*: Today, thousands of people gathered at Bondi in Sydney.

  *LOCAL RESIDENT [04:26]*: We are tight-knit. We're close. Everybody knows somebody who has been affected, and it truly is devastating.

  *MICHELLE [04:35]*: Across Australia, it was a similar story. Flags were flown at half-mast and memorials appeared on city streets. Online, there have been messages of support, including from some famous Aussies. While vigils have been held in many cities around the world.

  *VIGIL ATTENDEE [04:51]*: I believe we have to show an example of light wherever we are.
]

#pagebreak()

// ==========================================
// ANSWER KEY
// ==========================================
#v(1cm)
#block(width: 100%, fill: slate-dark, inset: 12pt, [
  #text(fill: white, weight: "bold", size: 12pt)[ANSWER KEY (For Teacher Reference)]
])

#v(0.5cm)

*Task 1:* 1-E, 2-D, 3-A, 4-C, 5-B

*Task 2:* There was a deadly terror attack where at least 15 people died. People were there to celebrate Hanukkah (Jewish festival).

*Task 3:*
1. At least 15 people.
2. One is dead, the other is arrested.
3. In a surf club / change room.
4. He helped disarm one of the gunmen.

*Task 4:* [✓] Speak with a trusted adult, [✓] Take a break from the media, [✓] It's unusual for this to happen, [✓] Look for the positive actions.
