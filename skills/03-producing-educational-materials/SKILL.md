---
name: 03-producing-educational-materials
description: Handles the entire lifecycle of educational material creation: consultation, pedagogical design, and production of professional Typst worksheets. Use when the user requests the creation of worksheets, lesson plans, or educational PDFs.
---

# Producing Educational Materials

## Purpose
Guide the transition from raw educational requirements to print-ready, professionally branded PDF worksheets. Consolidates pedagogical design with high-density Typst production. 

### 🛑 MANDATORY: ZERO HALLUCINATION POLICY
**You MUST NOT guess Typst syntax.** Before you write or edit any `.typ` file (Phase 4), if you are unsure of a layout, table, or list implementation, you **MUST** use the `consult_repo` tool (from skill 16) to check the official Typst repository (`typst:crates/typst-library/src/`).

## STRICT RULE: NEVER abbreviate, change, or truncate source text. Professional materials must maintain 100% instructional integrity.**

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
        LP --> DP[Dependency Discovery: Verify lib.typ & Paths]
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

    subgraph "Phase 4: Production & Export"
        SP --> BI{Booklet Needed?}
        BI -->|Yes| BO[Apply Imposition: 2,3,1,4 / 2,3,1]
        BI -->|No| TE[Typst Execution: Markup Eval]
        BO --> TE
        TE --> VAL[Validation: Code & Content Audit]
        VAL --> LG[🏁 Link Gate & Approval]
    end

    style PH fill:#f9f,stroke:#333,stroke-width:2px
    style MS fill:#f9f,stroke:#333,stroke-width:2px
    style LP fill:#bbf,stroke:#333,stroke-width:2px
    style DP fill:#bbf,stroke:#333,stroke-width:2px
```

---

## Workflow

### Step 1: Requirements Gathering & Consultation
You MUST consult with the user on these core constraints:
- **CEFR Level**: A1-C2 (mandatory).
- **Skill/System**: Reading, Listening, Writing, Speaking, Grammar, Vocabulary, or Pronunciation.
- **Duration**: Target lesson length.
- **Program Selection**: **CRITICAL**. Prompt user to choose between **Bell** and **Intensive**. 
  - *Assets Location*: Branded straps found in `C:\Users\elwru\AppData\Roaming\typst\packages\local\bell-sheets\0.1.0\images\`.
- **Hero Image Requirement**: **MANDATORY**. Every worksheet MUST have a hero image.
  - Ask the user for keywords to search Pixabay.
  - If Pixabay search fails or is unsuitable, prompt the user to provide a manual image path.
- **Badge Choice**: **MANDATORY**. Always include exactly three badges: CEFR Level, Skill, and Topic.
  - *Format*: Maroon rectangles with white bold text.
  - *Constraint*: Never include lesson duration in a badge.
- **Mission Mandate (The 'Cambridge Hook')**:
    -   **Headline**: MUST be "YOUR MISSION" in maroon bold.
    -   **Intro Text**: MUST explain the relevance to a specific Cambridge exam (e.g., "In your PET for Schools exam, you often have to...").
    -   **Structure**: A light pink block with a maroon border.
    -   **Icons**: 3 distinct boxes/columns for objectives, each with a relevant icon.
- **Writing/Critical Thinking Choice**: **MANDATORY**. Prompt user: *"Would you like to include an extension writing or critical thinking task? (Yes/No)"*.
  - **Action**: If "Yes", you MUST design a task aligned with the CEFR profile. If "No", do NOT invent any personal response or analysis tasks.
  - **Action**: If "Yes", you MUST execute Step 2 (Deterministic Gate).

### Step 2: Deterministic Data Gate (If Quiz is 'Yes')
To prevent LLM "probabilistic laziness" in option placement:
1. **Script First**: Write and run a Python script to generate randomized answer keys (e.g., `[1, 0, 1, 1...]`) and select anchor quotes from the text.
2. **Injunction**: Force the LLM to write questions where the correct answer **MUST** align with the indices provided by the script.

### Step 3: Dependency Discovery (Pre-Production)
Before writing any code, you MUST verify the environment:
- **Library Audit**: You MUST use the **GitHub API (Skill 16)** to consult the official Typst repository (`typst/typst`) for syntax verification. For the local project library, use `read_file` on `lib/typst/lib.typ`.
- **Path Verification**: Ensure images are downloaded using Pixabay Skill: `C:\PROJECTS\LESSONS AND SLIDESHOWS 2\skills\04-searching-pixabay\scripts\download_image.py`.

### Step 4: Content & Layout Strategy
- **Rule: Verbatim Mandate**: **CRITICAL**. You MUST use the source text EXACTLY as provided in the raw files.
- **Rule: Meander for Maps & Visuals**: **MANDATORY**. You MUST use the **Meander (Skill 08)** package to insert maps or large hero images into the worksheet. This ensures text wraps professionally around the visual and provides maximum visibility for student reference.
- **Rule: No Illegal Page Breaks**: **MANDATORY**. Do NOT put a manual page break (`#pagebreak()`) before small tasks (e.g., Task 3, Task 4) unless they truly require a new page. Let the content flow naturally.
- **Rule: Proper Enumeration**: **MANDATORY**. Use Typst's native enum syntax for tasks with lettered options (a, b, c). Example: `#set enum(numbering: "a)")` followed by `+ Item`. NEVER manually type `a)`.
- **Rule: Double Spacing for Handwriting**: **MANDATORY**. Tasks requiring student handwriting (gap-fills, dialogues) MUST be double-spaced or have significantly increased leading. Use `#set par(leading: 1.2em)` or `#v(0.8cm)` between lines.
- **Rule: ID Block Logic**: **CRITICAL**. 
    - ONLY include the `#identity_block()` if there is a **submitted writing task**. 
    - If the user explicitly stated "No" to a writing task (e.g., in Step 1 consultation), you MUST NOT include the ID block. 
    - Note-taking or roleplay prep (like Task 5) does NOT count as a submitted writing task.
