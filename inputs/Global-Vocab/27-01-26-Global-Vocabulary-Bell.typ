
#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 1.5cm, x: 1.5cm),
)
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.6em, justify: true)

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let travel-blue = rgb("#1E3A8A")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#4D4D4D")

// --- COMPONENTS ---

#let bell_header() = {
  stack(
    dir: ttb,
    image("../../images/bell-header.jpg", width: 100%),
    v(0.2cm),
    block(
      width: 100%,
      height: 4cm,
      radius: 4pt,
      clip: true,
      stroke: 1pt + maroon,
      [
        #image("images/world_map.jpg", width: 100%, height: 100%, fit: "cover")
        #place(center + horizon)[
          #block(fill: rgb(255, 255, 255, 80%), inset: 15pt, radius: 4pt)[
            #text(size: 24pt, weight: "bold", fill: maroon)[GLOBAL EXPLORER] \
            #text(size: 14pt, weight: "bold", fill: travel-blue)[COUNTRIES, PEOPLE & LANGUAGES]
          ]
        ]
      ]
    )
  )
}

#let section_title(icon, title) = {
  v(0.5cm)
  block(width: 100%, stroke: (bottom: 1.5pt + maroon), inset: (bottom: 5pt))[
    #text(size: 14pt, weight: "bold", fill: maroon)[#icon #h(5pt) #upper(title)]
  ]
  v(0.2cm)
}

#let task_stamp(num, title) = {
  v(0.5cm)
  block(
    width: 100%,
    fill: travel-blue.lighten(90%),
    stroke: 1pt + travel-blue,
    radius: 4pt,
    inset: 8pt,
    [
      #grid(
        columns: (auto, 1fr),
        gutter: 10pt,
        align(center + horizon)[
          #circle(radius: 12pt, stroke: 2pt + travel-blue, fill: white)[
            #set align(center + horizon)
            #text(size: 11pt, weight: "bold", fill: travel-blue)[#num]
          ]
        ],
        align(horizon)[
          #text(size: 11pt, weight: "bold", fill: travel-blue)[#upper(title)]
        ]
      )
    ]
  )
  v(0.3cm)
}

#let gap_line(w) = box(width: w, stroke: (bottom: 0.5pt + gray-line))

// --- DOCUMENT ---

#bell_header()

#v(0.2cm)
#align(center)[
  #text(size: 11pt, style: "italic", fill: slate-dark)[Vocabulary & Grammar for B1 Learners | Lesson Duration: 46 Minutes]
]

#v(0.5cm)

// REFERENCE SECTION
#grid(
  columns: (1.2fr, 1fr),
  gutter: 1cm,
  [
    #section_title("🌍", "Parts of the World")
    #text(weight: "bold")[The Continents:] 
    Europe, Africa, Asia, North America, South America, Australia (incl. New Zealand), Antarctica.
    
    #v(0.5em)
    #text(weight: "bold")[Regional Terms:]
    #list(
      [#text(weight: "bold")[The Middle East:] e.g. UAE, Saudi Arabia],
      [#text(weight: "bold")[The Far East:] e.g. Thailand, Japan],
      [#text(weight: "bold")[The Caribbean:] e.g. Jamaica, Barbados],
      [#text(weight: "bold")[Scandinavia:] Sweden, Norway, Denmark, Finland],
    )
  ],
  [
    #section_title("👥", "The People")
    #text(style: "italic")[When talking about people from a specific country:]
    
    #v(0.5em)
    #strong[1. Suffix -i or -(i)an] (Add 's' for plural):
    - Brazilians, Russians, Thais, Israelis.
    
    #v(0.5em)
    #strong[2. Adjectives with 'The'] (No 's'):
    - The British, The French, The Swiss, The Japanese.
    
    #v(0.5em)
    #block(fill: rgb("#FFFBEB"), inset: 8pt, radius: 4pt, stroke: 0.5pt + rgb("#F59E0B"))[
      #text(size: 9pt)[*Note:* You can also use 'people' (e.g. _British people_).]
    ]
  ]
)

#v(0.5cm)
#line(length: 100%, stroke: (paint: gray-line.lighten(50%), dash: "dashed", thickness: 0.5pt))

// EXERCISES
#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  [
    #task_stamp("1", "Quick Quiz")
    #set text(size: 9.5pt)
    1. Nationality of people from Poland? #gap_line(2.5cm) \
    2. Nationality of people from Thailand? #gap_line(2.5cm) \
    3. Language spoken in Spain? #gap_line(2.5cm) \
    4. Where do people speak Hebrew? #gap_line(2.5cm) \
    5. Where do people speak Mandarin? #gap_line(2.5cm) \
    6. Language spoken in Brazil? #gap_line(2.5cm) \
    7. Language spoken in Egypt? #gap_line(2.5cm) \
    8. Nationality of people from Germany? #gap_line(2.5cm) \
    9. Three countries where English is the 1st language: \
    #gap_line(100%) \
    10. Three languages spoken in Switzerland: \
    #gap_line(100%)
    
    #task_stamp("2", "Regional Mapping")
    _Which part of the world are these in? (e.g. Europe, Far East)_ \
    1. Germany: #gap_line(2.5cm) \
    2. Japan: #gap_line(2.5cm) \
    3. Saudi Arabia: #gap_line(2.5cm) \
    4. Italy: #gap_line(2.5cm) \
    5. Jamaica: #gap_line(2.5cm) \
    6. Argentina: #gap_line(2.5cm)
  ],
  [
    #task_stamp("3", "Word Stress")
    _Underline the main stress in these words:_
    #v(0.5em)
    #block(stroke: 0.5pt + gray-line, inset: 8pt, width: 100%)[
      #grid(
        columns: (1fr, 1fr),
        gutter: 10pt,
        [Brazilian], [Portuguese],
        [Chinese], [Australia],
        [Japan], [Arabic],
        [Egyptian], [Saudi Arabia],
        [Scandinavia], []
      )
    ]
    
    #task_stamp("4", "Global Capitals")
    1. Bangkok #gap_line(1cm) #h(5pt) 4. Moscow #gap_line(1cm) \
    2. Ankara #gap_line(1cm) #h(5pt) 5. Buenos Aires #gap_line(1cm) \
    3. Seoul #gap_line(1cm) #h(5pt) 6. Athens #gap_line(1cm)
    
    #task_stamp("5", "Collective Nationals")
    _Complete with the name of the people:_ \
    1. I've worked a lot with #gap_line(2cm) (FRANCE) \
    2. I know lots of #gap_line(2cm) (GERMANY) \
    3. Business with #gap_line(2.5cm) (JAPAN) \
    4. I used to know #gap_line(2cm) (ISRAEL) \
    5. I find #gap_line(2.5cm) friendly (BRAZIL) \
    6. People say #gap_line(2.5cm) are reserved (BRITAIN) \
    7. #gap_line(2.5cm) are very organised (SWITZERLAND) \
    8. I met a lot of #gap_line(2.5cm) in Moscow (RUSSIA)
  ]
)

