---
name: creating-html-presentation
description: Generates vibrant Reveal.js HTML presentations from materials and instructions. Handles design, animation, and strict content validation. Use when the user wants to generate a Reveal.js slideshow from lesson content or educational materials.
---

# Skill: Creating HTML Presentations (`creating-html-presentation`)

**Version**: 6.0 (Pedagogical Architecture + Layout Gap Analysis)

## Description
This skill generates high-energy Reveal.js presentations. It mandates a **Pedagogical Architecture** (Schema Activation -> Task) and operates on a **Local-First Architecture**. It strictly enforces content alignment and layout suitability.

## Core Mandates
1.  **Pedagogical Scaffolding**: **NEVER** present a task without a preceding "Bridge Slide" (Strategy/Context). Use the `strategy` layout to explain the "Why" before the "What".
2.  **Layout Gap Analysis**: If the content does not fit an existing layout (`REFERENCE.md`), you **MUST** ask the user to authorize designing a new template. Do not shoehorn complex content into simple lists.
3.  **Local-First Architecture**: **ABSOLUTELY NO CDNs** (except FontAwesome). All code comes from `temp_reveal_repo`.
4.  **Verbatim Fidelity**: Content in the slide JSON must match the `.typ` source 100%. No summarization.
5.  **Pedagogical UI**: Use **Dual Coding** (Icons + Text) and **Negative Feedback** animations (Red Strikethrough).
6.  **Phonemic Casing**: Phonemic script (text within slashes, e.g., /tɒm/) MUST NEVER use upper-case Latin letters (A-Z). Phonemes are always lower-case or specific IPA symbols.
7.  **Student-Centric Voice**: All visible slide content (titles, instructions, rationales) **MUST** be addressed directly to the student using an engaging, high-energy "Pop & Verve" tone (e.g., "YOUR MISSION", "THE CHALLENGE", "FINAL CHALLENGE"). **NEVER** use teacher-facing procedural language (e.g., "Objective", "Rationale", "Monitor") in student-visible areas. These belong exclusively in `<aside class="notes">`.

## Workflow

### Phase 0: 🧠 Discovery & Architecture
**Goal**: Define the "Master Blueprint" and validate Layout Fit.
1.  **Ingest Materials**: Read `.typ` files (Source of Truth).
2.  **Map Tasks**: Consult `REFERENCE.md` -> **Pedagogical Mapping Matrix**.
3.  **Layout Gap Check**:
    *   *Check*: Does every task map cleanly to a layout?
    *   *Action*: If NO, ask user: *"Task X requires a new layout. Shall I design one?"*
4.  **Draft Architecture**: Create `slide_architecture.md`. Define the layout for *every* slide, including mandatory **Bridge Slides**.

### Phase 1: 📊 Pedagogical Mapping (Visualization)
**Goal**: Verify the Learning Journey.
1.  **Execute**: `skills/rendering-prompts-into-mermaid`.
2.  **Constraint**: Nodes must be labeled with `[Layout ID]`.
3.  **Verify Flow**: Check for **Bridge Node** -> **Task Node** -> **Feedback Node** pattern. If Bridge is missing, add it.

### Phase 2: 📦 Asset Strategy
**Goal**: Secure high-quality visuals.
1.  **User-Led Generation**: Provide prompts. Wait for user to provide images.
2.  **Organization**: Store in `inputs/[Folder]/images/`.

### Phase 3: 🎨 Config Generation (The Plan)
**Goal**: Create the JSON driver.
1.  **Generate**: Create `presentation.json`.
2.  **Constraint**: Use layouts from `REFERENCE.md`. Prefer `split_table` for tasks.
3.  **Gatekeeper Validation**:
    *   **CRITICAL STEP**: Run `scripts/validate_content_alignment.py [json_path]`.
    *   **Action**: If fails, **STOP** and fix JSON.

### Phase 4: 🛠️ Build & Render
**Goal**: Generate the HTML using the Local Repo.
1.  **Execute**: `python skills/creating-html-presentation/scripts/generate_presentation.py [json_path]`.
2.  **Output**: `index.html` in the project folder.

### Phase 5: 🧪 Final Validation
**Goal**: Ensure technical stability.
1.  **Run Suite**:
    *   `python skills/creating-html-presentation/scripts/validate_presentation.py` (Checks assets, CSS).
    *   `python skills/creating-html-presentation/scripts/validate_pedagogical.py` (Checks timer/answer logic).

## Scripts
*   `validate_content_alignment.py`: **[Critical]** Checks JSON against `.typ` source.
*   `generate_presentation.py`: Builds the HTML from JSON using **Local Repo**.
*   `validate_presentation.py`: Checks HTML structure and assets.

> **Tip**: See `REFERENCE.md` for the **Pedagogical Mapping Matrix**, code snippets, and layout documentation.
