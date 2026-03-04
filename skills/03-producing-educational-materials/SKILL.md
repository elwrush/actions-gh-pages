---
name: 03-producing-educational-materials
description: Handles the entire lifecycle of educational material creation: consultation, pedagogical design, and production of professional Typst worksheets. Use when the user requests the creation of worksheets, lesson plans, or educational PDFs.
---

# Producing Educational Materials

## Purpose
Guide the transition from raw educational requirements to print-ready, professionally branded PDF worksheets. Consolidates pedagogical design with high-density Typst production.

### 🛑 MANDATORY: ZERO HALLUCINATION POLICY
**You MUST NOT guess Typst syntax.** Before you write or edit any `.typ` file (Phase 4), if you are unsure of a layout, table, or list implementation, you **MUST** consult the official repositories using **Skill 16**:
`python skills/16-consulting-global-repos/scripts/gh_fetch.py typst:crates/typst-library/src/...` or `python skills/16-consulting-global-repos/scripts/gh_fetch.py reference:path/to/template`. The local `/lib/` folder is **DELETED and LEGACY**.

## STRICT RULE: NEVER abbreviate, change, or truncate source text. Professional materials must maintain 100% instructional integrity.

## Workflow Visualization
```mermaid
graph TD
    subgraph "Phase 1: Analysis & Strategy"
        A[Consultation: CEFR/Skill/Prog/Dur/Images/Quiz/Writing] --> B{Strategy: Transform or Create?}
        B -->|Transform| C[Multimodal Content Extraction]
        B -->|Create| D[Pedagogical Content Design]
        C & D --> LP[Linguistic Alignment: CEFR Profile Sync]
    end

    subgraph "Phase 2: Dependency & Logic"
        LP --> DP[Dependency Discovery: Verify Skill 16 Consultation]
        DP --> DG{Quiz/Writing Required?}
        DG -->|Yes| DK[Deterministic Gate: Scripted Keys/Anchors/Prompts]
        DG -->|No| IM
        DK --> IM
    end

    subgraph "Phase 3: Visuals & Layout"
        IM{Hero Image Source} -->|Pixabay| SIG[Search & Download]
        IM -->|User| UPL[User Provides Path]
        SIG & UPL --> LOG[Layout: Logical Sequential Silos]
        LOG --> PH[Page 1 Rules: Logo + v0.1cm + Badges Left + HeroStrap]
        PH --> MS[Mandatory Mission: 'YOUR MISSION' Exam Hook]
        MS --> ID[ID Block Placement: ALWAYS immediately before the Writing Task, preceded by a mandatory #pagebreak()]
        ID --> SP[Strict Spacing: 0.55em Body / 0.9cm Writing]
    end

    subgraph "Phase 4: Production & Validation"
        SP --> TE[Typst Execution: Markup Eval]
        TE --> VAL[Validation: Code & Content Audit]
        VAL --> LG[🏁 Link Gate & Approval]
    end
```

---

## Workflow

### Step 1: Requirements Gathering & Consultation (PRE-FLIGHT GATE)
Before generating any layout or Typst code, you MUST complete this pre-flight gate:

1.  **Locate Source Materials**: Ask for the source material location.
2.  **Verify Ingestion**: Ensure `SOURCE_TEXT.md` exists with `(Count: X)` tags.
3.  **Read the Lesson Plan**: Read the associated `-LP.typ` file to ensure pedagogical alignment and re-order tasks if necessary to match the lesson flow.
4.  **THE TRUNCATION LAW**: **ZERO TOLERANCE**. Every task, sentence, and exercise from `SOURCE_TEXT.md` MUST appear in the final worksheet. Check the `(Count: X)` tags meticulously.
5.  **Multi-Page Writing Mandate**: If a writing task is > 150 words (e.g., Task 8's 225-word draft), you MUST provide a full extra page of writing lines.

You MUST consult with the user on these core constraints:
- **CEFR Level**: A1-C2 (mandatory).
- **Skill/System**: Reading, Listening, Writing, Speaking, Grammar, Vocabulary, or Pronunciation.
- **Duration**: Target lesson length.
- **Program Selection**: **CRITICAL**. Prompt user to choose between **Bell** and **Intensive**.
  - *Assets*: Standard straps found in `/lib/typst/images/`.
- **Hero Image Requirement**: **MANDATORY**. Every worksheet MUST have a hero image.
  - Ask the user for keywords to search Pixabay.
  - If Pixabay search fails or is unsuitable, prompt the user to provide a manual image path.
- **Badge Choice**: **MANDATORY**. Always include exactly three badges: CEFR Level, Skill, and Topic.
  - *Format*: Maroon rectangles with white bold text.
- **Mission Mandate (The 'Cambridge Hook')**:
    -   **Headline**: MUST be "YOUR MISSION" in maroon bold.
    -   **Intro Text**: MUST explain the relevance to a specific Cambridge exam (PET/First).
    -   **Structure**: A light pink block with a maroon border.
    -   **Icons**: 3 distinct boxes/columns for objectives, each with a relevant icon.
- **Writing/Critical Thinking Choice**: **MANDATORY**. Prompt user: *"Would you like to include an extension writing or critical thinking task? (Yes/No)"*.

### Step 2: Dependency Discovery (Pre-Production)
Before writing any code, you MUST verify the environment:
- **Autonomous Library Acquisition**: You MUST fetch necessary branding syntax and logic from the global source of truth using **Skill 16**.
- **Path Verification**: Ensure images are downloaded using Pixabay Skill: `python skills/04-searching-pixabay/scripts/download_image.py`. All paths MUST be root-relative.

### Step 3: Content & Layout Strategy
- **Rule: Verbatim Mandate**: **CRITICAL**. You MUST use the source text EXACTLY as provided.
- **Rule: Meander for Maps & Visuals**: **MANDATORY**. Use **Meander (Skill 08)** for maps or large hero images to ensure professional text wrapping.
- **Rule: Task Integrity**: **MANDATORY**. Wrap task headers and content in `#block(breakable: false, [...])` to prevent illegal page breaks.
- **Rule: No Task Page Breaks**: **STRICT**. You MUST NOT include `#pagebreak()` before any task EXCEPT for the final optional writing task (usually Task 4 or 5).
- **Rule: ID Block Logic**: **CRITICAL**. ONLY include the `#identity_block()` if there is a **submitted writing task**. Place it immediately before the writing task, preceded by a `#pagebreak()`.
- **Rule: Paragraph Numbering**: **MANDATORY**. All reading texts MUST have bold, maroon paragraph numbers: `#text(fill: maroon, weight: "bold")[[1]]`.
- **Rule: Writing Lines (The Spacing Law)**:
  - **Dynamic (Fill-to-Bottom)**: For the final writing task, use a fractional block to fill the remaining page space. This is the **OFFICIAL 2026 PATTERN**:
    ```typst
    #block(width: 100%, height: 1fr)[
      #grid(
        columns: (100%),
        rows: (1.1cm), // Standard handwriting spacing
        stroke: (bottom: 0.5pt + gray),
        ..for _ in range(25) { ([ ],) } // Oversupply rows; 1fr block handles clipping
      )
    ]
    ```
  - **Fixed**: For short, specific space needs (e.g., 5 lines), use `#writing_lines_fixed(5)`.
  - **Handwriting Space**: Minimum 0.8cm clearance (`#v(0.8cm)`) for all handwritten response areas.
- **Rule: Grid Answer Lines**: Use `#box(width: 3cm, stroke: (bottom: 0.75pt + black), outset: (bottom: 2pt), baseline: 15%)[#hide[a]]` for numbered answer lines in grids to ensure stroke alignment with text.

### Step 4: Rendering & Validation
1.  **Compile**:
    ```powershell
    typst compile "inputs/[folder]/[filename].typ" "inputs/[folder]/published/[filename].pdf" --root "."
    ```
2.  **Validate**: Run `python .gemini/hooks/typst_guard.py` to check for syntax regressions and layout violations.

### Step 5: 🏁 THE LINK GATE
> [!CRITICAL]
> **YOU MUST PROVIDE A CLICKABLE LINK TO THE PDF.**
> Post the link using the `file:///` protocol. Do NOT proceed until the user approves the visual output.

---

## Reference Material
- **Skill Architecture Standard**: `/knowledge_base/using-skills.md`
- **Styling Guide**: `/skills/03-producing-educational-materials/references/styling.md`
- **Official Typst Source**: `https://github.com/typst/typst` (Consult via Skill 16)
