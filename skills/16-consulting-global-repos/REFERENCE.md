# GitHub Consultation Reference

## Repository Aliases
Mappings used by `gh_fetch.py`:

| Alias | Repository | Description |
|-------|------------|-------------|
| `typst` | `typst/typst` | Official Typst source (Rust) & Language features. |
| `revealjs` | `hakimel/reveal.js` | Core presentation engine. |
| `fontawesome` | `FortAwesome/Font-Awesome` | Metadata for icons and SVG definitions. |
| `reference` | `elwrush/lesson-plan-references` | **MANDATORY**: Pedagogical templates for Bell/Intensive (replacing /lib/). |

## Useful Typst Paths
- **Grid Layout**: `typst:crates/typst-library/src/layout/grid.rs`
- **Tables**: `typst:crates/typst-library/src/layout/table.rs`
- **Images**: `typst:crates/typst-library/src/visualize/image.rs`
- **Metadata Handling**: `typst:crates/typst-library/src/meta/mod.rs`

## FontAwesome Implementation Strategy
To use FontAwesome in Typst:
1.  **Check Packages**: Consult `typst:packages/preview/fontawesome` (if searching the package repo).
2.  **Verify Versions**: Ensure `0.6.0` matches the current project standard.
3.  **Local Assets**: Verify if `.otf` fonts are required in the project's `fonts/` directory.
