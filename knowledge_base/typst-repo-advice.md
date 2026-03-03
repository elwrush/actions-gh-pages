# Engineering Advice: Hybrid Typst Reference System

## Overview
This document explains the "Public Reference + Local Branding" hybrid model used for Typst report generation. This system is designed to ensure that AI agents always use the most current Typst syntax while strictly adhering to local ACT (Assumption College Thonburi) branding standards.

---

## Why This System Is Needed

1.  **Stale Repository Prevention**: Local clones and directory junctions for the Typst codebase quickly become outdated. Referencing the public GitHub repository ensures access to the latest layout functions and foundations.
2.  **Context Efficiency**: Loading a full local repository into the context window is wasteful. Fetching specific raw source files or browsing via the GitHub API allows for "surgical" consultation, preserving tokens.
3.  **Separation of Concerns**: 
    *   **Syntax/Functionality**: Handled by the official Typst repository.
    *   **Branding/Identity**: Handled by the local `lib/act-lib.typ` library.
4.  **Enforcement via Guard Hooks**: Agents are prone to "guessing" layouts or using deprecated patterns (like `#h(1fr)`). A mandatory pre-tool hook forces consultation of both syntax and branding before any `.typ` file can be modified.

---

## How to Implement the System

### 1. The Guard Hook (`scripts/hooks/typst_guard.py`)
Implement a hook that triggers on `BeforeTool` for `write_file` and `replace` on `.typ` files. The hook must validate:
*   **Branding Consultation**: Was `lib/act-lib.typ` read in the last 30 minutes?
*   **Syntax Consultation**: Was a GitHub reference fetched in the last 30 minutes?
*   **Pattern Blocking**: Check for forbidden legacy strings (e.g., `bell_header`, `#h(1fr)`).
*   **Mandatory Imports**: Ensure `#import "/lib/act-lib.typ": *` is present.

### 2. State Tracking (`.gemini/tmp/`)
Use lightweight JSON files to track consultation timestamps:
*   `typst_last_consulted.json`: For local branding.
*   `typst_github_last_consulted.json`: For public syntax.

**Agent Requirement**: After reading the local library or fetching from GitHub, you MUST update the corresponding JSON file with the current Unix timestamp.

### 3. Fetching Strategy (Public Repo)
Do not clone the repo. Use `curl` or `run_shell_command` to:
*   **Browse Structure**: `https://api.github.com/repos/typst/typst/contents/crates/typst-library/src`
*   **Read Source**: `https://raw.githubusercontent.com/typst/typst/main/crates/typst-library/src/layout/mod.rs`

### 4. Local Branding Integration
All project-specific components (headers, footers, frames) reside in `lib/act-lib.typ`. 
*   **Rule**: Never redefine a header in a `.typ` file. Use the `act_header()` function from the library.
*   **Rule**: Always use the standard library for page setups to avoid layout spills.

---

## Workflow for Agents

When tasked with modifying a `.typ` file:

1.  **Consult Branding**: Call `read_file` on `lib/act-lib.typ`.
2.  **Consult Syntax**: Use `curl` to fetch the relevant source from the [Typst GitHub Repo](https://github.com/typst/typst).
3.  **Update State**: Write the current timestamp to the `.gemini/tmp/` tracker files.
4.  **Implement**: Apply changes, ensuring the mandatory import is included.
5.  **Validate**: Run the Typst compiler to ensure no regressions occur.

---

*This system prioritizes "Consultation before Action" to eliminate layout "guessing" and branding drift.*
