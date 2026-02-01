# Code Reference & Layout Catalog

> **Purpose**: Detailed reference for layouts, themes, and code patterns.
> **Use**: Consult this file during Step 3 (Config Generation).

---

## 🧠 Pedagogical Mapping Matrix (The "Brain")

**CRITICAL**: Use this table to select the correct layout for the content type. Do not guess.

| Worksheet Content Type | **MANDATORY Layout** | **Required Content Structure** |
| :--- | :--- | :--- |
| **New Concept / Strategy** | `strategy` | **Bridge Slide**: Background Color + Big Icon + Rationale. |
| **List of Vocabulary** | `split_table` | Native HTML `<table>` with icons in col 1. |
| **Matching (Word + Def)** | `match_reorder` | JSON lists (`left_items`, `right_items`). |
| **Gap Fill / Sentence Completion** | `split_table` | Native HTML `<table>` with centered numbering in col 1. |
| **Multiple Choice / Cross Out** | `split_table` | Native HTML `<table>` with strikethrough CSS in content. |
| **Discussion Questions** | `split_table` | Native HTML `<ul>` or `<table>`. **3-Line Rule**. |
| **Instructions + Timer** | `split_table` | Native HTML `<table>`. **Embed Timer Row manually**. |
| **Listening/Reading Text** | `split_task` | Text in `<p>`, Image on left. |
| **Lead-in / Warmer** | `video` or `title` | Video/Image background. |

> **⚠️ Layout Gap Analysis**: If the content does NOT fit these patterns (e.g., complex game, timeline), you **MUST** ask the user: *"This content requires a new layout. Shall I design a new template for it?"*

---

## 🏗️ Layout Catalog (The "Menu")

| Layout ID | Description | Best For |
| :--- | :--- | :--- |
| **`title`** | Gold Standard Split: Deck 1 (ALL CAPS) & Deck 2 (Title Case). | Opening slide. |
| **`segue`** | Heavy Radial Gradient with Skewed Phase markers. | Transition between phases. |
| **`strategy`** | Solid Color Background + Title + Text. | **Bridge Slides**, Context, Rules. |
| **`split_table`** | Split layout with embedded HTML table. | List-based tasks (Vocab/Matching). |
| **`match_reorder`** | Interactive Vocabulary Match. Right column morphs. | Matching tasks. |
| **`video`** | Embeds YouTube/Shorts + Floating Task Box. | Lead-ins, Warmers. |
| **`checklist`** | Grid of items for "Skim" tasks. | Simple checking tasks. |
| **`answer`** | Validation slide with "Why?" explanation box. | Answer keys. |

---

## 🎨 CSS Themes

Themes are located in `css/themes/`.

| Theme | Vibe | Usage |
| :--- | :--- | :--- |
| **`thai-heritage.css`** | **Gold Standard**. Deep Royal Blue + Gold. | Default for all academic lessons. |
| **`indonesia.css`** | Batik patterns, warm earth tones. | Cultural topics. |
| **`noir.css`** | High contrast, monochrome + red accent. | Serious/Crime topics. |
| **`cyber.css`** | Neon, dark mode, futuristic. | Tech/Sci-Fi topics. |

---

## ⚠️ Technical Pitfalls (Learned Lessons)

1.  **Pedagogical Scaffolding**:
    -   ❌ **NEVER** dump a task without context.
    -   ✅ **ALWAYS** insert a **Bridge Slide** (`strategy` layout) before every major task block (Vocab, Grammar, Speaking) to explain the *Why* and *How*.

2.  **Table Alignment**:
    -   ❌ **NEVER** rely on default left-alignment for numbers.
    -   ✅ **ALWAYS** explicitly set `text-align: center` for "Number" or "ID" columns.

3.  **Generative Hallucinations**:
    -   ❌ **NEVER** summarize or truncate source sentences in grammar/vocab tasks.
    -   ✅ **ALWAYS** verify strict verbatim alignment with the `.typ` source.

4.  **Student-Centric Voice**:
    -   ❌ **NEVER** use teacher-procedural words in student-visible areas (e.g., "Objective: Students will...", "Rationale: Focus on...").
    -   ✅ **ALWAYS** address the student directly with high energy (e.g., "YOUR MISSION", "THE CHALLENGE", "PRO TIP").

### 🎭 Tone Comparison Table

| Teacher-Facing (BANNED) | Student-Facing (REQUIRED: "Pop & Verve") |
| :--- | :--- |
| Objective: Master IPA Symbols | YOUR MISSION: Decode the Secret Code! |
| Rationale: Focus on phoneme contrasts | THE CHALLENGE: Spot the Difference! |
| Instructions: Listen and tick | LISTEN & TICK: Can you catch them all? |
| Procedural: Monitor student pairs | *[Place in <aside class="notes"> only]* |
| Note: /ɪ/ is a short vowel | PRO TIP: Keep it short and snappy! |

---

## 🧩 Copy-Paste Snippets

### Bridge Slide (Pedagogical Scaffolding)
```json
{
    "layout": "strategy",
    "title": "BUILDING BLOCKS",
    "background_color": "#C2B280",
    "icon": "fas fa-map-marked-alt",
    "content": "<p>Contextual explanation...</p>",
    "notes": "Explain why we are learning this."
}
```

### Native Table Pattern (Task/Numbered)
```html
<!-- Explicitly center the Number column to prevent visual crowding -->
<table style='width: 100%; border-collapse: separate; border-spacing: 0 20px; font-size: 0.9em;'>
    <tbody>
        <tr>
            <td style='width: 60px; text-align: center; vertical-align: middle; font-weight: bold; color: #FFD700;'>1</td>
            <td style='vertical-align: middle;'>Question text here...</td>
        </tr>
    </tbody>
</table>
```