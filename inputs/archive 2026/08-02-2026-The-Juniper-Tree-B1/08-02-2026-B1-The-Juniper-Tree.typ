#import "@local/bell-sheets:0.1.0": *

#set page(
  paper: "a4",
  margin: (x: 1.8cm, y: 1.5cm),
)

#set text(
  font: "Arial",
  size: 11.5pt,
  fill: slate-dark,
  hyphenate: false,
)

#let gap = h(1fr)

// 1. BRANDING
#bell_header()

// 2. HERO STRAP
#hero_strap(
  "The Juniper Tree",
  "A Dark Tale of Retribution & Rebirth",
  hero_image: image("images/hero.png"),
  badges: ("B1+", "46 MINS")
)

#v(0.6cm)

// 3. MISSION
#block(
  fill: pale-pink,
  inset: 18pt,
  radius: 4pt,
  stroke: 1pt + maroon,
  [
    #text(weight: "bold", fill: maroon, size: 14pt)[YOUR MISSION]
    #v(0.2cm)
    In your *B1 PET for Schools* exam, you must be able to follow complex narratives and understand the motivations of different characters. This lesson explores one of the darkest Brothers Grimm fairy tales to help you master storytelling, narrative tenses, and symbolic meaning.

    #v(0.4cm)
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 15pt,
      [#text(weight: "bold")[READ] for detail and narrative structure.],
      [#text(weight: "bold")[ANALYZE] the themes of justice and greed.],
      [#text(weight: "bold")[SPEAK] about the ethics and impact of folk tales.]
    )
  ]
)

#v(0.8cm)

// 4. THE STORY
#task_header(1, "The Reading: The Juniper Tree")

#columns(1, gutter: 20pt)[
  #text(style: "italic", size: 10pt, fill: slate-dark.lighten(20%))[Source: Abridged from the Brothers Grimm (1812)]
  #v(0.2cm)
  
  #text(fill: maroon, weight: "bold")[[1]] Long ago, a rich man and his beautiful, pious wife loved each other dearly but had no children, despite wishing for one constantly. In their garden stood a large juniper tree. One winter day, while peeling an apple under the tree, the woman cut her finger, and drops of blood fell onto the snow. "Ah," she sighed, looking at the red on white. "If only I had a child as red as blood and as white as snow!" Immediately, she felt happy, as if her wish would come true.

  #text(fill: maroon, weight: "bold")[[2]] Months passed. The snow melted, the world turned green, and the berries ripened. By the seventh month, the woman ate the juniper berries, becoming sad and ill. By the eighth, she knew she was dying. "If I die," she told her husband, "bury me under the juniper tree." soon after, she gave birth to a baby boy as white as snow and red as blood. She was so happy that she died holding him. Her husband buried her under the tree and mourned for a long time before eventually remarrying.

  #text(fill: maroon, weight: "bold")[[3]] With his second wife, he had a daughter named Marlinchen. However, the stepmother was jealous. She looked at her own daughter and then at the beautiful little boy, feeling angry. She wanted the family’s fortune solely for Marlinchen. The Devil entered her mind, and she began to hate the boy, pushing him from corner to corner and giving him only scraps.

  #text(fill: maroon, weight: "bold")[[4]] One day, the stepmother went to her room where she kept a heavy chest of apples. "Mother," said Marlinchen, "can I have an apple?"
  "Yes, my child," the woman said, giving her a fine one.
  Then the little boy entered. "Mother, can I have an apple too?"
  A sudden, terrible anger seized the woman. "Come here," she said sweetly. "The apples are in the chest. Lift the lid and take one."

  #text(fill: maroon, weight: "bold")[[5]] As the boy leaned over the deep chest, the stepmother slammed the heavy iron lid down. It fell with such force that his head flew off among the red apples. Fear seized her. "I must hide this!" she thought. She took a white handkerchief, set the boy’s head back on his neck, and tied the cloth around it to hide the cut. She sat him on a chair by the door with an apple in his hand.

  #text(fill: maroon, weight: "bold")[[6]] Later, Marlinchen came into the kitchen. "Brother," she said, "give me that apple." He did not answer. She pushed him, and his head fell off. Marlinchen screamed, running to her mother. "I have killed my brother!"
  "Be quiet!" said the wicked stepmother. "We cannot change it. We will make him into a stew."

  #text(fill: maroon, weight: "bold")[[7]] She chopped the boy into pieces and put him in a pot. Marlinchen cried until her tears fell into the stew, salting it perfectly. When the father came home, he asked, "Where is my son?"
  "He has gone to visit his uncle," the stepmother lied.
  The father ate the stew hungrily. "This is delicious," he said. "Give me more. I feel as if it all belongs to me." He ate until only bones remained. Marlinchen gathered the bones in her best silk handkerchief and laid them in the green grass under the juniper tree.

  #text(fill: maroon, weight: "bold")[[8]] Suddenly, the tree moved. Its branches shook, and a mist like fire rose from the center. Inside the fire, a beautiful bird sang. The bird flew into the sky, and the bones vanished. The bird flew to a goldsmith’s house and sang:
  "My mother, she killed me,
  My father, he ate me,
  My sister, Marlinchen,
  Gathered my bones,
  Tied them in silk,
  Laid them under the juniper tree.
  Kywitt, kywitt, what a beautiful bird am I!"

  #text(fill: maroon, weight: "bold")[[9]] Enchanted, the goldsmith gave the bird a heavy gold chain. The bird then flew to a shoemaker, sang the song, and received a pair of red shoes. Finally, it flew to a mill where twenty men were working. They stopped to listen, and the miller gave the bird a huge, heavy millstone.

  #text(fill: maroon, weight: "bold")[[10]] Carrying the chain, shoes, and stone, the bird returned home. The father sat inside, saying, "I feel so happy. The sun is shining, and I hear a beautiful old song."
  "I feel scared," said the stepmother. "I feel like a storm is coming."

  #text(fill: maroon, weight: "bold")[[11]] The bird landed on the juniper tree and sang. The father ran outside, and the bird dropped the gold chain around his neck. Marlinchen ran out next, and the bird threw down the red shoes. She put them on, feeling light and happy.
  "I must see this bird too," said the stepmother, trembling. As she stepped out, the bird dropped the heavy millstone, crushing her completely.

  #text(fill: maroon, weight: "bold")[[12]] Smoke and flames rose. When they cleared, the stepmother was gone. But standing there was the little boy, alive again. He took his father and Marlinchen by the hand. They were all very happy, and went inside to eat.
]

