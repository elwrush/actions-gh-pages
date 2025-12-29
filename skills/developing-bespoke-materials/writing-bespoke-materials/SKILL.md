---
name: writing-bespoke-materials
description: >
  Creates custom educational materials tailored to CEFR levels and skill types. Use when
  the user wants to design worksheets, transform textbook content, or develop new teaching materials.
---

# Writing Bespoke Materials

## Purpose
Guide the creation of custom educational materials tailored to specific CEFR levels, skills, and program types. Supports both transforming existing materials and developing brand new content.

---

## Workflow

### Step 1: Initial Consultation
Greet the user and gather requirements:
- **CEFR Level**: A1, A2, B1, B2, C1, or C2
- **Skill/System**: Reading, Listening, Writing, Speaking, Grammar, Vocabulary, or Pronunciation

### Step 2: Material Source
Ask the user:
> Are you mainly wishing to **transform existing materials** or **write brand new materials**?

### Step 3: Program Type
Ask the user:
> Are you creating these materials for **regular classes** or the **Intensive program**?

### Step 4: Development Phase

#### If Transforming Existing Materials:
1. Suggest using **Gemini 3 Flash's multimodal image capabilities** to read source materials
2. Ask user to provide images/scans of the source materials
3. Extract and analyze the content
4. Work in dialog with the user to adapt and transform the materials

#### If Writing Brand New Materials:
1. Discuss the topic, context, and learning objectives with the user
2. Determine required content types:
   - 📖 Reading texts
   - 🎧 Audio scripts (for listening)
   - 🖼️ Images (use `generate_image` tool)
3. Collaborate iteratively to develop the content

> [!NOTE]
> Separate specialized skills will be provided later for:
> - Audio generation
> - Image generation
> - Reading text development

### Step 5: Draft & Approval
1. Develop all materials in **Markdown format** for readability
2. Present the draft to the user
3. **Wait for explicit approval** before proceeding

### Step 6: Export to HTML (with inline styles) as the primary format
- **File Location**: Once a material is approved, save a copy of the final HTML and any local image assets in the same folder as the source materials (e.g., the folder containing the original scans).
- Archive previous drafts in the `outputs/` folder.
1. Ask the user for the **target Google Drive folder URL**
2. Convert the Markdown materials to **Google Docs HTML format**
3. Push to the target folder

> [!IMPORTANT]
> A dedicated skill for Google Docs export will be developed later. For now, use manual conversion or existing upload methods.

---

## Conversation Starters

Use one of these to begin the workflow:

```
Hello! I'm here to help you create bespoke educational materials.

To get started, please tell me:
1. What **CEFR level** are you targeting? (A1, A2, B1, B2, C1, C2)
2. What **skill or system** do you want to focus on? (Reading, Listening, Writing, Speaking, Grammar, Vocabulary, Pronunciation)
```

---

## Quality Standards

### Content Requirements
- Age-appropriate and culturally sensitive
- Aligned with CEFR descriptors for the target level
- Clear instructions and rubrics where applicable
- Consistent formatting throughout
- **Mandatory Answer Key**: Every worksheet MUST have a complete answer key appended at the end.
- **Mandatory Transcript**: If the materials involve a listening task, the full transcript MUST be included at the end (after the answer key).

### Format Standards
- Use Markdown headers for structure
- Use tables for exercises with multiple items
- Use blockquotes for reading passages
- Use numbered lists for sequential instructions
- **Inset Images**: For professional layouts, inset images within text passages using `float: right` or `float: left`. Ensure proper margins for readability.

### File Naming Convention

```
DD-MM-YY-[Topic]-[Skill/System]-[Program]
```

| Component | Options |
|-----------|---------|
| `DD-MM-YY` | Date (e.g., `27-12-25`) |
| `Topic` | Subject matter (e.g., `Politeness`, `Past-Progressive`) |
| `Skill/System` | `Reading`, `Listening`, `Writing`, `Speaking`, `Vocab`, `Grammar`, `Pronunciation` |
| `Program` | `Bell` or `Intensive` |

**Examples:**
- `27-12-25-Politeness-Reading-Intensive.html`
- `15-01-26-Travel-Vocab-Bell.html`

---

## Templates

Reusable HTML patterns are stored in `/templates`. Copy and customize as needed:

| Template | Purpose |
|----------|---------|
| [`entry-ticket-pet-part2.html`](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/templates/entry-ticket-pet-part2.html) | PET Part 2 matching (5 items, 3 matches, 2 distractors) |
| [`vocabulary-box.html`](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/templates/vocabulary-box.html) | Horizontal word box with pipe separators |
| [`exercise-box.html`](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/templates/exercise-box.html) | Blue-shaded exercise container |
| [`glossary-box.html`](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/templates/glossary-box.html) | Red-tinted vocabulary definitions |
| [`inset-image-table.html`](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/templates/inset-image-table.html) | 2-column table for text + image layout |
| [`answer-key-section.html`](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/templates/answer-key-section.html) | Standard answer key footer |

---

## Dependencies

| Dependency | Status | Notes |
|------------|--------|-------|
| Multimodal image reading | ✅ Available | Gemini 3 Flash |
| Image generation | ✅ Available | `generate_image` tool |
| Audio generation | 🔜 Planned | Future skill |
| Google Docs export | 🔜 Planned | Future skill |
