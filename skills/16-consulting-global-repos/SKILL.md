---
name: 16-consulting-global-repos
description: >
  Official repository consultation engine using the GitHub REST API.
  Use this to fetch Typst syntax, pedagogical patterns, and code references
  from global sources of truth without token churn.
---

# Consulting Global Repos

This skill enables precise, API-driven discovery of code patterns and documentation from external repositories. It utilizes the `GITHUB_MCP_PAT` for authenticated, high-rate-limit access.

## 🛑 MANDATORY: THE "SOURCE OF TRUTH" LAW
You MUST NOT guess architectural patterns or library syntax. If the local project refers to an external standard (like Typst or Reveal.js), you MUST consult the official repository using this skill before implementation.

## 🛠️ The Tool: `gh_fetch.py`
The engine for this skill is located at `skills/16-consulting-global-repos/scripts/gh_fetch.py`.

### Usage Patterns
Run via `run_shell_command`:
```powershell
python skills/16-consulting-global-repos/scripts/gh_fetch.py <alias>:<path>
```

**Common Commands:**
- **List Directory**: `python skills/16-consulting-global-repos/scripts/gh_fetch.py typst:crates/typst-library/src`
- **Fetch File**: `python skills/16-consulting-global-repos/scripts/gh_fetch.py typst:crates/typst-library/src/layout/grid.rs`

## 🛑 THE INTERACTIVE WORKFLOW

1. **Identify the Gap**: Determine what syntax, schema, or pattern is missing or ambiguous.
2. **Consult Reference**: Check `REFERENCE.md` for known repository aliases (e.g., `typst`, `revealjs`).
3. **Execute Fetch**: Use the `gh_fetch.py` script to pull the directory listing or specific file content.
4. **Analyze & Extract**: Read the returned code to identify the exact implementation pattern.
5. **Apply Surgically**: Integrate the pattern into the workspace following local conventions.

## Repository Aliases (Shortcuts)
| Alias | Repository | Purpose |
|-------|------------|---------|
| `typst` | `typst/typst` | Official Typst source & library components. |
| `revealjs` | `hakimel/reveal.js` | Presentation framework core. |
| `fontawesome` | `FortAwesome/Font-Awesome` | Icon metadata and SVG paths. |
| `reference` | `elwrush/lesson-plan-references` | Project-specific pedagogical templates. |
| `meander` | `Vanille-N/meander.typ` | Meander package for text wrapping. |

## Troubleshooting
- **401 Unauthorized**: Ensure `GITHUB_MCP_PAT` is correctly set in your environment.
- **404 Not Found**: Verify the alias mapping in `gh_fetch.py` or the specific path on GitHub.
- **Rate Limit**: Authenticated requests allow for 5,000 requests per hour.
