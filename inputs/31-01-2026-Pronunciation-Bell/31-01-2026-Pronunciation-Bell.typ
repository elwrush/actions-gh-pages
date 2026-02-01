#import "@local/bell-sheets:0.1.0": *

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let travel-blue = rgb("#1E3A8A")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#4D4D4D")

#set page(
  paper: "a4",
  margin: (top: 1.25cm, bottom: 1.25cm, x: 2cm),
)
#set text(font: "Arial", size: 13pt, fill: rgb("#333333"))
#set par(leading: 0.6em, justify: true)

#let phonemic_cell(symbol) = {
  rect(
    width: 100%,
    height: 1.5cm,
    stroke: 0.5pt + gray-line,
    align(center + horizon)[
      #text(size: 18pt, weight: "bold")[#symbol]
    ]
  )
}

#let gap_line(w) = box(width: w, stroke: (bottom: 0.5pt + gray-line))

// --- DOCUMENT ---

#intensive_header()

#hero_strap(
  "PRONUNCIATION",
  "Sound Symbols & Vowel Contrasts",
  hero_image: image("assets/hero_pron.jpg"),
  image_align: top
)

#v(0.5cm)
#badge("The Phonemic Chart")

#v(0.5cm)
#text(weight: "bold", fill: maroon)[Consonants]
#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr, 1fr),
  gutter: 4pt,
  phonemic_cell("/p/"), phonemic_cell("/t/"), phonemic_cell("/k/"), phonemic_cell("/f/"), phonemic_cell("/s/"), phonemic_cell("/θ/"),
  phonemic_cell("/b/"), phonemic_cell("/d/"), phonemic_cell("/ɡ/"), phonemic_cell("/v/"), phonemic_cell("/z/"), phonemic_cell("/ð/"),
  phonemic_cell("/ʃ/"), phonemic_cell("/tʃ/"), phonemic_cell("/ʒ/"), phonemic_cell("/dʒ/"), phonemic_cell("/h/"), phonemic_cell("/l/"),
  phonemic_cell("/r/"), phonemic_cell("/w/"), phonemic_cell("/m/"), phonemic_cell("/n/"), phonemic_cell("/ŋ/"), phonemic_cell("/j/")
)

#v(4cm) // White space above the rules

#block(fill: rgb("#FFFBEB"), inset: 10pt, radius: 4pt, stroke: 0.5pt + rgb("#F59E0B"))[
  #text(size: 11pt)[*Note:* Words like _happy_ and _hungry_ end in a short sound halfway between /iː/ and /ɪ/. Some dictionaries show this as /i/.]
]

#pagebreak() // Vowels & Diphthongs start on Page 2

#text(weight: "bold", fill: maroon)[Vowels & Diphthongs]
#grid(
  columns: (1fr, 1fr, 1fr, 1fr, 1fr),
  gutter: 4pt,
  phonemic_cell("/ɪ/"), phonemic_cell("/iː/"), phonemic_cell("/uː/"), phonemic_cell("/ʊ/"), phonemic_cell("/eɪ/"),
  phonemic_cell("/ɪə/"), phonemic_cell("/əʊ/"), phonemic_cell("/ə/"), phonemic_cell("/ɜː/"), phonemic_cell("/ɔː/"),
  phonemic_cell("/ɒ/"), phonemic_cell("/aɪ/"), phonemic_cell("/eə/"), phonemic_cell("/au/"), phonemic_cell("/e/"),
  phonemic_cell("/æ/"), phonemic_cell("/ɑː/"), phonemic_cell("/ʌ/"), phonemic_cell("/ɔɪ/"), phonemic_cell("/ʊə/")
)

#v(0.5cm)
#badge("Task 1: Transcription Challenge")
#v(0.3cm)
#align(center)[
  #image("assets/characters.png", width: 80%)
  #text(size: 11pt, style: "italic")[Tom, Joe, Paul, Liz, Sue, Jane]
]

#v(0.3cm)
#grid(
  columns: (1fr, 1fr),
  gutter: 1.2cm,
  [
    1. /tɒm laɪks 'raɪtɪŋ 'pəʊətri/ \
    #v(0.3cm)
    #gap_line(100%) \
    #text(size: 11pt, fill: travel-blue.lighten(40%))[_Tom likes writing poetry._]
    
    #v(1cm)
    2. /dʒeɪnz ɡɒt ə 'frendli braʊn pet kæt/ \
    #v(0.3cm)
    #gap_line(100%)
    
    #v(1cm)
    3. /suː wəz fɑːst ə'sliːp wen ðə 'bɜːɡləz keɪm/ \
    #v(0.3cm)
    #gap_line(100%)
    
    #v(1cm)
    4. /dʒəʊ bɔːt ə 'bɒtəl əv hʌŋ'ɡeəriən waɪn lɑːst naɪt/ \
    #v(0.3cm)
    #gap_line(100%)
  ],
  [
    5. /lɪz wɒnts tə biː rɪtʃ ənd 'feɪməs wʌn deɪ/ \
    #v(0.3cm)
    #gap_line(100%)
    
    #v(1cm)
    6. /pɔːlz ə 'welθi jʌŋ 'tʊərɪst/ \
    #v(0.3cm)
    #gap_line(100%)
    
    #v(1cm)
    7. /tɒm ənd lɪz ə ɡʊd ət 'spænɪʃ/ \
    #v(0.3cm)
    #gap_line(100%)
    
    #v(1cm)
    8. /dʒəʊ wɜːks ɪn ə 'nɔɪzi 'ɡæraːʒ/ \
    #v(0.3cm)
    #gap_line(100%)
  ]
)