#block(width: 100%, stroke: 1.5pt + maroon, fill: white, inset: 15pt, radius: 4pt)[
  #text(fill: maroon, weight: "bold", size: 12pt)[🌍 OVER TO YOU]
  #v(0.8em)
  #text(fill: slate-dark, size: 10pt)[
    #grid(
      columns: (1fr, 1fr),
      row-gutter: 30pt, // Expanded for handwriting
      gutter: 20pt,
      [1. What's your nationality? \ #gap_line(100%)],
      [2. Capital city & population? \ #gap_line(100%)],
      [3. What's your first language? \ #gap_line(100%)],
      [4. Other languages you speak? \ #gap_line(100%)],
      [5. Countries you've visited? \ #gap_line(100%)],
      [6. Countries you'd like to visit? \ #gap_line(100%)]
    )
  ]
]

#v(1cm)
#section_title("💡", "Critical Thinking")
#text(style: "italic", size: 11pt)[Discuss with a partner or write your thoughts below:]
#v(0.5cm)
*How would the world be different if everyone spoke the same language? Would it be better or worse? Why?*

#v(1cm)
#range(3).map(_ => [#gap_line(100%) #v(1cm)]).join()

#pagebreak()

// ANSWER KEY
#section_title("🔑", "Answer Key")

#grid(
  columns: (1fr, 1fr),
  gutter: 1cm,
  [
    #task_stamp("1", "Quick Quiz")
    1. Polish 🇵🇱; 2. Thai 🇹🇭; 3. Spanish 🇪🇸; 4. Israel 🇮🇱; 5. China 🇨🇳 / Taiwan 🇹🇼; 6. Portuguese 🇵🇹; 7. Arabic 🇪🇬🇸🇦; 8. German 🇩🇪; 9. UK 🇬🇧, USA 🇺🇸, Canada 🇨🇦, Australia 🇦🇺, NZ 🇳🇿; 10. German, French, Italian, Romansh 🇨🇭.
    
    #task_stamp("2", "Regional Mapping")
    1. Germany 🇩🇪: Europe; 2. Japan 🇯🇵: Far East; 3. Saudi Arabia 🇸🇦: Middle East; 4. Italy 🇮🇹: Europe; 5. Jamaica 🇯🇲: Caribbean; 6. Argentina 🇦🇷: South America.
    
    #task_stamp("3", "Word Stress")
    Bra*zi*lian, Chi*nese*, Ja*pan*, Portu*guese*, E*gyp*tian, Aus*tra*lia, *Ar*abic, *Sau*di A*ra*bia, Scandi*na*via.
  ],
  [
    #task_stamp("4", "Global Capitals")
    1. Thailand 🇹🇭; 2. Turkey 🇹🇷; 3. South Korea 🇰🇷; 4. Russia 🇷🇺; 5. Argentina 🇦🇷; 6. Greece 🇬🇷.
    
    #task_stamp("5", "Collective Nationals")
    1. the French 🇫🇷; 2. Germans 🇩🇪; 3. the Japanese 🇯🇵; 4. Israelis 🇮🇱; 5. Brazilians 🇧🇷; 6. the British 🇬🇧; 7. The Swiss 🇨🇭; 8. Russians 🇷🇺.
  ]
)
