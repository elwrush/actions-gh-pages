#import "@local/bell-sheets:0.1.0": *

#set page(
  margin: (x: 2cm, top: 1.25cm, bottom: 1.25cm),
  footer: align(right, text(size: 8pt, fill: gray)[Bell Language Centre | B2 Vocabulary])
)

#set text(font: "Arial", size: 13pt, fill: slate-dark)
#set par(leading: 0.55em, justify: false)

// --- BRANDING ---
#bell_header()
#v(0.1cm)
#hero_strap(
  "Holidays",
  "B2 Vocabulary & Essential Phrases",
  hero_image: image("images/hero_holiday.jpg"),
  badges: ("B2", "Vocab")
)

#v(1cm)

// --- SECTION A ---
#text(weight: "bold", fill: maroon)[A. Here are a number of different places where you can spend a holiday.]
#v(0.2cm)
- *camp site*: a place where you can pitch a tent or park a caravan
- *self-catering flat*: flat which you rent, you cook for yourself
- *guesthouse*: accommodation like a hotel but cheaper and with fewer services
- *youth hostel*: cheap accommodation, mainly for young people, with, perhaps, ten or more people sleeping in bunk beds in one room
- *holiday camp*: a place providing holiday accommodation in little chalets or flats, with restaurants, bars, swimming pools and lots of other facilities and entertainment
- *time-share apartment*: accommodation which one owns, say, a 26th part of and so has the right to stay there for 2 weeks every year

#v(0.6cm)

// --- SECTION B ---
#text(weight: "bold", fill: maroon)[B. Here are a number of different things which people like to do on holiday.]
#v(0.2cm)
- sunbathe
- swim or go swimming
- do some or go sightseeing
- ski or go skiing
- go for a drive
- hike or go hiking
- tour or go touring
- go on an excursion
- climb or go climbing/mountaineering
- camp or go camping

#v(0.6cm)
#block(fill: pale-pink, inset: 12pt, radius: 4pt, width: 100%)[
  *Note:* You usually ask 'Have you ever been skiing/hang-gliding?' rather than 'Have you ever gone?' 'He's been wind-surfing' means that at some point in his life he has done this.
]

#v(0.6cm)

// --- SECTION C ---
#text(weight: "bold", fill: maroon)[C. Here is some useful language for when you are staying in a hotel.]
#v(0.4cm)
- I'd like to book a single/double room with a cot.
- I'd like a room with a shower, a colour TV, and a view of the sea.
- What time do you serve breakfast?
- Am I too late for dinner/to get something to eat?
- Is service included?
- Could I have a call at 7.30, please?
- Could we have dinner in our room, please?
- The teasmade [tea-making machine] in my room isn't working.
- I'd like an extra pillow, please.
- I'd like to make a call to New Zealand, please.
- What time do you like rooms to be vacated by?
- Sorry to bother you, but...
- I'm afraid there's something wrong with the..., could you have a look at it?

#v(0.8cm)

// --- TASK 1 ---
#task_header(1, "Personal Experience")
#v(0.2cm)
#text(style: "italic")[Which of the holiday places in A have you or any of your friends stayed at? What are the advantages and disadvantages of each? Try and note down at least one advantage and one disadvantage for each even if you have no direct personal experience of them.]

#v(0.6cm)
#writing_lines_fixed(3, line-spacing: 1.1cm)

#v(0.8cm)

#pagebreak()

// --- TASK 2 ---
#task_header(2, "Preferences")
#v(0.2cm)
#text(style: "italic")[List the ten activities shown in B opposite according to your personal preferences.]

#v(0.6cm)
#grid(
  columns: (1fr, 1fr),
  column-gutter: 1.5cm,
  row-gutter: 1.2cm,
  ..range(1, 11).map(i => {
    stack(dir: ltr, spacing: 12pt,
      badge(str(i), fill_color: slate-dark),
      align(bottom, box(width: 1fr, stroke: (bottom: 0.5pt + gray), inset: (bottom: 2pt))[])
    )
  })
)

#v(0.8cm)

// --- TASK 3 ---
#task_header(3, "Verb Forms: Go & Be")
#v(0.2cm)
#text(style: "italic")[Look at B opposite again. Note the way you can say either 'We camped in Spain this year' or 'We went camping in Spain this year'. Write the sentences below in an alternative form, either with or without go or be.]

#v(0.6cm)
#let s3 = (
  "1 They went canoeing in the Dordogne last year.",
  "2 Have you ever been windsurfing?",
  "3 I love going sailing.",
  "4 He spends too much time fishing.",
  "5 It's quite expensive to shop in Rome.",
  "6 I enjoy cycling at weekends."
)

#stack(
  spacing: 1.6cm,
  ..s3.map(s => block(width: 100%)[
    #text(weight: "bold", size: 12pt)[#s]
    #v(0.6cm)
    #line(length: 100%, stroke: 0.5pt + gray)
  ])
)

#v(0.8cm)

// --- TASK 4 ---
#task_header(4, "Error Correction")
#v(0.2cm)
#text(style: "italic")[There are six typical language mistakes in the paragraph below. Underline them and then write the corrections.]

#v(0.6cm)
#block(stroke: 1pt + slate-dark, inset: 15pt, radius: 4pt, fill: rgb("#fffaf0"))[
  #text(size: 13pt)[
    #set par(leading: 1.5em)
    The Smiths stayed at a camping last summer because all other kinds of holiday accommodations are too expensive for them. Every day Mrs Smith had a sunbath, Mr Smith made a sight-seeing and the children made a travel around the island. One day they made an excursion to a local castle.
  ]
]

#v(0.5cm)
#stack(
  spacing: 1.2cm,
  ..range(1, 7).map(i => {
    stack(dir: ltr, spacing: 12pt,
      text(weight: "bold", size: 13pt)[#(i):],
      align(bottom, box(width: 1fr, stroke: (bottom: 0.5pt + gray), inset: (bottom: 2pt))[])
    )
  })
)

#pagebreak()

// --- ANSWER KEY ---
#align(center)[#text(weight: "bold", fill: maroon, size: 20pt)[ANSWER KEY]]
#v(1.5cm)

#stack(spacing: 1.5cm,
  [
    #text(weight: "bold", size: 14pt, fill: maroon)[Task 3: Verb Forms]
    #v(0.4cm)
    1. They canoed in the Dordogne last year. \
    2. Have you ever windsurfed? \
    3. I love sailing. \
    4. He fishes too much. / He spends too much time going fishing. \
    5. It's quite expensive going shopping in Rome. \
    6. I enjoy going cycling at weekends.
  ],
  [
    #text(weight: "bold", size: 14pt, fill: maroon)[Task 4: Error Correction]
    #v(0.4cm)
    1. a campsite (not a camping) \
    2. holiday accommodation (not accommodations) \
    3. sunbathed (not had a sunbath) \
    4. went sightseeing (not made a sight-seeing) \
    5. went for a tour (not made a travel) \
    6. went on an excursion (not made an excursion)
  ]
)
