---
description: The Master Gated Pipeline for all lesson plan and slideshow creation.
---

# Master Workflow: The Gated Robust Pipeline

> **CRITICAL**: Before ANY task, execute the Skill Activation Gate (Section 0).

---

## SECTION 0: SKILL ACTIVATION (MANDATORY FIRST STEP)

1. **DETECT** task type from user request using the matrix in `AGENTS.md`
2. **READ** the corresponding `skills/[skill]/SKILL.md` file completely
3. **ANNOUNCE**: "✅ Skill loaded: [skill-name]"
4. **EXECUTE** the workflow below

**FAILURE TO LOAD THE CORRECT SKILL IS A CRITICAL ERROR.**

---

## SECTION 1: TASK ROUTING

| Task Type | Skill to Load | Workflow Phase |
|:---|:---|:---|
| Create lesson plan | `skills/writing-lesson-plans/SKILL.md` | Phase 2 |
| Create worksheet | `skills/producing-educational-materials/SKILL.md` | Phase 2 |
| Create presentation | `skills/producing-educational-materials/SKILL.md` | Phases 3-5 |
| Generate quiz | `skills/generating-quizzes/SKILL.md` | Standalone |
| Search images | `skills/searching-pixabay/SKILL.md` | Phase 4 |
| Deploy slides | `skills/deploying-to-github-pages/SKILL.md` | Phase 5 |
| Get transcript | `skills/grabbing-youtube-transcripts/SKILL.md` | Standalone |
| Commit changes | `skills/committing-project-to-github/SKILL.md` | Standalone |

---

## PHASE 1: INGESTION & VERIFICATION (The Source Gate)

**Trigger**: User provides source materials (PDF, Typst, Images, Video)

1. **Source Extraction**: Read the source PDF/Typst/Text/Video
2. **Checklist Creation**: Create `inputs/[Lesson]/SOURCE_TEXT.md`
   - Extract ALL vocabulary, definitions, task instructions, Q&A verbatim
   - Number paragraphs systematically (Para 1, Para 2, etc.)
   - Solve all tasks (Genre, Recall, Analysis) WITHIN the file
3. **GATE**: Present checklist to user. **STOP AND WAIT** for approval.
   - Ask: "Does this checklist contain every single question and answer needed?"

---

## PHASE 2: PEDAGOGICAL BLUEPRINT (The Lesson Plan Gate)

**Trigger**: Source content approved in Phase 1

1. **Drafting**: Write the Typst Lesson Plan (`[Date]-LP-[Name].typ`) in `inputs/[Lesson]/published/`
2. **Pedagogy**: Ensure Stage → Strategy → Task → Answer logic is sound
3. **Validation**: Run `python skills/writing-lesson-plans/scripts/validate_lesson_plan.py`
4. **GATE**: **STOP AND WAIT** for user approval of the compiled PDF.
   - Ask: "Is the teaching logic sound? Is the CEFR level appropriate?"

---

## PHASE 3: VISUAL ROADMAP (The Structural Gate)

**Trigger**: Lesson Plan approved in Phase 2

1. **Mapping**: Create `inputs/[Lesson]/visual_plan.md`
2. **Layouts**: Map lesson stages to Reveal.js layouts (Title, Mission, Segue, Strategy, Task, Answer)
3. **Asset Planning**: Identify required images/videos/icons
4. **GATE**: **STOP AND WAIT**.
   - Agent MUST provide a clickable link to the `visual_plan.md`.
   - User reviews and edits the markdown file directly.
   - User approves the visual flow.

---

## PHASE 4: ASSET GENERATION (The Content Phase)

**Trigger**: Visual Roadmap approved in Phase 3

1. **User Input**: **STOP AND ASK**: "I am about to acquire assets. Do you have any specific images, videos, or files you want me to use?"
2. **Sourcing**: Use `skills/searching-pixabay/SKILL.md` to find missing assets
3. **Processing**: Ensure all videos are 7s loops, 720p, and muted
4. **Data Assembly**: Write `inputs/[Lesson]/presentation.json`
5. **GATE**: Self-verify against `SOURCE_TEXT.md`.
   - Ask: "Did I include every question from Phase 1?"

---

## PHASE 5: CODE ASSEMBLY (The Construction Phase)

**Trigger**: Assets assembled in Phase 4

1. **Building**: Run `python scripts/fast_edit.py [lesson-name]`
2. **Validation**: Run `python .gemini/hooks/present-validator.py [lesson-name]`
3. **Preview**: Provide the localhost link for final review
4. **GATE**: FINAL REVIEW. **STOP AND WAIT** for user approval.

---

## STANDALONE WORKFLOWS

### Deploy Slides
1. Build: `python scripts/build.py [lesson-folder]`
2. Push: Follow `skills/deploying-to-github-pages/SKILL.md`
3. Sync URL: `python skills/deploying-to-github-pages/scripts/sync_lesson_plan_url.py`

### Generate Quiz
1. Load `skills/generating-quizzes/SKILL.md`
2. Follow multi-stage logic (Anchors → Questions → Validation)

### Get YouTube Transcript
1. Load `skills/grabbing-youtube-transcripts/SKILL.md`
2. Run: `python skills/grabbing-youtube-transcripts/scripts/grab_transcript.py [VIDEO_ID] --output inputs/[TOPIC]/transcript.txt`

### Commit Changes
1. Load `skills/committing-project-to-github/SKILL.md`
2. Filter: `git reset **/desktop.ini`
3. Stage and commit with verbose message

---

## QUICK REFERENCE: VALIDATION SCRIPTS

| Check | Script |
|:---|:---|
| Presentation | `python .gemini/hooks/present-validator.py [lesson]` |
| Lesson Plan | `python skills/writing-lesson-plans/scripts/validate_lesson_plan.py [file.typ]` |
| Content Alignment | `python skills/creating-html-presentation/scripts/validate_content_alignment.py [json]` |
| Answer Separation | `python skills/creating-html-presentation/scripts/validate_answer_separation.py [json]` |

---

*Master workflow consolidated February 10, 2026. All stub workflows deprecated.*
