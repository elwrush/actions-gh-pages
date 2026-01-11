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

### Step 4: Clarify Materials

If materials are unclear, ask specific questions:
- What is the main topic/context?
- What target language items are covered?
- Are there audio/video components?
- Are there exercises with answer keys?

### Step 5: Special Requests and Notes

Before generating the lesson plan, ask:
> "Do you have any special requests or notes for this lesson? (e.g., include a YouTube video, emphasize particular exercises, specific activities, time constraints, student needs)"

Wait for user response and incorporate their requests into the lesson plan.

### Step 6: Suggest Objective + Marker Sentences

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
> ## Interpretative Pedagogy Principle
> 
> Do NOT slavishly and mechanistically reproduce the structure of worksheets in lesson plan format. Instead:
> - **Frame and Interpret**: Present material as an expert ESL teacher would.
> - **Guidance**: Use analogies, metaphors, similes, and models to guide students on HOW to do tasks properly.
> - **Scaffolding**: Provide conceptual "mental models" rather than just lists of instructions.
> 
> Example:
> - *Mechanistic*: "Step 3: Fill in the worksheet now."
> - *Interpretative*: "Step 3: **Detective Work**. Like detectives searching for clues, scan the text for ONLY the information you need. You don't need to understand every word—just find the answer to solve the case."

### Step 7: Write Lesson Plan (HTML for GDocs)

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

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>[Lesson Title]</title>
</head>
<body style="font-family: Arial, sans-serif; font-size: 11pt; color: #333; line-height: 1.15;">
    
    <!-- Header Image -->
    <p style="text-align: center;">
        <img src="../../images/intensive-header.jpg" width="600" style="margin-bottom: 20pt;">
        <!-- OR: <img src="../../images/bell-header.jpg" width="600"> for regular Bell lessons -->
    </p>
    
    <!-- Lesson Metadata Header (1.15 line spacing) -->
    <div style="line-height: 1.15;">
        <h1 style="font-size: 16pt; color: #A62D26; border-bottom: 3pt solid #A62D26; padding-bottom: 5pt;">[Unit Title]</h1>
        <p><strong>Objective:</strong> [Objective from Step 6]</p>
        <p><strong>Date:</strong> [DD-MM-YY format]</p>
        <p><strong>Systems/Skills:</strong> [From Step 2]</p>
        <p><strong>CEFR Level:</strong> [From Step 2]</p>
        <p><strong>Teacher:</strong> [From Step 2]</p>
        <p><strong>Duration:</strong> [From Step 2]</p>
        <p><strong>Materials:</strong> [Meaningful description of resources, e.g., "Worksheet on comprehending a reading and developing ideas about what it means to be polite in a given culture" OR "Coursebook XYZ, pages 45-48"]</p>
        <p><strong>Assessment:</strong> [From Step 2]</p>
    </div>
    
    <hr style="margin: 20pt 0; border: none; border-top: 1pt solid #ddd;">
    
    <!-- Lesson Stages Table -->
    <h2 style="color: #A62D26; font-size: 14pt; margin-top: 20pt;">Lesson Stages</h2>
    
    <table border="1" style="width: 100%; border-collapse: collapse;">
        <thead>
            <tr style="background-color: #A62D26; color: white;">
                <th style="padding: 8pt; width: 8%;">Stage</th>
                <th style="padding: 8pt; width: 20%;">Aim</th>
                <th style="padding: 8pt; width: 52%;">Procedure</th>
                <th style="padding: 8pt; width: 10%;">Time</th>
                <th style="padding: 8pt; width: 10%;">Interaction</th>
            </tr>
        </thead>
        <tbody>
            <!-- Stage Header Row (colored, spanning all columns) -->
            <tr style="background-color: #cb5c55; color: white;">
                <td colspan="5" style="padding: 8pt; font-weight: bold; text-align: center;">
                    STAGE ONE: [Stage Name from Lesson Shape]
                </td>
            </tr>
            <!-- Individual steps within this stage -->
            <tr>
                <td style="padding: 8pt; text-align: center;">1</td>
                <td style="padding: 8pt;">To [specific aim]</td>
                <td style="padding: 8pt;">
                    <strong>[Activity Name]</strong>
                    <ul style="margin: 5pt 0 0 0; padding-left: 20px;">
                        <li>First step of procedure</li>
                        <li>Second step of procedure</li>
                        <li>Pair check / feedback step</li>
                    </ul>
                </td>
                <td style="padding: 8pt; text-align: center;">5</td>
                <td style="padding: 8pt; text-align: center;">T-Ss</td>
            </tr>
            <!-- Alternating row background -->
            <tr style="background-color: #fceceb;">
                <td style="padding: 8pt; text-align: center;">2</td>
                <td style="padding: 8pt;">To [specific aim]</td>
                <td style="padding: 8pt;">[Use <ul><li> for procedures]</td>
                <td style="padding: 8pt; text-align: center;">5</td>
                <td style="padding: 8pt; text-align: center;">Ss-Ss</td>
            </tr>
            
            <!-- Next Stage Header Row -->
            <tr style="background-color: #cb5c55; color: white;">
                <td colspan="5" style="padding: 8pt; font-weight: bold; text-align: center;">
                    STAGE TWO: [Next Stage Name]
                </td>
            </tr>
            <!-- More rows... -->
        </tbody>
    </table>
    
    <p style="margin-top: 15pt; font-style: italic; color: #7f8c8d;"><strong>Total Time:</strong> [sum of all stage times] minutes</p>
    
    <hr style="margin: 30pt 0; border: none; border-top: 2pt solid #A62D26;">
    
    <!-- Answer Key (if applicable) -->
    <h2 style="color: #A62D26; font-size: 16pt; border-bottom: 2pt solid #A62D26; padding-bottom: 5pt;">Answer Key</h2>
    
    <!-- Transcript (Shape E Listening ONLY) -->
    
</body>
</html>
```

#### Stage Headers Guide

Stage headers must be informed by the lesson shape model. **Colored rows** should span all 5 columns and indicate major stages:

**Shape E (Receptive Skills) example stages:**
- STAGE ONE: Build Interest (Lead-in)
- STAGE TWO: Pre-teach Vocabulary
- STAGE THREE: Reading/Listening for Gist (Global Reading)
- STAGE FOUR: Reading/Listening for Detail (Close Reading)
- STAGE FIVE: Post-reading/listening Discussion

**Important Notes:**
1. Pre-teach Vocabulary appears **in the lesson table**, NOT in the header metadata
2. Each major stage gets a colored header row
3. Within each stage, individual steps are numbered sequentially (1, 2, 3...)

#### Formatting Guidelines

**Color Scheme (ACT Maroon Branding):**
- Title heading: `#A62D26` (maroon)
- Table header: `#A62D26` (maroon)
- Stage header rows: `#cb5c55` (lighter maroon)
- Alternating row background: `#fceceb` (light pink tint)
- Answer Key/dividers: `#A62D26` (maroon)

**Bullet Points (Google Docs Compatible):**
- Use proper HTML lists `<ul>` and `<li>` in the Procedure column
- Do NOT use manual dashes with `<br>` tags
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

3. **🚦 USER REVIEW GATE**: Open in browser for user review
   - If user requests changes, edit and go back to step 2
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

### Step 8: Export via ADC to GDocs

Once the lesson plan is approved, use the **`push_to_gdocs`** tool.
- Ensure the push operation uses the **ADC (Application Default Credentials)** method.
- The tool will automatically embed local images as base64.

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
