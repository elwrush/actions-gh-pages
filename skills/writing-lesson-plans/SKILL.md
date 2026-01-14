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

- Access to `knowledge_base/shapes/` directory for modular shape definitions
- Materials in `/inputs` subfolder (or user will design new materials)

## Workflow

### Step 1: Present Lesson Shape Menu

Load shapes from `knowledge_base/shapes/` directory and present:

```
Which lesson shape would you like to use?

A. Text-based presentation of language
B. Language Practice
C. Test-Teach-Test (TTT)
D. Situational Presentation (PPP)
E. Receptive Skills (Reading/Listening - Traditional)
F. Productive Skills (Speaking/Writing - Traditional)
G. Task-Based Learning (TBL)
H. SCR Receptive Skills (Reading/Listening - Storytelling Framework)
I. SCR Systems (Grammar/Vocabulary - Storytelling Framework)
J. SCR Productive Skills (Speaking/Writing - Message Structure)
```

### Step 2: Collect Lesson Metadata

Ask for:
- **CEFR Level**: A1, A2, B1, B2, C1, C2
- **Focus**: Systems (Grammar/Vocabulary/Pronunciation) or Skills (Reading/Writing/Listening/Speaking)
- **Teacher Name**: Defaults to **Ed Rush** (Always use this unless specified otherwise)
- **Duration**: Total lesson time in minutes
- **Textbook/Unit**: If using coursebook
- **Page Numbers**: Relevant pages
- **Assessment Type**: CA (Continuous Assessment), formal test, or n/a

### Step 3: Lesson Type

Ask:
> "Is this an **Intensive** or **Regular Bell** lesson?"

This determines which header image to use:
- **Intensive**: `intensive-header.jpg`
- **Regular Bell**: `bell-header.jpg` (or appropriate regular header)

### Step 4: Materials Source

Ask:
> "Will you be designing new materials (separate skill) or using pre-existing materials?"

If pre-existing:
1. List subfolders in `/inputs`
2. Ask user to select one
3. Note: Actual file scanning uses a separate multimodal skill

### Step 5: Clarify Materials

If materials are unclear, ask specific questions:
- What is the main topic/context?
- What target language items are covered?
- Are there audio/video components?
- Are there exercises with answer keys?

### Step 6: Special Requests and Notes

Before generating the lesson plan, ask:
> "Do you have any special requests or notes for this lesson? (e.g., include a YouTube video, emphasize particular exercises, specific activities, time constraints, student needs)"

Wait for user response and incorporate their requests into the lesson plan.

### Step 7: Suggest Objective + Marker Sentences

Based on collected information:

1. **Propose lesson objective** using format:
   > "By the end of the lesson, learners will be better able to [skill/language point] in the context of [topic]."

2. **Suggest marker sentences** (for shapes A, B, C, D):
   > Example sentences containing target language for clarification stages.

Wait for user approval before proceeding.

> [!CRITICAL]
> ## Model Compliance Requirement
> 
> Before generating the lesson plan, **consult the model lesson plan** for the selected shape in `knowledge_base/shapes/shape-[letter].yaml`.
> 
> The generated lesson plan must:
> 1. **Match the stage structure** of the model (not be a slavish rendering of materials)
> 2. **Follow the pedagogical intent** - e.g., Shape E focuses on skills, not language
> 3. **Use similar stage headers** - e.g., "Lead-in", "Reading for detail", "Post-reading"
> 4. **Maintain similar timing proportions** - the model shows where to invest time
> 5. **Consolidate activities** into logical stages rather than listing each exercise separately
> 
> **Example: Shape E (Receptive Skills) model has only 3 stages:**
> - Stage 1: Lead-in (6 min) - Multi-part warmup with prediction/discussion
> - Stage 2: Reading for detail and specific information (22 min) - Main reading tasks
> - Stage 3: Post-reading speaking task (2 min) - Brief personalization/discussion
> 
> **Do NOT** create 6+ granular stages for each worksheet section. Combine related activities into coherent stages that match the model.

> [!IMPORTANT]
> ## McKinsey Storylining & Strategic Pedagogy
> 
> Do NOT slavishly and mechanistically reproduce the structure of worksheets. Also, **AVOID labored, hokey, or intrusive metaphors** (e.g., Turning everything into "Coding", "Heroes", or "Mechanics").
> 
> Instead:
> - **McKinsey Logic**: Use the **SCR Framework** (Situation, Complication, Resolution) to structure the lesson flow.
> - **Dot-Dash Strategy**: Organize key points as **Dots** (Headlines) and evidence as **Dashes** (Details).
> - **Similes over Metaphors**: When explain pedagogy, use **professional similes** rather than deep metaphors. 
>   - *Example (Simile)*: "Like an architect sketching a plan, we must outline our ideas before writing."
>   - *Avoid (Labored Metaphor)*: "You are the Programmer, and Paragraph 2 is your System Architecture."
> - **Strategic Clarity**: Frame material as an expert consultant would—focused on *influence* and *clarity*.

### Step 8: Write Lesson Plan (HTML for GDocs)

Generate the lesson plan **directly in HTML format** for native Google Docs editing. 

> [!IMPORTANT]
> **Gold Standard Template**: Use `inputs/05-Social-Media-Reading/06-01-26-LP B1-Social-Media-Reading-Shape H.html` as the structural and styling reference.
> - Use 1-cell tables for colored boxes (e.g. Differentiation).
> - Use standard HTML tables for lesson stages.
> - Ensure all styles are **inline** (`style="..."`).
> - Use **relative paths** for images to ensure correct base64 embedding during push (`../../images/...`).

