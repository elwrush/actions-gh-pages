#import "/lib/typst/lib.typ": *

#set page(paper: "a4", margin: (top: 1.5cm, bottom: 1.5cm, x: 1.5cm))
#set text(font: "Arial", size: 11pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

#intensive_header()

#hero_strap(
  "[TITLE]",
  "[SUBTITLE]",
  hero_image: image("[IMAGE_PATH]"),
  badges: ("[BADGE1]", "[BADGE2]", "[BADGE3]")
)

#v(0.5cm)

#block(
  width: 100%,
  fill: rgb("#fceceb"),
  stroke: 1.5pt + maroon,
  inset: 15pt,
  radius: 4pt,
  [
    #text(weight: "bold", fill: maroon, size: 14pt)[YOUR MISSION]
    #v(0.3em)
    [MISSION_DESCRIPTION_CAMBRIDGE_HOOK]

    #v(0.5em)
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 10pt,
      [🎯 *[VERB]* [OBJECTIVE 1]],
      [📝 *[VERB]* [OBJECTIVE 2]],
      [🗣️ *[VERB]* [OBJECTIVE 3]]
    )
  ]
)

#v(0.5cm)

#block(breakable: false, [
  #task_header(1, "[TASK TITLE]")
  #v(0.3cm)
  #text(size: 11pt)[[INSTRUCTIONS]]
  #v(0.3cm)
  [CONTENT]
])

// ... more tasks ...

#pagebreak()

#block(breakable: false, [
  #task_header([NUM], "Critical Thinking / Writing")
  #v(0.3cm)
  #writing_lines_dynamic()
])