#v(1cm)

// 5. ASSESSMENT
#task_header(2, "Comprehension & Analysis")

#text(weight: "bold")[A. Multiple Choice]
#v(0.2cm)

1. Where did the first wife ask to be buried?
   #enum(numbering: "A.", 
     [Under the apple tree],
     [In the churchyard],
     [Under the juniper tree],
     [Next to the garden gate]
   )

2. In the phrase "a beautiful and *pious* wife", what does "pious" mean?
   #enum(numbering: "A.",
     [Deeply religious and moral],
     [Very wealthy],
     [Extremely beautiful],
     [Sad and lonely]
   )

3. Why did the father eat the stew so hungrily?
   #enum(numbering: "A.",
     [He had not eaten for days],
     [He felt a supernatural connection to it],
     [He wanted to please the stepmother],
     [It was his favorite meal]
   )

4. What is the primary theme of the story's conclusion?
   #enum(numbering: "A.",
     [The danger of apples],
     [Family dinners],
     [The value of gold],
     [Justice and retribution for evil deeds]
   )

#v(0.6cm)

#text(weight: "bold")[B. Chronological Order]
#v(0.2cm)
*Number the events of the bird's journey in the correct order (1-4).*

- The bird receives red shoes from the shoemaker. #gap #text("(___)")
- The bird rises from the mist and fire of the juniper tree. #gap #text("(___)")
- The bird receives a millstone from the miller. #gap #text("(___)")
- The bird receives a gold chain from the goldsmith. #gap #text("(___)")

#v(0.6cm)

#text(weight: "bold")[C. Character Connections]
#v(0.2cm)
*Match the gift to the receiver.*

#grid(
  columns: (1fr, 1fr),
  gutter: 10pt,
  [1. Gold Chain], [A. The Little Boy],
  [2. Red Shoes], [B. The Stepmother],
  [3. Millstone], [C. The Father],
  [4. Apple], [D. Marlinchen]
)

#v(0.6cm)

#text(weight: "bold")[D. Recall]
#v(0.2cm)
*Complete the missing words from the bird's song.*
"My mother, she #box(width: 2cm, rule_line) me, My father, he #box(width: 2cm, rule_line) me."

#v(1cm)

// 6. SPEAKING
#task_header(3, "Discussion: The Power of Folk Tales")

#block(
  fill: rgb("#f1f5f9"),
  inset: 18pt,
  radius: 4pt,
  [
    Discuss the following question with your partner using the *ORE* pattern:
    
    *"In your opinion, is 'The Juniper Tree' too dark or violent for children today?"*
    
    #v(0.4cm)
    #grid(
      columns: (1fr, 1fr, 1fr),
      gutter: 15pt,
      [#text(weight: "bold", fill: maroon)[O] PINION \ I believe that...],
      [#text(weight: "bold", fill: maroon)[R] EASON \ The reason for this is...],
      [#text(weight: "bold", fill: maroon)[E] XAMPLE \ For example, in the story...]
    )
  ]
)

#v(1fr)

// 7. ANSWER KEY
#pagebreak()
#task_header(4, "Answer Key")

#text(weight: "bold")[A. Multiple Choice]
#grid(
  columns: (1fr, 1fr, 1fr, 1fr),
  gutter: 10pt,
  [1. C], [2. A], [3. B], [4. D]
)

#v(0.5cm)
#text(weight: "bold")[B. Chronological Order]
1. The bird rises from the mist and fire of the juniper tree.
2. The bird receives a gold chain from the goldsmith.
3. The bird receives red shoes from the shoemaker.
4. The bird receives a millstone from the miller.

#v(0.5cm)
#text(weight: "bold")[C. Character Connections]
1. Gold Chain -> C. The Father
2. Red Shoes -> D. Marlinchen
3. Millstone -> B. The Stepmother
4. Apple -> A. The Little Boy

#v(0.5cm)
#text(weight: "bold")[D. Recall]
"My mother, she *killed* me, My father, he *ate* me."
