---
name: creating-html-presentation
description: Generates vibrant Reveal.js HTML presentations (slideshows) from lesson plans with high-energy visuals, timers, and answer keys.
---

# Skill: Creating HTML Presentations (`creating-html-presentation`)

## Description
This skill generates vibrant, high-energy HTML presentations using **Reveal.js**. It transforms lesson plans into dynamic, web-based experiences with "pop and verve."

## ⛔ MANDATORY CO-LOCATION RULE (READ FIRST)

> [!CRITICAL]
> **ALL presentation files (`index.html`, `images/`, `audio/`) MUST be created inside the SAME folder as the lesson plan and worksheet.**
> 
> **Canonical Location**: `inputs/[QAD-folder]/` (e.g., `inputs/QAD-Fight-or-Flight/`)
> 
> **NEVER create presentations in**:
> - ❌ Project root (e.g., `18-01-26_Fight-or-Flight/`)
> - ❌ `presentations/` folder (this is for deployment links only)
> - ❌ Any folder that doesn't contain the `.typ` lesson plan file
>
> **Why**: This ensures all materials for a lesson are grouped, preventing version drift and deployment bugs.

## Context
Use this skill to create the visual backbone of a lesson. Slides must:
- **Mirror the Lesson Plan**: Alignment with stages and materials is mandatory.
- **High-Energy Stage Segues**: Use clear, high-energy transitions (Phases).
- **Preferred Transition**: Use **`convex`** as the default Reveal.js transition for all presentations.
    - **Requirement**: Every segue slide MUST include a sub-headline (max 15 words) explaining the specific pedagogical goal of the upcoming phase.
- **Interactive Timers (MANDATORY)**: Every timed exercise MUST have a visible, interactive countdown timer.
    - **Physics**: Must remain within the 960x700 artboard (no spill-off).
    - **Logic**: Must include Start/Pause/Reset functionality for teacher control.
- **Speaker View (MANDATORY)**:
    - **Access**: Teachers access notes by pressing **'s'** on the keyboard.
    - **Content**: Every slide MUST contain an `<aside class="notes">` block with "Advice" and "Next Slide" cues.
- **Visual Pivots (Slide Offsets)**: Use strongly differentiated background tints for specific pedagogical moments:
    - **Answer Slides**: Use a Deep Emerald/Teal tint (`#052a10`) to signal the transition to validation/review.
    - **Final Task Slides**: Use a Deep Maroon/Crimson tint (`#2a0a0a`) to signal the "Boss Level" or assessment phase.
- **Visual Impact**: Use high-contrast themes and cinematic visuals.

## 🛑 VISUAL-FIRST WORKFLOW (MANDATORY)

> [!CRITICAL]
> **DO NOT WRITE CODE UNTIL STEP 4**
> You must strictly follow this linear process. Do not skip steps.

### Step 0: ❓ Context Check
**Goal**: Determine the target audience, branding, and file routing.

**GATE 1: Branding**
- **Mode**: "Bell" or "Intensive" (Determines default color palette, but **NO LOGOS** are included).
- **Tone**: 
  - **Bell**: Warm/Standard.
  - **Intensive**: Modern/Edge.

**GATE 2: Audience (MANDATORY - STOP HERE)**
- **Ask**: "Is the audience **Middle School** or **High School**?"
- **⚠️ CRITICAL**: **STOP** and wait for explicit user confirmation. Do NOT assume, do NOT pre-fetch files, and do NOT read ahead to Step 0.5. Wait for the answer.
- **Tone Logic**:
  - **Middle School**: "Pop & Verve"
    - **Language**: High energy, game-based metaphors (Boss Levels, Power Ups, Missions)
    - **Complexity**: More visual scaffolding, shorter explanations
    - **Example Slide Title**: "MISSION 1: Hunt the Hidden Clauses!" ✅
    - **Avoid**: "Analyze the syntactic structure..." ❌
  - **High School**: "Expert/Academic"
    - **Language**: Focus on university pathways, career utility, professional lexicon
    - **Complexity**: Sophisticated analytical hooks, technical terminology
    - **Example Slide Title**: "Task 1: Identify and Classify Relative Clause Types" ✅
    - **Avoid**: "Let's find the clauses, team!" ❌