- **Rule: Paragraph Numbering**: **MANDATORY**. 
  - All reading texts MUST have numbered paragraphs to facilitate classroom reference.
  - Prefix every paragraph with a bold, maroon number: `#text(fill: maroon, weight: "bold")[[1]]`.
- **Rule: Multiple Choice Formatting**: **MANDATORY**. 
  - NEVER use run-on lines for choices. Use vertical enums or 2-column grids.
- **Rule: Question-Answer Integrity**: **MANDATORY**.
  - Questions and their corresponding ruled lines MUST be wrapped in a non-breakable block (e.g., `#block(breakable: false, [...])`) to prevent them from being separated by page breaks.
- **Rule: Handwriting Space**: **MANDATORY**.
  - All ruled lines for handwriting MUST have a minimum vertical clearance of 0.8cm (`#v(0.8cm)`).
- **Rule: Dynamic Writing Lines**: **MANDATORY**.
  - Writing tasks MUST use the library function `#writing_lines_dynamic()` which utilizes the `layout(size => ...)` engine.
  - NEVER attempt to calculate remaining space manually using `page.margin` math. The `size.height` provided by the `layout` block is the only source of truth for available vertical space.
  - The line count formula is strictly $n = \text{int}(H/S) + 1$ to ensure the last line reaches the bottom margin.
- **Rule: Single-Column & Natural Flow (Starting State)**: **MANDATORY**. 
  - ALWAYS start the first draft with a **single-column layout**.

### Step 5: Design Strategy & Styling
For detailed typography, spacing, and branding standards, refer to **[styling.md](references/styling.md)**.

### Step 6: Rendering & Validation
1. **Compile**:
   ```powershell
   typst compile "inputs/[folder]/[filename].typ" "inputs/[folder]/published/DD-MM-YYYY-[LEVEL]-[TITLE].pdf" --root "."
   ```
2. **Validate**:
   ```powershell
   python scripts/validate_text.py "path/to/source.typ"
   ```

### Step 7: 🏁 THE LINK GATE
> [!CRITICAL]
> **YOU MUST PROVIDE A CLICKABLE LINK TO THE PDF.**
> Post the link using the `file:///` protocol. Do NOT proceed until the user approves the visual output.

---

## Reference Material
- **Skill Architecture Standard**: `C:\PROJECTS\LESSONS AND SLIDESHOWS 2\knowledge_base\using-skills.md`
- **Visualization Tool**: `C:\PROJECTS\LESSONS AND SLIDESHOWS 2\skills\rendering-prompts-into-mermaid\SKILL.md`
- **Styling Guide**: `C:\PROJECTS\LESSONS AND SLIDESHOWS 2\skills\producing-educational-materials\references\styling.md`
- **Typst Library**: `C:\Users\elwru\AppData\Roaming\typst\packages\local\bell-sheets\0.1.0\lib.typ`
