// ============================================================
// BELL-SHEETS GLOBAL LIBRARY (V0.1.0)
// Standard components for educational materials
// ============================================================

// BRAND COLORS
#let maroon = rgb("#8B1538")
#let slate-dark = rgb("#334155")
#let gray-line = rgb("#333333") // Mandate dark gray for photocopy survival
#let pale-pink = rgb("#fceceb")

// ==========================================
// 1. BRANDING & HEADERS
// ==========================================

#let bell_header() = {
  v(0.2cm)
  align(center)[
    #image("/images/bell-header.jpg", width: 100%)
  ]
  v(0.2cm)
}

#let intensive_header() = {
  v(0.2cm)
  align(center)[
    #image("/images/intensive-header.jpg", width: 100%)
  ]
  v(0.2cm)
}

// ==========================================
// 2. BADGES & PILLS
// ==========================================

#let badge(content, fill_color: maroon) = {
  box(
    fill: fill_color,
    inset: (x: 12pt, y: 7pt),
    radius: 3pt,
    baseline: 25%,
    stroke: 0.5pt + fill_color.darken(25%),
    [
      #set text(font: "Arial", fill: white, weight: "bold", size: 14pt, tracking: 0.02em)
      #upper(content)
    ]
  )
}

// ==========================================
// 3. HERO STRAP
// ==========================================

#let hero_strap(title, subtitle, hero_image: none, badges: (), image_align: center) = {
  if badges.len() > 0 {
    stack(dir: ltr, spacing: 5pt, ..badges.map(b => badge(b)))
    v(4pt)
  }

  block(
    width: 100%,
    height: 5.5cm,
    radius: 4pt,
    clip: true,
    [
      #if hero_image != none {
        place(image_align, {
          set image(width: 100%, fit: "cover")
          hero_image
        })
      }
      
      #place(
        bottom + left,
        block(
          width: 100%,
          fill: maroon.lighten(10%).transparentize(15%),
          inset: (x: 18pt, y: 15pt),
          [
            #text(fill: white, weight: "bold", size: 24pt)[#upper(title)]
            #v(-10pt)
            #text(fill: white, size: 13pt, style: "italic")[#subtitle]
          ]
        )
      )
    ]
  )
}

// ==========================================
// 4. TASK HEADERS
// ==========================================

#let task_header(num, title) = {
  block(breakable: false, width: 100%, inset: (top: 15pt, bottom: 8pt), [
    #stack(dir: ltr, spacing: 12pt,
      badge("TASK " + str(num)),
      align(horizon, text(weight: "bold", fill: maroon, size: 16pt)[#upper(title)])
    )
  ])
}

// ==========================================
// 5. STUDENT IDENTITY
// ==========================================

#let bubble(content, size: 12pt) = {
  box(
    width: size,
    height: size,
    stroke: 0.5pt + gray-line,
    radius: 50%,
    fill: white,
    align(center + horizon, text(size: size * 0.55, weight: "bold", fill: gray-line)[#content])
  )
}

#let identity_block() = {
  let bubble_col = 19pt
  let label_col = 22pt
  
  block(
    width: 100%, 
    fill: rgb("#F1F5F9"),
    inset: 18pt,
    radius: 4pt,
    [
      #align(center)[
        #text(size: 11pt, fill: slate-dark, weight: "bold")[ระบายวงกลมด้วยปากกาหรือดินสอตามชั้นเรียนและรหัสนักเรียน (ห้ามเขียนชื่อ)]
      ]
      #v(0.2cm)
      #grid(
        columns: (auto, 1fr),
        gutter: 1.2cm,
        
        stack(spacing: 8pt,
          align(center)[#text(weight: "bold", size: 10pt, tracking: 0.12em)[CLASS]],
          block(
            stroke: 0.8pt + gray-line,
            inset: 12pt,
            fill: white,
            [
              #set align(left)
              #stack(spacing: 12pt,
                grid(columns: (bubble_col,), align: left + horizon, text(weight: "bold", size: 12pt, fill: gray-line)[M]),
                grid(columns: (..(5 * (bubble_col,))), gutter: 0pt, align: left + horizon, ..range(1, 4).map(i => bubble(str(i)))),
                grid(columns: (..(5 * (bubble_col,))), gutter: 0pt, align: left + horizon, ..range(1, 6).map(i => bubble(str(i)))),
                grid(columns: (..(5 * (bubble_col,))), gutter: 0pt, align: left + horizon, .."ABC".clusters().map(c => bubble(c)))
              )
            ]
          )
        ),

        stack(spacing: 8pt,
          align(center)[#text(weight: "bold", size: 10pt, tracking: 0.12em)[STUDENT ID]],
          block(
            width: 100%,
            stroke: 0.8pt + gray-line,
            inset: 12pt,
            fill: white,
            [
              #stack(spacing: 12pt,
                ..range(1, 6).map(row => {
                  grid(
                    columns: (label_col, ..(10 * (bubble_col,))),
                    align: left + horizon,
                    text(weight: "bold", size: 10pt, fill: gray-line)[#row],
                    ..range(10).map(digit => align(left, bubble(str(digit))))
                  )
                })
              )
            ]
          )
        )
      )
    ]
  )
}

// ==========================================
// 6. WRITING LINES (DYNAMIC) - FINAL SOLUTION 2026-03-02
// ==========================================

#let rule_line = line(length: 100%, stroke: 0.75pt + gray-line)

#let writing_lines_dynamic(line-spacing: 1.1cm) = layout(size => {
  let count = int(size.height / line-spacing) + 1
  stack(spacing: line-spacing, ..range(count).map(_ => rule_line))
})

#let writing_lines_fixed(count, line-spacing: 1.1cm) = {
  v(0.5cm)
  stack(spacing: line-spacing, ..range(count).map(_ => rule_line))
}