### Step 0.5: 📂 Source Material Validation (MANDATORY GATE)
**Goal**: Ensure input materials exist before generating slides.
**Action**:
1.  **Check Lesson Plan**: Look for `*.typ`, `*.md`, or `*.pdf` lesson plan.
    -   **IF MISSING**: **STOP**. You cannot generate a presentation without a plan.
2.  **Check Learning Materials**: Look for a worksheet or source text.
    -   **IF MISSING**: Ask: "No worksheet/source text found. Are we proceeding without one? (y/n)"
    -   **Decision**: 
        -   **Yes**: Proceed (User acknowledges 'No Source' mode).
        -   **No**: **STOP** and wait for files.

### Step 1: 🎨 Gated Palette Selection (MANDATORY GATE)
**Goal**: Define the exact color palette from the modular system.

**Action**:
1.  **Consult** `skills/creating-html-presentation/PALETTES.md` to review available themes.
2.  **STOP** and present the menu to the user explicitly.
3.  **Propose** a specific palette (Name + ID) based on the lesson's tone (Step 0).
    -   *Example*: "For a 'High School/Serious' lesson, I recommend Palette #5 (Blue Grey Steel)."
4.  **Wait** for the user to confirm the Palette ID (e.g., "Use #5").

**MANDATORY RULES (The Fixed Canvas):**
-   **Segue Slides**: Must ALWAYS use a **vibrant dark radial gradient** and a **neon glow** on the title.
    -   *Background Code*: `var(--grad-segue)`
    -   *Title Glow*: `text-shadow: 0 0 20px var(--text-accent), 0 0 40px var(--primary), 6px 6px 0px rgba(0,0,0,0.5);`
-   **Warning/Constraint Slides**: Must use the **Boss Level gradient** (`var(--grad-boss)`) and include a visual hazard icon (e.g., road sign).
    -   *Purpose*: Signals a negative grammar rule (e.g., "When NOT to use this").
    
### Step 1.5: 📦 Asset Strategy & Sourcing (MANDATORY GATE)
**Goal**: Define and source the exact media assets needed.

**GATE: Media Strategy Check**
You MUST ask:
> "Do you want images, sound, or video in this presentation? Choose:
> 1. Images
> 2. Sounds
> 3. Videos
> 4. All"

**Sourcing Logic (Strict):**
-   **A. Images**:
    1.  Ask: "Photos, Illustrations, or Vectors?"
    2.  **Constraint**: Illustrations/Vectors **MUST** be transparent PNGs.
    3.  **Source**: **Pixabay First** (`searching-pixabay`).
    4.  **Attribution (MANDATORY)**:
        -   **Format**: "Image by [User] from Pixabay"
        -   **Placement**: Static, centered, directly BENEATH the image (inside the column).
        -   **Code**: `.attribution { position: static; text-align: center; font-size: 12px; margin-top: 8px; }`
    5.  **Fallback**: Internal Generation -> External Gemini API.
-   **B. Sounds**:
    1.  **Source**: **Freesound ONLY** (`searching-freesound`). **NO VOCABULARY AUDIO** (user explicitly removed requirement).
    2.  **Process**: Present 3 candidates (for UI/Timer) -> Wait for Approval -> Download.
    3.  **Optimization (MANDATORY)**: You MUST convert all `.wav` files to `.mp3` using `ffmpeg` to reduce file size.
        -   *Command*: `ffmpeg -i input.wav -codec:a libmp3lame -qscale:a 2 output.mp3`
        -   **Action**: Delete the original `.wav` after successful conversion.
-   **C. Videos**:
    1.  Ask: "YouTube or Pixabay?"
    2.  **Source**: Pixabay (Download) or YouTube (Embed). **NO GENERATION**.

**Output**: A list of approved assets to use in Step 2.

---

### Step 1.6: 🔊 Audio Setup (MANDATORY - AUTOMATIC)
**Goal**: Copy standard timer audio files to the presentation folder.