#pagebreak() // Ensure Task 2 and 3 are on Page 3 as Task 1 is high-density

#v(1cm)
#badge("Task 2: The sounds /ɒ/, /ɔː/, and /əʊ/")

#v(0.5cm)
#grid(
  columns: (1fr, 1fr, 1fr),
  gutter: 10pt,
  image("assets/fox-cock.png", width: 100%),
  image("assets/forks-cork.png", width: 100%),
  image("assets/folks-coke.png", width: 100%)
)

#v(0.5cm)
#text(weight: "bold", fill: travel-blue)[Listen and Tick] \
#text(size: 12pt)[_You will hear ten words. For each word, put a tick (✓) in the correct box._]

#v(0.5cm)
#table(
  columns: (40pt, 1fr, 1fr, 1fr, 2fr),
  stroke: 0.5pt + gray-line,
  align: center + horizon,
  inset: 10pt,
  [], [/ɒ/], [/ɔː/], [/əʊ/], [Word],
  [1], [✓], [], [], [clock],
  ..range(2, 11).map(i => ([#i], [], [], [], [])).flatten()
)

#pagebreak()
#badge("Task 3: Categorization")
#v(0.3cm)
#text(size: 12pt)[_Put the words from the box into the correct columns below._]

#v(0.5cm)
#align(center)[
  #block(stroke: 1pt + maroon, inset: 15pt, radius: 4pt, width: 90%)[
    #grid(
      columns: (1fr, 1fr, 1fr, 1fr),
      gutter: 15pt,
      [w#underline[a]lk], [wr#underline[o]ng], [w#underline[o]n't], [g#underline[o]ne],
      [ag#underline[o]], [n#underline[o]vel], [w#underline[a]ter], [#underline[a]ll],
      [qu#underline[a]rrel], [w#underline[a]nt], [#underline[o]nly], [d#underline[oo]r],
      [m#underline[o]ment], [th#underline[ou]ght], [ph#underline[o]ne], [alth#underline[ou]gh]
    )
  ]
]

#v(0.5cm)
#table(
  columns: (1fr, 1fr, 1fr),
  stroke: 0.5pt + gray-line,
  align: center + horizon,
  inset: 12pt,
  table.header(
    [*[ /ɒ/ ]*], [*[ /ɔː/ ]*], [*[ /əʊ/ ]*],
  ),
  [], [walk], [],
  ..range(7).map(_ => ([], [], [])).flatten()
)

#v(2cm)
#line(length: 100%, stroke: (paint: gray-line.lighten(50%), dash: "dashed", thickness: 0.5pt))
#align(right)[
  #text(size: 9pt, fill: gray-line)[© Bell Education Services | B1 Pronunciation Series]
]

#pagebreak()

#badge("Answer Key")
#v(0.5cm)

#text(weight: "bold", fill: maroon)[Task 1: Transcription Challenge]
#v(0.2cm)
#text(size: 11pt)[
  1. Tom likes writing poetry.
  2. Jane's got a friendly brown pet cat.
  3. Sue was fast asleep when the burglars came.
  4. Joe bought a bottle of Hungarian wine last night.
  5. Liz wants to be rich and famous one day.
  6. Paul's a wealthy young tourist.
  7. Tom and Liz are good at Spanish.
  8. Joe works in a noisy garage.
]

#v(1cm)
#text(weight: "bold", fill: maroon)[Task 2: Listen and Tick]
#v(0.2cm)
#table(
  columns: (40pt, 1fr, 1fr, 1fr, 2fr),
  stroke: 0.5pt + gray-line,
  align: center + horizon,
  inset: 8pt,
  [], [/ɒ/], [/ɔː/], [/əʊ/], [Word],
  [1], [✓], [], [], [clock],
  [2], [], [✓], [], [sport],
  [3], [], [], [✓], [boat],
  [4], [], [✓], [], [saw],
  [5], [✓], [], [], [got],
  [6], [], [], [✓], [joke],
  [7], [✓], [], [], [box],
  [8], [], [], [✓], [shown],
  [9], [], [✓], [], [born],
  [10], [], [], [✓], [coat],
)

#v(1cm)
#text(weight: "bold", fill: maroon)[Task 3: Categorization]
#v(0.2cm)
#list(
  [#strong[/ɒ/:] quarrel, wrong, novel, want, gone],
  [#strong[/ɔː/:] walk, thought, water, all, door],
  [#strong[/əʊ/:] ago, moment, won’t, only, phone, although]
)
