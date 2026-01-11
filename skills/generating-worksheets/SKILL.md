---
name: generating-worksheets
description: >
  Generates professional, branded PDF worksheets using Typst.
  Use when the user requests worksheet creation, especially for grammar or skill-based activities.
---

# Generating Worksheets Skill

## Description
Generates high-quality, print-ready PDF worksheets using **Typst**. This workflow replaces the legacy HTML/WeasyPrint method, offering superior layout control, precise pagination, and "printer-safe" margins.

## Prerequisites
- **Typst CLI** must be installed and accessible in the terminal.
- **Bell/ACT Logos** must be present in the project root `/images/` directory.

## Reference Material
- **Gold Standard Template**: `knowledge_base/templates/grammar_repair_worksheet_gold.typ`
  - *Use this as the source of truth for all new worksheets.*
  - *Features: Integrated "Strap" header, 14pt left-aligned title, 15-line writing limit, zero spillover.*

## Workflow

1. **Source the Template**:
   - Copy the gold standard template from `knowledge_base/templates/grammar_repair_worksheet_gold.typ`.
   - Save it to `skills/generating-worksheets/templates/[new_worksheet_name].typ`.

2. **Customize Content**:
   - **Header**: Update the title in the integrated strap (separated by `|` from "BELL LANGUAGE CENTRE").
   - **Diagnostic Section (Page 1)**: Customize the "Repair Targets" or introductory activity.
   - **Tasks (Pages 2-4)**: 
     - Update the `task_card` function calls with specific prompts, contexts, and constraints.
     - **Constraint**: Maintain the **15-line limit** for writing areas to ensure zero spillover.
     - **Pagination**: Keep strict `#pagebreak()` calls between levels (A2/B1/B2).

3. **Compile PDF**:
   - Compiling follows a strict naming convention: `DD-MM-YYYY-[CEFR LEVEL]-[DESCRIPTION].pdf`.
   - Run the Typst initialization command from the project root:
   ```powershell
   typst compile "skills/generating-worksheets/templates/[template].typ" "inputs/[Folder]/DD-MM-YYYY-[CEFR_LEVEL]-[DESCRIPTION].pdf" --root "."
   ```
   - *Example: `11-01-2026-A2-B2-Grammar-Repair-Shop.pdf`*

4. **🚦 Verify**:
   - Check for **printer safety**: Are headers inside the margins?
   - Check for **logo visibility**: Are the SVG/PNG logos rendering correctly?
   - Check for **spillover**: Does every page fit perfectly without content bleeding to the next?

## Template Structure
The Typst template uses a functional component approach:
- `#integrated_header()`: The maroon strap with logos and title.
- `#task_card()`: Boxed prompt with level and context.
- `#radar_box()`: Self-correction checklist.
- `#writing_lines(count: 15)`: Fixed-height writing area.

## Legacy Methods (Deprecated)
- *HTML/WeasyPrint*: Do not use.
- *Playwright PDF*: Do not use.