**CRITICAL**: **EVERY** presentation uses timers and requires these 3 audio files. This step is **NOT OPTIONAL**.

**Action (Auto-run)**:
```bash
Copy-Item "audio/blip.mp3" "inputs/[presentation-folder]/audio/blip.mp3"
Copy-Item "audio/30-seconds.mp3" "inputs/[presentation-folder]/audio/30-seconds.mp3"  
Copy-Item "inputs/18-Jan-Reading/audio/bell.mp3" "inputs/[presentation-folder]/audio/bell.mp3"
```

**Verification**:
- ✅ Confirm all 3 files exist in `inputs/[presentation-folder]/audio/`
- ✅ File sizes > 0

**Why This Matters**: Timer sounds break EVERY TIME if this step is skipped. This is now a mandatory pre-flight check.

---

### Step 2: 📝 The Visual Plan (Markdown)
**Goal**: Map every single slide, **INCLUDING ANSWER KEYS**.
- **Action**: Cross-reference every Task slide with the Source File. If content is missing, **STOP**.
- **Constraint**: You MUST interleave answer keys immediately after tasks.
- **Format**:
  ```markdown
  ## Slide 1: Title
  - **Visual**: Hero image...
  ```

### Step 3: 🚦 User Approval Gate
**STOP**. Present the Visual Plan (Markdown) to the user.
- **Ask**: "Does this visual structure match the [Theme Name] vision?"
- **Do not proceed** to wireframing until the user says "Yes."

### Step 4: 🛠️ Visual Plan Review (Artifact Gate)
**Goal**: Allow the user to review the full plan via an artifact BEFORE coding.
**Action**:
1.  Generate a file named `visual-plan.md` (if not already done in Step 2).
2.  Update it with **FINALIZED** asset paths (e.g., `images/ship.jpg`).
3.  **STOP AND WAIT**. Explicitly ask the user to review the artifact.
4.  **Do not proceed** to `index.html` until you get "Approved".

### Step 4.5: 📊 Batch Building Assessment (MANDATORY)
**Goal**: Determine if the presentation needs to be built in batches to avoid token limits.

**CRITICAL RULE**: Count the total number of slides in `visual-plan.md`.
- **IF ≤ 30 slides**: Build in ONE file using `write_to_file`.
- **IF > 30 slides**: Build in BATCHES using `replace_file_content`.
  - **Batch 1**: Base HTML structure + Slides 1-20
  - **Batch 2**: Slides 21-40
  - **Batch 3**: Slides 41-60 (if needed)
  - etc.

**Why This Matters**: Large presentations (>40 slides) exceed the 16K token generation limit. You MUST use incremental edits for presentations with many slides.

### Step 5: 🛠️ Implementation (The Gold Standard)
Now, write the `index.html`.

**📚 REQUIRED READING**:
1.  **First**: Review `COMPONENTS.md` for all available CSS classes and Web Components.
2.  **When unsure**: Consult `DECISION_TREE.md` for "which component to use when" logic.
3.  **For Reveal.js features**: Check `docs/reveal-layout.md` and `docs/reveal-backgrounds.md`.

**Pre-Flight Checklist**:
- ✅ **CRITICAL**: Use CDN links for Reveal.js: `https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css` (NOT `../../js/reveal.js/dist/reveal.css`)
- ✅ Check `images/` folder for real file extensions (`.jpg`, `.png`, `.svg`)
- ✅ Verify `audio/` folder exists with `blip.mp3`, `30-seconds.mp3`, `bell.mp3`
- ✅ Confirm lesson plan specifies timer durations for tasks

