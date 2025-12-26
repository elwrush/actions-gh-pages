# Agent Skills System: A Guide for AI Agents

**Audience:** AI Agents / LLMs
**Purpose:** To define the architecture, usage, and best practices for the "Skills" methodology.

## 1. Overview: What are Skills?

Skills are modular capabilities that extend an AI agent's functionality. They are **filesystem-based resources**—packaged instructions, metadata, scripts, and templates—that provide domain-specific expertise.

Unlike one-off prompts, Skills are persistent, reusable, and structured to transform a general-purpose agent into a specialist.

### Key Concepts
- **Modular:** Each Skill is a self-contained unit.
- **Filesystem-Based:** Skills exist as directories and files which the agent navigates using bash commands.
- **Progressive Disclosure:** An agent loads only the necessary information (instructions, reference files) when needed, rather than consuming context window with everything at once.

## 2. The Skills Architecture

Skills operate within a code execution environment where the agent has:
- Filesystem access
- Bash command capabilities
- Code execution capabilities

You should think of a Skill as a directory on a virtual machine. You interact with it using standard bash commands (`ls`, `cat`, `python`, etc.).

### Content Types & Loading Levels

This architecture ensures efficiency by loading content only when it is relevant.

| Level | Content Type | Loaded When | Token Cost | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Level 1** | **Metadata** | **Startup** | Low (~100 tokens/skill) | The `name` and `description` from the Skill's YAML frontmatter. This is always in your system prompt so you know the Skill exists. |
| **Level 2** | **Instructions** | **Triggered** | Medium (< 5k tokens) | The main `SKILL.md` file. You read this file via bash when a user request matches the Skill's description. |
| **Level 3** | **Resources** | **As Needed** | Zero (until read) | Additional files like `FORMS.md` or `REFERENCE.md`. You only read these if the task specifically requires them. |
| **Level 3** | **Code** | **Executed** | Zero (until run) | Utility scripts (e.g., `fill_form.py`). You run these via bash. **The code itself does not enter your context; only the output does.** |

## 3. Workflow: How to Use a Skill

When you receive a user request, follow this decision loop:

1.  **Check Metadata:** Does the user's request match the description of any known Skill in your system prompt?
2.  **Trigger Skill:** If yes, use `bash` to read the main instruction file:
    ```bash
    cat skills/pdf-skill/SKILL.md
    ```
    *This brings the procedural knowledge and workflows into your context.*
3.  **Assess Requirements:** Read the instructions.
    *   Do you need more specific guidance (e.g., for form filling)? -> Read `cat skills/pdf-skill/FORMS.md`.
    *   Do you need to perform an action? -> Execute the relevant script using `python`.
4.  **Execute:** improved Perform the task using the loaded instructions and scripts.

### Example: PDF Processing Workflow

1.  **User Request:** "Extract text from this PDF."
2.  **Trigger:** You recognize the "PDF Processing" skill and run: `cat pdf-skill/SKILL.md`.
3.  **Read Instructions:** The `SKILL.md` tells you to use `pdfplumber`.
4.  **Execute Code:** You write or run the script as instructed:
    ```python
    import pdfplumber
    with pdfplumber.open("document.pdf") as pdf:
        print(pdf.pages[0].extract_text())
    ```
5.  **Refine:** If the user asked to fill a form, you would have also read `FORMS.md` and then run `python pdf-skill/scripts/fill_form.py`.

## 4. Structure of a Skill

A typical Skill directory looks like this:

```text
pdf-skill/
├── SKILL.md           # [Level 2] Main entry point. Contains workflows & best practices.
├── FORMS.md           # [Level 3] Specialized guide (e.g., for form filling).
├── REFERENCE.md       # [Level 3] API references, schemas, data tables.
└── scripts/           # [Level 3] Executable tools.
    └── fill_form.py   # Utility script.
```

## 5. Deployment & Constraints

Be aware of the environment you are running in.

-   **Claude.ai:**
    -   Skills are user-specific (not org-wide).
    -   Network access varies (check settings).
-   **Claude API:**
    -   **No Network Access:** You cannot make external API calls.
    -   **No Runtime Installation:** You cannot `pip install` new packages. You must rely on pre-installed packages or the provided utility scripts.
-   **Claude Code:**
    -   Full network access.
    -   Can install packages locally (do not install globally).

## 6. Security & Best Practices

-   **Trusted Sources Only:** Only use Skills from sources you trust. Malicious skills can execute harmful code.
-   **Data Privacy:** Be careful with skills that handle sensitive data, especially if they have potential network access.
-   **No "Magic":** Do not hallucinate capabilities. Rely strictly on the tools and scripts provided within the Skill directory.
-   **Progressive Disclosure:** Do not read every file in a Skill directory immediately. Only read what is necessary for the current step of the task.

