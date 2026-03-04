#import "../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *

#set page(
  paper: "a4",
  margin: (top: 1.5cm, bottom: 2cm, x: 2cm),
)
#set text(font: "Arial", size: 10pt, fill: rgb("#333333"))
#set par(leading: 0.65em, justify: false)

// BRAND COLORS (Keeping local for now as they are used in main body logic if any)
#let maroon = rgb("#A62D26")
#let light-maroon = rgb("#cb5c55")
#let pale-pink = rgb("#fceceb")

// ==========================================
// DOCUMENT CONTENT
// ==========================================

#lesson_header("bell")

#metadata_table((
  teacher: "Ed Rush",
  date: "18-01-2026",
  cefr: "B1 (Mixed/Differentiated)",
  duration: "46 Minutes",
  shape: "E (Receptive Skills - Reading)",
  assessment: "N/A",
  focus: "Reading (Detail & Specific Information)",
  materials: "18-Jan-2026-QAD-handout.pdf",
))

#v(0.5cm)

#main_aim_box[
  By the end of the lesson, learners will have practiced and developed the sub-skills of reading for detail and specific information in the context of the biological "Fight or Flight" response.
]

#v(0.5cm)

#differentiation_box[
  This lesson employs a "Tiered Text" strategy, allowing students to self-select between B1, B1+, and B2 versions of the core material. This approach is grounded in *Krashen's Input Hypothesis (1982)*, which posits that language acquisition occurs when learners receive "comprehensible input" (i+1). By providing choice, we lower the *Affective Filter* and promote *Learner Autonomy* (Tomlinson, 2014), ensuring that the cognitive load is sufficient to challenge without causing "frustration-level" reading. This maximizes engagement and ensures that the focus remains on the process of reading for detail rather than a struggle with decoding unfamiliar lexis.
]

#v(0.5cm)

#stage_table((
  // STAGE ONE
  table.cell(
    colspan: 4,
    fill: maroon,
    text(fill: white, weight: "bold", hyphenate: true)[STAGE ONE: Lead-in],
  ),
  [8 Min],
  [To activate schema and introduce key vocabulary],
  [
    - *Part 1 (Engagement):* Display the "Fight or Flight" title graphic. Ask: "What happens to your body when you are scared?" Elicit symptoms (heart beating fast, breathing quickly, feeling cold). (2 Min)
    - *Part 2 (Defining terms):* Introduce the biological term "Fight or Flight" as a natural _instinct_. Elicit other animal instincts (migration, hibernation). (2 Min)
    - *Part 3 (Personalization):* **Task 1 (Before you read):** Ss work in pairs to discuss the questions about specific fears they and their family have. T monitors and collects good language. (4 Min)
  ],
  [T-Ss / Ss-Ss],
))

#pagebreak()

