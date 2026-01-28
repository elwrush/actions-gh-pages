#import "@local/bell-sheets:0.1.0": *

#set page(paper: "a4", margin: 2cm)
#set text(font: "Arial", size: 11pt)

#bell_header()

#hero_strap(
  "Global Test",
  "Testing the new bell-sheets package",
  hero_image: image("inputs/Superconsumer-Generation/mall_hero.jpg"),
  badges: ("B1", "READING")
)

#task_header(1, "Verification")
#lorem(50)

#pagebreak()
#identity_block()

#writing_lines_dynamic()
