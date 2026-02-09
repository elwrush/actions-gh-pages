# Reveal.js Activity Decision Matrix

> **OBJECTIVE**: Match the pedagogical task type to the most effective Reveal.js visual behavior. Stop using generic layouts for everything.

## 1. The "One-per-Slide" Rule (Standard)
**Use for**: Open Questions, Comprehension Checks, Definition Checks.
*   **Why**: Focuses attention on a single concept at a time.
*   **Behavior**:
    *   Slide A: Question only.
    *   Slide B: Question + Answer + Evidence + Explanation (`answer_detail` layout).
*   **Transition**: `slide` or `fade`.

## 2. The "Auto-Animate" Rule (Transformations)
**Use for**: Matching, Ordering, Gap Fills, Error Correction, Multiple Choice.
*   **Why**: Visualizes the *process* of language change or connection.
*   **Behavior**:
    *   **Matching**: Items physically move from a random list to their pair.
    *   **Gap Fill**: The word floats from a "Word Bank" into the blank space.
    *   **Error Correction**: The incorrect word glows red, then morphs into the green correct word.
    *   **Multiple Choice**: The wrong answers fade out opacity 0.2, correct answer scales up 1.2.
*   **Requirement**: strictly use `data-id` on elements to enable morphing.

## 3. The "Fragment" Rule (Lists & Drills)
**Use for**: Choral Drills, Pronunciation Lists, long checklists.
*   **Why**: Keeps the learner focused on the current item while maintaining context of the whole list.
*   **Behavior**:
    *   Use `class="fragment fade-up"`.
    *   **Current item is high contrast**; previous items remain visible but dimmed (optional).

---

## 4. Pedagogical Mappings (Human Reference)

| ESL Activity Type | Recommended Layout | Reveal.js Feature | Answer Strategy |
|:---|:---|:---|:---|
| **Comprehension Questions** | `answer_detail` | Standard Slide | **One-per-slide** (Strict) |
| **Vocabulary Definition** | `split_table` | Standard Slide | **One-per-slide** (Strict) |
| **Matching (def-word)** | `matching` | **Auto-Animate** | Items move to pair |
| **Sentence Ordering** | `ranking` | **Auto-Animate** | Strips re-order vertically |
| **Gap Fill (Word Bank)** | `cloze` | **Auto-Animate** | Word moves from bank to gap |
| **Multiple Choice** | `quiz` | **Auto-Animate** | Distractors fade, Key scales |
| **Error Correction** | `text_repair` | **Auto-Animate** | Text morphs (Bad -> Good) |
| **True/False** | `binary_choice` | **Auto-Animate** | Correct option scales/glows |

---

## 5. Script Mappings (Automated)

*Table used by `convert_plan_to_json.py`. Keys must match Mermaid node labels.*

| Activity Type | Layout |
| :--- | :--- |
| Sentence Ordering | ranking |
| Verb Matching | match_reorder |
| Mission | mission |
| Title | title |
| Video | video |
| Lead-in | video |
| Linguistic Alignment | strategy |
| Discovery | strategy |
| Reflection | strategy |
| Prep & Pronunciation | split_table |
| The Athletes | split_table |
| Default | split_table |