#stage_table((
  // STAGE TWO
  table.cell(
    colspan: 4,
    fill: maroon,
    text(fill: white, weight: "bold", hyphenate: true)[STAGE TWO: Self-Selection],
  ),
  [5 Min],
  [To allow learners to select appropriate text level],
  [
    - Display Paragraph \[1\] from the 3 versions (B1, B1+, B2) successively on slides.
    - Ask: "Which one feels most comfortable? Which one is a good challenge for you today?"
    - Distribute the appropriate page from the handout (P.1/7/8) based on student choice. T reminds Ss that they can change levels if it feels too hard/easy.
  ],
  [T-Ss],
  // STAGE THREE
  table.cell(
    colspan: 4,
    fill: maroon,
    text(fill: white, weight: "bold", hyphenate: true)[STAGE THREE: Pre-teach Vocabulary],
  ),
  [8 Min],
  [To pre-teach key biological lexis],
  [
    *Target Lexis (B1/B2 Consistency Check):*

    1. *instinct* /'ɪnstɪŋkt/: We are born with the *instinct* to breathe; nobody needs to teach us how to do it.\
    #h(1em)สัญชาตญาณ: เราเกิดมาพร้อมกับ*สัญชาตญาณ*ในการหายใจ ไม่มีใครต้องสอนเราว่าต้องทำอย่างไร

    2. *hormones* /'hɔːməʊnz/: Our brain releases *hormones* which travel through the blood to tell our body how to feel.\
    #h(1em)ฮอร์โมน: สมองของเราหลั่ง*ฮอร์โมน*ซึ่งเดินทางผ่านเลือดเพื่อบอกร่างกายว่าควรจะรู้สึกอย่างไร

    3. *adrenaline* /ə'drenəlɪn/: When I was scared, my body released *adrenaline* and I suddenly had the energy to run very fast.\
    #h(1em)อะดรีนาลีน: เมื่อฉันกลัว ร่างกายของฉันก็หลั่ง*อะดรีนาลีน*ออกมา และทันใดนั้นฉันก็มีพลังงานที่จะวิ่งได้เร็วมาก

    4. *glucose* /'ɡluːkəʊส/: After eating sugar, your body produces *glucose* to give your muscles the power they need.\
    #h(1em)กลูโคส: หลังจากรับประทานน้ำตาล ร่างกายของคุณจะผลิต*กลูโคส*เพื่อให้กล้ามเนื้อมีพลังตามที่ต้องการ

    5. *organs* /'ɔːɡənz/: Doctors check the health of your *organs*, like your heart and lungs, to make sure your body is working correctly.\
    #h(1em)อวัยวะ: แพทย์จะตรวจสอบสุขภาพของ*อวัยวะ*ของคุณ เช่น หัวใจและปอด เพื่อให้แน่ใจว่าร่างกายของคุณทำงานอย่างถูกต้อง

    #v(0.3em)
    _CCQs: Is an instinct learned or are we born with it? (Born). Does adrenaline make you fast or slow? (Fast)._
  ],
  [T-Ss],
  // STAGE FOUR
  table.cell(
    colspan: 4,
    fill: maroon,
    text(fill: white, weight: "bold", hyphenate: true)[STAGE FOUR: Reading for Detail],
  ),
  [18 Min],
  [To practice reading for detail and specific information],
  [
    - **Task 2 (Global Reading):** Ss skim their chosen text to find which paragraphs contain specific facts (scanning). Ss compare answers in pairs before class feedback. (6 Min)
    - **Task 3 (Close Reading & Vocabulary):** Ss read the text again to match words with definitions (e.g. glucose, organs). T monitors to ensure Ss are using context to find answers. (8 Min)
    - **Feedback:** Review answers for Task 2 and 3 using PowerPoint. Elicit the reason for any incorrect answers to assist with comprehension. (4 Min)
  ],
  [Ss-Ss],
  // STAGE FIVE
  table.cell(
    colspan: 4,
    fill: maroon,
    text(fill: white, weight: "bold", hyphenate: true)[STAGE FIVE: Critical Thinking],
  ),
  [7 Min],
  [To personalize content and develop critical thinking through writing],
  [
    - **Task 4 (Critical Thinking):** Students choose one question to write a **70-word response**:
      1. _"Avoid risk is a good or bad thing? Why?"_
      2. _"Does fear stop you from achieving what you want?"_
    - Ss must use context from Paragraph 6 (Fear of failure) to support their arguments.
    - Monitor for accurate use of target lexis (instinct, adrenaline).
    - Class feedback: Select 2-3 examples to read out and provide language feedback on the board.
  ],
  [Indiv / T-Ss],
))

#v(1cm)

#block(
  width: 100%,
  stroke: (top: 2pt + maroon),
  inset: (top: 10pt),
  [
    #text(weight: "bold", fill: maroon, size: 11pt)[Answer Key:]

    #v(0.3em)

    *Task 2:* 1. Para 4 | 2. Para 6 | 3. Para 2 | 4. Para 7 | 5. Para 3 | 6. Para 8 | 7. Para 5

    *Task 3:* 1. self-defense | 2. fight or flight instinct | 3. physical abilities | 4. adrenaline | 5. glucose | 6. organs
  ],
)