**CSS LOCKDOWN**:
- 🛑 **NO INLINE STYLES** for `font-size` or `color` on high-contrast slides (use CSS classes from `COMPONENTS.md` or scoped CSS).
- ✅ **CONTRAST RULE**: Yellow/White backgrounds (Level Selection, Task Subtitles) **MUST** use black text (`color: black !important`) for readability.
- ✅ **IMAGE CLASS**: All <img> tags must use either `.inset-media` or `.constrained-media` to prevent layout explosions.
- ✅ **USE DOCUMENTED CLASSES**: `.glass-box`, `.inset-media`, `.slide-table`, `<timer-pill>`
- ✅ **COPY BOILERPLATE** from `REFERENCE_TEMPLATE.html`
- 🛑 **DO NOT** invent custom classes (use `COMPONENTS.md` library)

**Theme Adaptation**:
- Modify `:root` CSS variables (`--maroon`, `--cyan`, `--navy`) to match **Approved Theme** (Step 1)
- Do NOT break layout classes (`.row-container`, `.col-*`)

### Step 5.3: Pedagogical Compliance
**Goal**: Ensure students can use the vocabulary in practice.
**Rules**:
1.  **Vocabulary Context (MANDATORY)**: Every vocabulary slide MUST include a contextualizing sentence in English.
    *   *Correct*: "If you face a dangerous situation, your **instinct** tells you to run."
    *   *Incorrect*: "Instinct: A natural behavior."

3.  **One Answer, One Slide (MANDATORY)**: Never put multiple answers on a single slide. Each answer must have its own slide containing:
    *   **Title Format**: "Answer: Question N" (e.g. "Answer: Question 1").
    *   **Snippet/Para**: Use the format "Para N" for the source reference (e.g. "Para 4").
    *   A brief snippet from the source text and a clear **Explanation Box** ("Why is this the answer?").
    *   **Goal**: Ensure students digest the logic, not just the correct word.

### Step 5.4: 🧱 The "Split-Anchor" Visual Standard
**Goal**: Integrate images without cluttering explanations.
**Rule**: Use the **40/60 Split Layout** for content slides with images.
-   **Left Column (40%)**: The **Visual Anchor** (Image).
    -   *Class*: `.col-40` containing `<img>` and `.attribution`.
-   **Right Column (60%)**: The **Instructional Content**.
    -   *Class*: `.col-60` containing `.glass-box`.
**Why**: This prevents "wallpaper" images. The image becomes a distinct pedagogical tool.

### Step 5.5: 🧪 Technical Validation (MANDATORY)
**Action**: You MUST run the technical validator before proceeding.
1.  **First**: Run with `--help` to understand usage:
    ```bash
    python skills/creating-html-presentation/scripts/validate_presentation.py --help
    ```
2.  **Then**: Execute the validator:
    ```bash
    python skills/creating-html-presentation/scripts/validate_presentation.py [path/to/index.html] --mode [bell|intensive]
    ```
- **Rule**: If the script fails, you **MUST** fix the issues and re-run it until it passes.
- **Why**: This script catches broken links, incorrect CSS usage, and missing components.

### Step 5.6: 🎓 Pedagogical Validation (MANDATORY)
**Action**: You MUST run the pedagogical validator to ensure content fidelity.
1.  **Execute**:
    ```bash
    python skills/creating-html-presentation/scripts/validate_pedagogical.py [path/to/index.html]
    ```
    - The script auto-detects `visual-plan.md` and source materials in the same directory.
2.  **What it checks**:
    - ✅ Slide count matches `visual-plan.md`
    - ✅ Answer slides follow task slides (interleaving)
    - ✅ Each task has correct number of answer slides
    - ✅ Task numbering is sequential and consistent
    - ✅ Content matches source materials (no hallucination)

- **Rule**: If the script fails, you **MUST** fix the pedagogical issues and re-run.
- **Why**: This prevents content hallucination and ensures strict adherence to the approved plan.
- **Critical**: This is the **enforcement mechanism** that prevents the errors you just experienced.

### Step 5.7: 🛑 Slide Approval Gate (MANDATORY)
**Goal**: Ensure the user is satisfied with the visual and audio quality before making it live.
**Action**:
1.  Provide the path to the `index.html` and a summary of the media assets.
2.  **STOP**. You MUST get explicit approval (e.g., "Approved" or "Go for deployment") from the user.
3.  **DO NOT** push to Git or generate Google Doc links until this gate is cleared.