#### File Naming Convention
Store in the **source folder** (same as materials) with this format:
```
DD-MM-YYYY-LP [CEFR]-[topic]-[skill or system]-[Shape]
```
*(Note: Use 4-digit year as per latest user request)*

#### HTML Structure

> [!IMPORTANT]
> **See [REFERENCE.md#html-template](REFERENCE.md#html-template)** for the complete HTML boilerplate.
>
> - **Gold Standard**: `inputs/05-Social-Media-Reading/06-01-26-LP B1-Social-Media-Reading-Shape H.html`
> - Use 1-cell tables for colored boxes (e.g., Differentiation).
> - Use standard HTML tables for lesson stages.
> - Ensure all styles are **inline** (`style="..."`).
> - Use **relative paths** for images: `../../images/...`

#### Color Scheme (ACT Maroon Branding)
- Title: `#A62D26` | Table header: `#A62D26` | Stage rows: `#cb5c55` | Alternating row: `#fceceb`

#### McKinsey Logic Checks (MANDATORY)

Before finalizing:
1. **Horizontal Flow (The Story)**: Can you understand the lesson's narrative path by reading ONLY the stage headers?
2. **Vertical Flow (The Proof)**: Does every activity explicitly support the lesson objective or Stage Aim?

#### Bullet Points (Google Docs Compatible)
- Use proper HTML lists `<ul>` and `<li>` in the Procedure column.
- Apply margin styling: `<ul style="margin: 5pt 0 0 0; padding-left: 20px;">`


**Line Spacing:**
- All text: `line-height: 1.15` (set on body tag)

#### After Generation

1. Save the HTML file to the source folder

2. **🔍 RUN VALIDATOR**: Check lesson plan for compliance
   ```bash
   python skills/writing-lesson-plans/scripts/validate_lesson_plan.py <lesson_plan.html>
   ```
   - **Checks performed**:
     - ❌ Timing sums to total duration
     - ❌ Pre-teach vocabulary (Shape E-H)
     - ❌ Thai scaffolding in vocabulary
     - ⚠️ Answer key present
     - ⚠️ Stage structure
   - **Fix ALL errors** before proceeding

3. **🚦 USER REVIEW GATE**: User reviews via IDE preview
   - Do NOT open the file in a browser automatically.
   - Wait for the user to review the file in their IDE.
   - If user requests changes, edit and go back to step 2.
   - **DO NOT proceed until user approves**


#### Required Additions

> [!IMPORTANT]
> - **Shape E (Receptive Skills)**: MUST include a "Pre-teach Vocabulary" stage immediately after Lead-in
> - **Shape E (Listening)**: Include full transcript at the end
> - **All lessons with exercises**: Include answer keys as footer section

#### Pre-teach Vocabulary Format (Shape E)

Select **5 words** from the source text that would be challenging for learners at the given CEFR level.

**Format for each word:**

```
### [number]. word /phonemic script/: Thai translation
English context sentence with **target word** highlighted.
Thai context sentence with **คำแปล** highlighted.
```

**Complete Example:**

```
### 1. postpone /pəʊstˈpəʊn/: เลื่อน
They decided to **postpone** the meeting until next week.
พวกเขาตัดสินใจ**เลื่อน**การประชุมไปสัปดาห์หน้า

### 2. behavior /bɪˈheɪvjər/: พฤติกรรม
Teachers should always model good **behavior** in the classroom.
ครูควรเป็นแบบอย่างของ**พฤติกรรม**ที่ดีในห้องเรียนเสมอ

### 3. interrupt /ˌɪntəˈrʌpt/: ขัดจังหวะ
It's not polite to **interrupt** people when they're talking.
การ**ขัดจังหวะ**คนอื่นตอนพวกเขากำลังพูดไม่สุภาพ

### 4. appropriate /əˈprəʊpriət/: เหมาะสม
Wearing formal clothes is **appropriate** for a job interview.
การแต่งกายอย่างเป็นทางการ**เหมาะสม**สำหรับการสัมภาษณ์งาน

### 5. acceptable /əkˈseptəbl/: ยอมรับได้
Using your phone during class is not **acceptable**.
การใช้โทรศัพท์ในระหว่างเรียนไม่**ยอมรับได้**
```

### Step 9: Export & Archiving

Once the lesson plan is approved:
1.  **Push to GDocs**: Use the `push_to_gdocs` skill (via ADC) to create the cloud version.
2.  **Save Locally**: Copy the final HTML file to the local Google Drive path based on lesson type:
    - **Intensive**: `G:\My Drive\A CLASSES- ED - TERM 2\INTENSIVE - SHORTCUT FROM HERE`
    - **Regular Bell**: `G:\My Drive\A CLASSES- ED - TERM 2\M24A - M3-3A`
    *(Naming: `DD-MM-YYYY-LP-[CEFR]-[Topic].html`)*

---

## Reference Files

For full lesson shape details and examples, see:
- [REFERENCE.md](REFERENCE.md) - Shape summaries
- [knowledge_base/shapes/](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/knowledge_base/shapes/) - Complete shape definitions (modular files)
  - Shapes A-G: Traditional lesson frameworks
  - Shapes H-J: SCR (Situation-Complication-Resolution) frameworks for Thai middle schoolers

---

## Output Example

See [REFERENCE.md](REFERENCE.md) for a complete lesson plan example.