## 7. Authoring Best Practices

When creating your own Skills (or asking an agent to create them):
-   **Deterministic Code:** Prefer providing a python script (`validate_data.py`) over identifying errors purely via LLM reasoning. It is faster, cheaper, and more reliable.
-   **Clear Metadata:** The `description` in YAML frontmatter is critical. It determines *when* the Skill is triggered.
- **Separation of Concerns:** Keep `SKILL.md` concise. Move heavy reference material to `REFERENCE.md` or `EXAMPLES.md` to save context tokens.

---

# Skill Authoring Best Practices

This section details how to write effective Skills that Claude can discover and use successfully. Good Skills are concise, well-structured, and tested.

## 1. Core Principles

### Concise is Key
The context window is a shared resource. Be efficient.
-   **Bad:** Explaining what a PDF is before extracting text.
-   **Good:** "Use `pdfplumber` to extract text." (Assumes Claude knows libraries).

### Degrees of Freedom
Match specificity to the task's fragility.
-   **High Freedom (Text):** "Review this code for bugs." (Context-dependent).
-   **Medium Freedom (Template):** "Generate a report using this specific python function signature."
-   **Low Freedom (Script):** "Run `migrate.py --verify`. Do not modify flags." (Safety-critical).

### Test Across Models
-   **Haiku:** Needs more explicit guidance.
-   **Opus:** Needs less explanation; avoids over-explaining.

## 2. Skill Structure & Naming

### Naming Conventions
Use **gerund form** (verb + -ing) for directory names/IDs.
-   `processing-pdfs`, `analyzing-spreadsheets`
-   **Avoid:** `utils`, `helper`, `files`.

### Effective Descriptions
The `description` in `SKILL.md` frontmatter is **critical** for discovery.
-   **Write in third person:** "atrop" -> "Extracts text from..."
-   **Be specific:** "Extract text and tables from PDF files." vs "Helps with docs."
-   **Include triggers:** "Use when the user mentions PDFs, forms, or document extraction."

## 3. Progressive Disclosure Patterns

Keep `SKILL.md` under 500 lines. Use these patterns to split content:

### Pattern 1: High-Level Guide
`SKILL.md` acts as a menu.
```markdown
# PDF Processing
## Advanced features
**Form filling**: See [FORMS.md](FORMS.md)
**API reference**: See [REFERENCE.md](REFERENCE.md)
```

### Pattern 2: Domain-Specific
Organize by domain to avoid finding irrelevant schemas.
```text
bigquery-skill/
├── reference/
│   ├── finance.md
│   ├── sales.md
```

### Pattern 3: Conditional Details
"For tracked changes, see `REDLINING.md`. Otherwise, edit XML directly."

**Visual Overview:**
A basic skill is just `SKILL.md`. A complex skill is a directory with scripts, references, and examples.

## 4. Workflows & Feedback Loops

### Checklists for Complex Tasks
For multi-step processes, provide a checklist Claude can copy and tick off.
```markdown
- [ ] Step 1: Analyze form (run analyze_form.py)
- [ ] Step 2: Create mapping
...
```

### Feedback Loops
**Validators are crucial.**
1.  Draft content / Edit file.
2.  **Run Validator immediately.**
3.  If fail -> Fix -> Retry.
4.  Only proceed when validation passes.

## 5. Coding Best Practices for Skills

### Solve, Don't Punt
Handle errors in your scripts. Don't just crash and make Claude figure it out.
-   *Good:* Catch `FileNotFoundError` and create a default file or print a helpful message.

### Provide Utility Scripts
Pre-made scripts (`analyze_form.py`) are better than asking Claude to write code on the fly because they are:
-   Reliable (tested).
-   Token-efficient (code is not in context).
-   Consistent.

### Verifiable Intermediate Outputs
For complex changes (e.g., "update 50 fields"):
1.  Run analysis.
2.  Generate a **plan file** (`changes.json`).
3.  **Validate** the plan with a script.
4.  Execute.

### Environment Awareness
-   **Paths:** Always use forward slashes (`scripts/run.py`), even on Windows.
-   **Dependencies:** Don't assume packages are installed unless they are standard. explicit about `pip install` requirements if in a capable environment.

## 6. Checklist for Effective Skills

-   [ ] **Description:** Specific, third-person, includes triggers.
-   [ ] **Conciseness:** `SKILL.md` < 500 lines.
-   [ ] **Structure:** References are 1 level deep (no nested linking).
-   [ ] **Scripts:** Robust error handling; no "magic numbers".
-   [ ] **Testing:** Verified with intended models (Sonnet, Opus, etc.).

