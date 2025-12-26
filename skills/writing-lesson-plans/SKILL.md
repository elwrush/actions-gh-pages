---
name: writing-lesson-plans
description: >
  Interactive lesson planning workflow. Use when the user wants to create
  a lesson plan, design a lesson, or prepare teaching materials. Guides
  through shape selection, metadata collection, and lesson generation.
---

# Writing Lesson Plans

This skill guides you through an 8-step interactive workflow to create a lesson plan.

## Prerequisites

- Access to `knowledge_base/lesson_shapes.yaml` for shape definitions
- Materials in `/inputs` subfolder (or user will design new materials)

## Workflow

### Step 1: Present Lesson Shape Menu

Load shapes from `knowledge_base/lesson_shapes.yaml` and present:

```
Which lesson shape would you like to use?

A. Text-based presentation of language
B. Language Practice
C. Test-Teach-Test (TTT)
D. Situational Presentation (PPP)
E. Receptive Skills (Reading/Listening)
F. Productive Skills (Speaking/Writing)
G. Task-Based Learning (TBL)
```

### Step 2: Collect Lesson Metadata

Ask for:
- **CEFR Level**: A1, A2, B1, B2, C1, C2
- **Focus**: Systems (Grammar/Vocabulary/Pronunciation) or Skills (Reading/Writing/Listening/Speaking)
- **Teacher Name**
- **Duration**: Total lesson time in minutes
- **Textbook/Unit**: If using coursebook
- **Page Numbers**: Relevant pages
- **Assessment Type**: CA (Continuous Assessment), formal test, or n/a

### Step 3: Materials Source

Ask:
> "Will you be designing new materials (separate skill) or using pre-existing materials?"

If pre-existing:
1. List subfolders in `/inputs`
2. Ask user to select one
3. Note: Actual file scanning uses a separate multimodal skill

### Step 4: Clarify Materials

If materials are unclear, ask specific questions:
- What is the main topic/context?
- What target language items are covered?
- Are there audio/video components?
- Are there exercises with answer keys?

### Step 5: Special Requests

Ask:
> "Any special requirements for this lesson? (e.g., specific activities, time constraints, student needs)"

### Step 6: Suggest Objective + Marker Sentences

Based on collected information:

1. **Propose lesson objective** using format:
   > "By the end of the lesson, learners will be better able to [skill/language point] in the context of [topic]."

2. **Suggest marker sentences** (for shapes A, B, C, D):
   > Example sentences containing target language for clarification stages.

Wait for user approval before proceeding.

### Step 7: Write Lesson Plan

Generate the lesson plan using **markdown tables**:

#### Header Format
```markdown
**[Unit Title]**
**Aim**: [Objective from Step 6]
**Systems/Skills**: [From Step 2]
**Page Numbers**: [From Step 2]
**Assessment**: [From Step 2]
```

#### Stage Table Format
| Stage | Aim | Procedure | Time | Interaction |
|-------|-----|-----------|------|-------------|
| 1 | To lead-in | [Detailed procedure] | 5 | T-Ss |
| 2 | To [stage aim] | [Detailed procedure] | 8 | Ss-Ss |

#### Required Additions

> [!IMPORTANT]
> - **Shape E (Receptive Skills)**: MUST include a "Pre-teach Vocabulary" stage immediately after Lead-in
> - **Shape E (Listening)**: Include full transcript at the end
> - **All lessons with exercises**: Include answer keys as footer section

#### Pre-teach Vocabulary Format (Shape E)

Select **5 words** from the source text that would be challenging for learners at the given CEFR level.

**Format for each word:**

```
word /phonemic script/: Thai translation
English context sentence with **target word** highlighted.
Thai context sentence with **คำแปล** highlighted.
```

**Example:**
```
postpone /pəʊstˈpəʊn/: เลื่อน
They decided to **postpone** the meeting until next week.
พวกเขาตัดสินใจ**เลื่อน**การประชุมไปสัปดาห์หน้า
```

### Step 8: Export Prompt

Once lesson plan is approved, ask:
> "Ready to convert to HTML and upload to Google Docs?"

This triggers the `uploading-to-google-docs` skill.

---

## Reference Files

For full lesson shape details and examples, see:
- [REFERENCE.md](REFERENCE.md) - Shape summaries
- [lesson_shapes.yaml](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/knowledge_base/lesson_shapes.yaml) - Complete definitions

---

## Output Example

See [REFERENCE.md](REFERENCE.md) for a complete lesson plan example.
