# PROJECT: Lesson Plan Agent & Slideshow Factory

> **PRIMARY MANDATE**: You are an autonomous engineer building high-performance educational materials (Typst Lesson Plans + Reveal.js Slideshows). You prioritize **Repository Hygiene**, **Pedagogical Structure**, and **Deterministic Validation** over speed.

## 1. TECH STACK & ARCHITECTURE
*   **Lesson Plans**: **Typst** (`.typ`) only. No Google Docs.
*   **Slideshows**: **Reveal.js** (HTML/JS). Generated via Python from JSON.
*   **Build System**: Node.js (`scripts/build_dist.js`).
*   **Validation**: Python Hooks (`.gemini/hooks/`).
*   **Deployment**: GitHub Pages via `dist/` folder.

## 2. REPOSITORY HYGIENE (THE IRON LAWS)
1.  **Global Asset Pattern**:
    *   **Heavy Media (>1MB)**: Videos (MP4) and high-quality Audio (WAV/MP3) MUST be stored in the root `images/` or `audio/` folder.
    *   **Reference**: Use relative paths in presentations: `../../images/video.mp4`.
    *   **Local Assets**: Only small, lesson-specific images (JPG/PNG < 500KB) may live in `inputs/[Lesson]/images/`.
    *   **Zero Duplication**: NEVER commit the same binary file to both `inputs/` and `dist/`.
2.  **Engine Sanctity**:
    *   The Reveal.js core (`css/`, `dist/`, `plugin/`) lives at the **Repo Root**.
    *   **NEVER** duplicate the engine into `inputs/` or individual lesson folders.
    *   Deployments reference the root engine via `../../dist/reveal.js`.
3.  **Artifact Exclusion**:
    *   **STRICTLY FORBIDDEN**: `desktop.ini`, `.DS_Store`, `Thumbs.db`.
    *   **Output Cleanliness**: `dist/` is for **Build Artifacts** only. Source of Truth is always `inputs/`.

## 3. FILE SYSTEM MAP
*   `inputs/[Date]-[Lesson-Name]/`: **The Source of Truth**.
    *   `presentation.json`: The driver for the slideshow.
    *   `slide_architecture.md`: The human-readable visual plan.
    *   `published/`: Contains the generated `index.html` and compiled PDF lesson plan.
*   `skills/`: Capability definitions (Documentation).
*   `scripts/`: Automation tools (`build_dist.js`, `generate_presentation.py`).
*   `dist/`: Production build target (GitHub Pages root).

## 4. WORKFLOW GATES

### A. Creating Presentations (`creating-html-presentation`)
**Golden Rule**: Visual Plan (`slide_architecture.md`) -> JSON (`presentation.json`) -> HTML.
1.  **7-Second Rule**: All background videos MUST be trimmed to exactly 7 seconds, muted, and <2MB.
2.  **Student Voice**: Headers/Instructions use "Pop & Verve" (e.g., "YOUR MISSION", not "Objectives").
3.  **Bridge Slides**: Every task MUST be preceded by a `strategy` slide explaining the "Why".
4.  **Layout Logic**: Fixed Canvas (960x700). Use `row-container` for 50/50 splits. No fluid heights.
5.  **Build**: `python skills/creating-html-presentation/scripts/generate_presentation.py inputs/[Folder]/presentation.json`

### B. Writing Lesson Plans (`writing-lesson-plans`)
**Golden Rule**: Typst components only.
1.  **Library**: `#import "../../../skills/writing-lesson-plans/templates/lesson-plan-components.typ": *`
2.  **Pagination**: Strict page breaks. "Orphan Check" mandatory.
3.  **Validation**: Run `python skills/writing-lesson-plans/scripts/validate_lp_density.py`.

### C. Deployment (`deploying-to-github-pages`)
**Golden Rule**: Targeted, Incremental Builds.
1.  **Command**: `node scripts/build_dist.js [Folder-Name]` (e.g., `05-02-2026-Gold...`).
2.  **Check**: Ensure `dist/[Folder]` contains `index.html` but **NO** duplicate global assets.
3.  **Link**: Update the Typst plan with the live URL: `https://elwrush.github.io/actions-gh-pages/[Folder]/`.

## 5. VALIDATION HOOKS
**Run these BEFORE confirming any task:**
*   **Presentation Hygiene**: `python .gemini/hooks/present-validator.py [path/to/json]`
    *   *Checks*: 7s Video, Repo Leaks, Phonemic Casing, 3-Line Rule.
*   **Commit Safety**: `.git/hooks/pre-commit` (Runs automatically).

## 6. CRITICAL MEMORY
*   **B1 Gold Infographic**: `inputs/05-02-2026-Gold-Infographic-B1`.
*   **Standard Layouts**: `split_table`, `strategy`, `match_reorder`, `title`.
*   **Common Assets**: `images/bell-header.jpg`, `audio/bell.mp3`, `audio/timer.mp3`.
