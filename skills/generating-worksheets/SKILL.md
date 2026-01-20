---
name: generating-worksheets
description: >
  Generates professional, branded PDF worksheets using Typst.
  Use when the user requests worksheet creation, especially for grammar or skill-based activities.
---

# Generating Worksheets Skill

## Description
Generates high-quality, print-ready PDF worksheets using **Typst**, offering superior layout control, precise pagination, and "printer-safe" margins.

## Prerequisites
- **Typst CLI** must be installed and accessible in the terminal.
- **Branding Assets** must be present in `/images/`:
  - Bell: `ACT_transparent.png`, `Bell.svg`
  - Intensive: `intensive-header.jpg`

- **If Intensive**: Use `images/intensive-header.jpg` as the header image. 
  - **CRITICAL**: **NEVER** use the maroon strap or the `integrated_header()` function.
  - **PRINTER SAFETY**: The header image MUST be **center-aligned** and have at least **0.5cm of top padding** from the edge of the sheet (do not use `dy: -1.5cm`).
  - **Action**: Use the `intensive_header()` function and ensure it uses `align(center)` and reasonable vertical spacing.

## Reference Material
- **Bell Template**: `knowledge_base/templates/grammar_repair_worksheet_gold.typ`
- **Intensive Template**: `skills/generating-worksheets/templates/intensive_worksheet_template.typ`

## Workflow

1. **Source the Template**:
   - Copy the gold standard template from `knowledge_base/templates/grammar_repair_worksheet_gold.typ`.
   - Save it to `skills/generating-worksheets/templates/[new_worksheet_name].typ`.

2. **Select Header**:
   - **Bell**: Use `#integrated_header()` with maroon strap and logos.
   - **Intensive**: Use `#intensive_header()` which displays `intensive-header.jpg`.
3. **Content Generation**:
   - **Page 1 Branding**: Use the main header strap (e.g., Bell or Intensive) **only on Page 1**. Subsequent pages should remain clean.
   - **Section Headers**: Use "Task X" (e.g., Task 1, Task 2) rather than "Part X".
   - **Terminology**: Use specific text types (e.g., "Article", "Report") instead of generic terms like "Story".
   - **Orphan Prevention**: **CRITICAL**. Wrap every Task header and its instructions in a block with `breakable: false` (e.g., `#block(breakable: false)[ #section_header(...) ... ]`). Never let a header sit alone at the bottom of a page.
   - **No Separators**: Do **not** use horizontal lines to separate tasks. Use whitespace and clear headers.

4. **Design & Layout Standards (CRITICAL)**:
   - **Native Graphics**: Use Typst's native `stack`, `circle`, `line`, and `gradient` for headers. **DO NOT** use external decorative images or simple/naff placeholders. 
   - **Writing Lines**: 
     - **Dynamic Alignment**: ALWAYS use `#box(width: 1fr, repeat("."))` for leaders and writing lines.
     - **Justification**: Set `#set par(justify: false)` for worksheets with leaders to prevent unsightly text stretching.
     - **Color**: Use **Dark Gray (#666666)** or darker (#4D4D4D) for all lines to ensure visibility in photocopies. **NEVER** use light gray (#E0E0E0).
   - **Typography**: Minimum font size is **11pt** for student facings text.

5. **Compile PDF**:
   - Compiling follows a strict naming convention: `DD-MM-YYYY-[CEFR LEVEL]-[DESCRIPTION].pdf`.
   - Run the Typst initialization command from the project root:
   ```powershell
   typst compile "skills/generating-worksheets/templates/[template].typ" "inputs/[Folder]/DD-MM-YYYY-[CEFR_LEVEL]-[DESCRIPTION].pdf" --root "."
   ```
   - *Example: `11-01-2026-A2-B2-Grammar-Repair-Shop.pdf`*

6. **🧪 Validate (MANDATORY)**:
   Run the validator before finalizing:
   ```powershell
   python skills/generating-worksheets/scripts/validate_worksheet.py "path/to/worksheet.typ" --mode [bell|intensive]
   ```
   - **Rule**: If the script fails, fix the issues and re-run until it passes.
   - **Checks**: Branding, writing line limits (max 15), image paths, pagebreaks.

7. **🚦 Visual Verify**:
   - **Photocopy Safety**: Are lines Dark Gray (#666666)?
   - **Layout**: Are writing lines perfectly aligned (using `box(width: 1fr...)`)?
   - **Orphans**: Are headers attached to their content?
   - **Spillover**: Does every page fit perfectly without content bleeding to the next?
   - **Legibility**: Is text size >= 11pt?

8. **🏁 THE LINK GATE (MANDATORY)**:
   > [!CRITICAL]
   > **YOU MUST PROVIDE A CLICKABLE LINK TO THE PDF.**
   > 
   > **Action**: Post the link using the `file:///` protocol so the user can open it in the IDE.
   > 
   > **Example**: [My Worksheet](file:///path/to/worksheet.pdf)
   > 
   > **DO NOT** proceed to any follow-up tasks (like lesson planning or pushing to Drive) until this link is provided and the user has seen it.

## Template Structure
The Typst template uses a functional component approach:
- `#integrated_header()`: **BELL ONLY - Page 1**. The maroon strap with logos and title.
- `#intensive_header()`: **INTENSIVE ONLY**. Full-width branding image (`intensive-header.jpg`). Do NOT add text or straps over this.
- `#task_card()`: Boxed prompt with level and context.
- `#radar_box()`: Self-correction checklist.
- `#writing_lines(count: 15)`: Fixed-height writing area using `repeat(".")`.