### Step 6: 🚀 Deployment & Organization

> [!CAUTION]
> **STORAGE RULE**: Always keep the `index.html` and its `audio/images` folders in the **SAME FOLDER** as the worksheet (`*.typ`) and lesson plan. 
> This ensures that all materials for a specific lesson are grouped together in the `inputs/` directory.

1.  **Organize**: Ensure the presentation files (`index.html`, `audio/`, `images/`) are inside the specific lesson folder (e.g., `inputs/QAD-Fight-or-Flight/`).
2.  **Deployment (Optional)**: If a web-live version is needed:
    - Add an entry to `presentations/index.html` (library card).
    - Git Add / Commit / Push to trigger Cloudflare build.

## Pedagogical & Thematic Standards (STRICT)

### 1. The Expert ESL Teacher Voice
- **Rule**: Every slide must have a clear *student action* or *takeaway*.
- **Tone Adaptation (Based on Gate 2 Decision)**:
    - **Middle School**: Use "Hook & Play" language. Tasks are "Missions" or "Quests".
    - **High School**: Use "Utility & Achievement" language. Tasks are "Case Studies" or "Strategic Analysis".
- **Tone**: **Warm & Authoritative**. (Never infantilizing, even for Middle School).
- **Scaffolding**: You MUST use the `<div class="teacher-tip">` box for **pedagogical hints only** (e.g., "Check understanding," "Monitor pronunciation").
- **CRITICAL**: **NEVER** put procedural instructions (e.g., "Give students 5 minutes to review") in teacher-tip boxes. These belong in `<aside class="notes">` only.

**Tone Comparison Table**:
| Context | Middle School (Pop & Verve) | High School (Expert/Academic) |
|:--------|:----------------------------|:------------------------------|
| **Slide Title** | "BOSS LEVEL: Final Writing Mission!" | "Task 4: Written Case Study" |
| **Instructions** | "Hunt down the relative clauses and mark them!" | "Identify and classify relative clause types." |
| **Explanation** | "This word connects two ideas like a bridge!" | "Relative pronouns establish syntactic relationships between clauses." |
| **Motivation** | "Unlock the next grammar power-up!" | "This skill is essential for IELTS Writing Task 2." |
| **Feedback** | "You crushed it! 🎯" | "Excellent application of the target structure." |

### 2. Theming: Flexible Identity
- **Rule**: The visuals must strictly follow the **Approved Theme** (Step 1).
- **No Freestyling**: Do not mix aesthetics.

### 3. Source Material Sync (DETERMINISTIC)
- **Rule**: Slides cannot be divorced from source materials.
- **Naming**: If the Worksheet says "Task 2", the Slide must say "TASK 2".
- **Validation**: If the Lesson Plan does not explicitly list the questions/answers, you **MUST STOP** and ask the user for the source text. **NEVER invent/hallucinate questions or answers**.
- **Quote-Based**: You must be able to point to the exact line in the source file for every activity.

### 4. The Per-Question Answer Key Standard (STRICT GOLDEN RULE)
- **Separate Slides**: NEVER present all answers on a single slide.
- **Rule**: Create a distinct slide for **EACH** question's answer (e.g., Answer 1, Answer 2, Answer 3).
- **Format**:
    - **Header**: "Task X: Question Y"
    - **Body**: The full sentence/answer with the key part highlighted.
    - **Explanation (MANDATORY)**: A short "Why?" or explanation box below the answer is REQUIRED for every single answer slide. No exceptions.
- **Interleaving**: These slides must appear sequentially after the Task slide.
- **Explanation Quality (STRICT)**:
    - ❌ **Forbidden**: Single technical words (e.g., "Recurrence", "Collocation", "Adjective").
    - ✅ **Required**: Simple, student-friendly sentences (e.g., "We do this every day, so it is a daily habit.", "Clients are for professional services like lawyers.").

### 5. Direct Vocabulary Instruction (The Legacy Standard)
- **One Word Per Slide**.
- **MANDATORY Image**.
- **Header**: Word + /phonemics/ + **Thai Definition**.
- **NO AUDIO**: Audio players/listen badges are no longer used for vocabulary slides.

