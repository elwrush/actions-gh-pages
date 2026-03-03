# Proposed Ideal Workflow for Robust Slideshow Creation

To eliminate hallucinations, "dropped" content, and pedagogical "stupidity," the workflow is refactored into a strict multi-stage pipeline with mandatory Human-in-the-Loop (HITL) gates.

## Phase 1: Ingest & Verify (Source Gate)
- **Goal**: Establish a single, immutable source of truth.
- **Action**: Agent saves raw material to `verbatim_source.md`.
- **HITL Gate**: User confirms the source is complete and accurate.

## Phase 2: Pedagogical Blueprint (Pedagogical Gate)
- **Goal**: Design lesson logic and Q&A without layout distractions.
- **Action**: Agent creates `lesson_plan.md` with verbatim-extracted Vocab and Q&A (mapped to lines).
- **HITL Gate**: User approves the "intelligence" (CEFR level, accuracy of answers).

## Phase 3: Visual Roadmap (Structural Gate)
- **Goal**: Map the lesson plan to slides before writing code.
- **Action**: Agent creates a Mermaid diagram or `slides_outline.md` mapping tasks to slide IDs.
- **HITL Gate**: User approves the flow, sequencing, and timing.

## Phase 4: Asset Generation (Content Phase)
- **Goal**: Prepare slide data verbatim from the Blueprint.
- **Action**: Agent generates `presentation_content.json`.
- **Rule**: Content must be programmatically extracted from `lesson_plan.md` (No re-generation).

## Phase 5: Code Assembly (Construction Phase)
- **Goal**: Assemble the Reveal.js HTML.
- **Action**: Agent injects JSON into templates. No creative writing at this stage.

---
**Status**: Pending implementation into a formal skill (`creating-robust-lesson`).
