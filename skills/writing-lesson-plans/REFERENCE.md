# Lesson Shapes Reference

Quick reference for the 7 lesson shapes. Full details in [lesson_shapes.yaml](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/knowledge_base/lesson_shapes.yaml).

## Shape Summaries

| Shape | Name | When to Use | Typical Stages |
|-------|------|-------------|----------------|
| **A** | Text-based Presentation | Introducing language via reading/listening text | Lead-in → Clarify TL → Controlled Practice → Freer Practice |
| **B** | Language Practice | Follow-up to A or C; more practice needed | Lead-in → Controlled → Semi-controlled → Freer Practice |
| **C** | Test-Teach-Test (TTT) | Testing prior knowledge before teaching | Lead-in → Test 1 → Test 2 → Teach → Practice |
| **D** | Situational Presentation (PPP) | Teaching new language in context | Lead-in → Present (MPF) → Practice → Produce |
| **E** | Receptive Skills | Reading/Listening focus | Lead-in → Pre-teach Vocab → Pre-task → Main Task → Post-task |
| **F** | Productive Skills | Speaking/Writing focus | Lead-in → Preparation → Task → Feedback |
| **G** | Task-Based Learning (TBL) | Communication-first approach | Pre-task → Task Cycle → Planning → Report → Analysis |
| **H** | SCR Receptive Skills | Narrative-driven Reading/Listening | Situation → Complication (Conflict) → Resolution (Insight) |
| **I** | SCR Systems | Narrative-driven Grammar/Vocab | Situation (Awareness) → Complication (Challenge) → Resolution (Mastery) |
| **J** | SCR Productive Skills | Narrative-driven Speaking/Writing | Situation (Position) → Complication (Counter-view) → Resolution (Synthesis) |

## Interaction Patterns

| Code | Meaning |
|------|---------|
| T-Ss | Teacher to Students (whole class) |
| Ss-Ss | Student to Student (pairs/groups) |
| S | Solo work |

## Objective Templates

**Systems (Grammar/Vocabulary):**
> By the end of the lesson, learners will be better able to use [target language] in the context of [topic].

**Skills (Reading/Listening):**
> By the end of the lesson, learners will have practiced the sub-skills of [gist/detail/inference] in the context of [text type about topic].

**Skills (Speaking/Writing):**
> By the end of the lesson, learners will be better able to [communicate/write] about [topic] using [language features].

---

## Example Lesson Plan Output

**Life Elementary – Unit 10B – How well can you remember**

**Aim**: By the end of the lesson, learners will have had practice using the present perfect and past simple in the context of life experiences.
**Systems**: Grammar
**Page Numbers**: SB: 167
**Assessment**: n/a

### Lead-in

| Stage | Aim | Procedure | Time | Interaction |
|-------|-----|-----------|------|-------------|
| 1 | To engage Ss and activate schemata | Mini WB quiz about Nelson Dellis. 1 mini WB per student. Ss negotiate answers in teams. Award points. | 3 | T-Ss |

### Clarifying Target Language

| Stage | Aim | Procedure | Time | Interaction |
|-------|-----|-----------|------|-------------|
| 2 | To clarify meaning, form, pronunciation of TL | **Meaning**: Guided discovery with marker sentences on PP. Pairs answer CCQs. 1 min. Feedback. **Form**: New pairs discuss form. 1 min. Feedback. **Pron**: Model and drill chorally/individually. Pairs work on stress and connected speech. | 5 | Ss-Ss |

### Controlled Practice

| Stage | Aim | Procedure | Time | Interaction |
|-------|-----|-----------|------|-------------|
| 3 | To provide controlled practice | Page 167, Exercise 2. Ss choose correct option. 5 min. Swap and check scores. | 8 | T-Ss |

### Freer Practice

| Stage | Aim | Procedure | Time | Interaction |
|-------|-----|-----------|------|-------------|
| 4 | To provide freer practice | Liar! Liar! game. A makes present perfect questions. B answers "yes, I have". A asks follow-up past simple questions to detect lies. 5 questions each, then swap. 8 min. Content feedback → error correction. | 10 | Ss-Ss |

---

### Answer Key (Footer)

**Exercise 2 (p.167)**: 1. have visited, 2. went, 3. has lived, 4. moved, 5. have never been

---

## HTML Template <a name="html-template"></a>

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
    
    <!-- Lesson Metadata Header -->
    <div style="line-height: 1.15;">
        <h1 style="font-size: 16pt; color: #A62D26; border-bottom: 3pt solid #A62D26; padding-bottom: 5pt;">[Unit Title]</h1>
        <p><strong>Objective:</strong> [Objective]</p>
        <p><strong>Date:</strong> [DD-MM-YYYY]</p>
        <p><strong>Systems/Skills:</strong> [Systems/Skills]</p>
        <p><strong>CEFR Level:</strong> [Level]</p>
        <p><strong>Teacher:</strong> Ed Rush</p>
        <p><strong>Duration:</strong> [Duration] min</p>
        <p><strong>Materials:</strong> [Description]</p>
        <p><strong>Assessment:</strong> [Type]</p>
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
            <tr style="background-color: #cb5c55; color: white;">
                <td colspan="5" style="padding: 8pt; font-weight: bold; text-align: center;">
                    STAGE ONE: [Lead-in]
                </td>
            </tr>
            <tr>
                <td style="padding: 8pt; text-align: center;">1</td>
                <td style="padding: 8pt;">To engage Ss</td>
                <td style="padding: 8pt;">
                    <strong>[Title]</strong>
                    <ul style="margin: 5pt 0 0 0; padding-left: 20px;">
                        <li>Step...</li>
                    </ul>
                </td>
                <td style="padding: 8pt; text-align: center;">5</td>
                <td style="padding: 8pt; text-align: center;">T-Ss</td>
            </tr>
        </tbody>
    </table>
    
    <p style="margin-top: 15pt; font-style: italic; color: #7f8c8d;"><strong>Total Time:</strong> [Total] minutes</p>
    
    <!-- Answer Key Section -->
    <hr style="margin: 30pt 0; border: none; border-top: 2pt solid #A62D26;">
    <h2 style="color: #A62D26; font-size: 16pt; border-bottom: 2pt solid #A62D26; padding-bottom: 5pt;">Answer Key</h2>
    
</body>
</html>
```