### 6. Pronunciation Drills (Sentences)
- **Rule**: Use **COMPLETE SENTENCES** from the source text. No isolated phrases.
- **MANDATORY**: Consult `REFERENCE.md` for phonological accuracy.
- **Markup**:
    - **Stress**: CAPITALIZE stressed syllables (e.g., "imPORtant").
    - **Linking**: Use `‿` symbol (e.g., "where‿I").
    - **Intonation**: Use arrows `↘` `↗` for tone changes.
- **Example**: "The TOWN **where‿I** LIVED‿as‿a TEENager ↘ is FAmous..."

### 7. Speaker Notes Standard (MANDATORY)
- **Code**: Every slide MUST have an `<aside class="notes">` block.
- **Access**: Remind the user/teacher: "Press 's' to view Speaker Notes."
- **Content**:
    1.  **Advice**: Delivery tips for the teacher (e.g., "Check understanding," "Elicit answers").
    2.  **Next**: A preview of the next slide to facilitate smooth transitions.
- **Example**:
    ```html
    <aside class="notes">
        **Advice**: Monitor student pronunciation of 'intricate'.
        **Next**: Task 2 Instructions.
    </aside>
    ```



## Technical Standards (The Fixed Canvas)

### 📐 Resolution & Scaling
- **960x700 ONLY**. This is the artboard. All internal math assumes this footprint.
- **Font Sizes (MANDATORY)**: 
    - **H1 (Titles/Segues)**: `80pt` (approx. `2.5em`). Use `r-fit-text` ONLY if text is long.
    - **H2 (Slide Headings)**: `45pt` (approx. `1.5em`).
    - **H3 (Sub-titles)**: `35pt` (approx. `1.2em`).
    - **Normal Body**: `30pt` (approx. `1.0em`).
    - **Small Body**: `24pt`.
    - **Teacher Tips**: `18pt`.

### 🎨 Design Philosophy: "Vibrant Depth"
- **NO IMAGE BACKERS**: Do not use photos as backgrounds.
- **THE RADIAL BACKER**: Every slide must have a multi-layered CSS background driven by variables.
    - **Main Gradient**: `var(--grad-main)` (e.g., `radial-gradient(circle, var(--bg-dark) 0%, #100630 100%)`)
    - **Segue Gradient**: `var(--grad-segue)` (Fixed high-contrast dark: `radial-gradient(circle, #2d3436 0%, #000000 100%)`)
- **GLOWING SEGUES**: Segue titles must use a multi-layered text shadow to create a "neon" effect.
- **IMAGES AS INSETS**: Images must be focal points, wrapped in a frame (border + shadow).

### 🧱 Layout Classes (Use These EXACTLY)
- `.slide-canvas`: The main wrapper.
- `.row-container`: `width: 900px`, `gap: 40px`.
- `.col-40`, `.col-50`, `.col-60`: Fixed width columns.
- `.glass-box`: The standard container for text/input.
- `.inset-media`: Standard wrapper for images (adds border, shadow, and `max-height: 400px`).

### 🕒 Interactive Timers (The "Pace" Standard)
- **Timer Component**: Use the standard `.timer-pill` layout.
- **Visibility**: Always place in the bottom-center or a clearly visible `.glass-box`.
- **Logic**: Use the `reveal-timer.js` pattern (Start/Pause functionality).
- **Duration**: Match the Lesson Plan (Default: 4 or 6 minutes).
- **Audio Behavior (MANDATORY)**:
  - **Blip on Start**: Plays when START button is pressed
  - **Final 29 Seconds**: Blip plays every second from 29 down to 1 (not during longer periods)
  - **30-Second Warning**: Warning sound plays at exactly 30 seconds remaining
  - **Bell on Finish**: Bell sound plays when timer reaches 0
- **Audio Files Required**: `blip.mp3`, `30-seconds.mp3`, `bell.mp3` (auto-copied in Step 1.6)

### 🧱 Split Layout Rule (GLOBAL STANDARD)
**CRITICAL**: **Whenever a slide has a `timer-pill`, it MUST use a Split Layout.**

**Structure**:
```html
<div class="row-container">
    <div class="col-50">
        <img src="images/[relevant-image].png" class="inset-media">
    </div>
    <div class="col-50">
        <div class="glass-box" style="text-align: left;">
            <h2>Task Title</h2>
            <p class="text-xl">Instructions...</p>
            <timer-pill duration="5"></timer-pill>
        </div>
    </div>
</div>
```

**Why This Matters**:
- Timers "stranded" at the bottom look unbalanced and amateur.
- Split layouts create visual weight balance.
- The image provides context and makes the slide feel premium.

**Image Selection**:
- **Task 1 (People/Matching)**: Business meeting or team photo.
- **Task 2 (Synonyms/Vocabulary)**: Contract signing or document.
- **Task 3 (Multiple Choice)**: Global/Professional imagery.
- **Task 4 (Transformation)**: Abstract/Conceptual imagery.


---

### 🎬 Auto-Animate for Grammar Lessons (GOLD STANDARD)

**When to Use AUTO-ANIMATE**:
✅ **USE** when:
- Showing **sentence transformations** (e.g., rewrites using synonyms, paraphrasing)
- Demonstrating **grammar changes** (tense, voice, clause reduction)
- Revealing **before/after** comparisons where words change position or disappear
- The visual plan explicitly says "Auto-Animate"

❌ **DO NOT USE** when:
- Just revealing an answer (use standard answer slides instead)
- Showing static vocabulary definitions
- Displaying multiple-choice questions
- The transformation is conceptual, not textual (e.g., explaining a process)

**How It Works**:
1. Add `data-auto-animate` to two consecutive `<section>` elements
2. Use `data-id="unique-id"` on elements you want to morph
3. Reveal.js automatically animates the transformation

**Manual Implementation**:
```html
<!-- Before -->
<section data-auto-animate 
         data-auto-animate-duration="1.5" 
         data-auto-animate-easing="ease-in-out"
         data-background-color="var(--bg-dark)">
    <h2>Sentence Reduction</h2>
    <p data-id="sentence" style="font-size: 36px;">
        Michelangelo, <span data-id="remove" style="color: #ef4444; text-decoration: underline;">who was</span> a brilliant sculptor, carved...
    </p>
    <p style="font-size: 24px; color: #ef4444;">⬇ Watch the underlined words disappear ⬇</p>
</section>

<!-- After -->
<section data-auto-animate 
         data-auto-animate-duration="1.5" 
         data-auto-animate-easing="ease-in-out"
         data-background-color="var(--bg-dark)">
    <h2>Sentence Reduction</h2>
    <p data-id="sentence" style="font-size: 36px; color: var(--text-accent);">
        Michelangelo, a brilliant sculptor, carved...
    </p>
    <p style="font-size: 32px; color: var(--text-accent);">✓ We removed: <strong>who was</strong></p>
</section>
```

**CRITICAL Settings**:
- `data-auto-animate-duration="1.5"`: Animation takes 1.5 seconds (default is too fast at 0.4s)
- `data-auto-animate-easing="ease-in-out"`: Smooth acceleration/deceleration
- `data-id="sentence"`: Matches elements between slides for morphing
- Visual cue: "⬇ Watch the underlined words disappear ⬇" prepares students

**Reusable Component** (Recommended):
```html
<grammar-transform 
    title="From Relative Clause to Appositive"
    before="Michelangelo, who was a brilliant sculptor, carved the statue of David."
    after="Michelangelo, a brilliant sculptor, carved the statue of David."
    highlight="who was">
</grammar-transform>
```

**Use Cases**:
- ✅ **Appositives** (reducing relative clauses)
- ✅ **Tense Changes** (present → past)
- ✅ **Active → Passive Voice**
- ✅ **Word Order** (questions, inversions)
- ✅ **Adding/Removing Clauses**

**Why This Matters**: Visual morphing makes grammar transformations **dramatically clearer** than static before/after comparisons.
