# Using Typst for PDF Report Generation

A guide to developing professional PDF reports using Typst + Jinja2 templating. This approach replaces HTML→WeasyPrint pipelines with faster, more reliable typesetting.

## Why Typst?

| Approach | Pros | Cons |
|----------|------|------|
| HTML→WeasyPrint | Familiar syntax | Slow, CSS quirks, poor layout control |
| **Typst** | Fast (~100ms/page), precise layout, native PDF | Learning curve, less documentation |

**Key advantages:**
- **Speed**: 10-50x faster than WeasyPrint
- **Precision**: `breakable: false` prevents orphaned content
- **Native PDF**: No browser engine required
- **Live preview**: VS Code extension available

---

## Architecture Pattern

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────┐
│  Python Script  │───▶│  Jinja2 Template │───▶│  .typ file  │
│  (data prep)    │    │  (template.typ)  │    │  (rendered) │
└─────────────────┘    └─────────────────┘    └─────────────┘
                                                      │
                                                      ▼
                                              ┌─────────────┐
                                              │  typst CLI  │
                                              │  compile    │
                                              └─────────────┘
                                                      │
                                                      ▼
                                              ┌─────────────┐
                                              │   PDF File  │
                                              └─────────────┘
```

**Core components:**
1. **Generator Script** (Python): Loads data, escapes content, renders template
2. **Template** (.typ with Jinja2): Layout + placeholders
3. **Typst CLI**: Compiles rendered .typ to PDF

---

## Quick Start Template

### 1. Create Template (`templates/example_report.typ`)

```typst
// Page setup
#set page(paper: "a4", margin: 1.5cm)
#set text(font: "Charter", size: 11pt)
#set par(leading: 0.65em)

// Design tokens
#let heading-font = "Helvetica"
#let primary = rgb("#8B1538")  // Maroon
#let gray-light = rgb("#F5F5F5")

// ========== DATA (Jinja injects) ==========
#let title = "{{ title }}"
#let student_name = "{{ student_name }}"
#let score = {{ score }}  // Note: no quotes for numbers

// Arrays use Jinja loops
#let items = (
{% for item in items %}
  (label: "{{ item.label }}", value: {{ item.value }}),
{% endfor %}
)

// Content blocks use [...]
#let description = [{{ description }}]

// ========== LAYOUT ==========
#text(font: heading-font, 16pt, weight: "bold", fill: primary)[#title]
#v(10pt)

#block(
  fill: gray-light,
  inset: 12pt,
  radius: 4pt,
  width: 100%,
)[
  Student: *#student_name* #h(1fr) Score: *#score*/5
]
#v(15pt)

#description

#v(10pt)
#for item in items [
  • #item.label: *#item.value*
  #v(4pt)
]
```

### 2. Create Generator Script (`scripts/generate_example.py`)

```python
#!/usr/bin/env python3
"""
Example Typst PDF Generator
"""
import json
import subprocess
import sys
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

# Force UTF-8 for Windows console
sys.stdout.reconfigure(encoding='utf-8')

PROJECT_ROOT = Path("C:/PROJECTS/YOUR_PROJECT")
TEMPLATE_DIR = PROJECT_ROOT / "templates"

def escape_typst(text: str) -> str:
    """Escape special Typst characters."""
    if not text:
        return ""
    for char in ['\\', '#', '$', '%', '&', '@', '*', '_', '[', ']']:
        text = text.replace(char, f"\\{char}")
    return text

def generate_report(data: dict, output_path: Path):
    """Generate PDF from data dictionary."""
    
    # Prepare context with escaped strings
    context = {
        'title': escape_typst(data.get('title', 'Report')),
        'student_name': escape_typst(data.get('student_name', 'Unknown')),
        'score': data.get('score', 0),  # Numbers don't need escaping
        'description': escape_typst(data.get('description', '')),
        'items': [
            {'label': escape_typst(i['label']), 'value': i['value']}
            for i in data.get('items', [])
        ]
    }
    
    # Render template
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template('example_report.typ')
    typst_code = template.render(**context)
    
    # Write .typ file
    typ_path = output_path.with_suffix('.typ')
    with open(typ_path, 'w', encoding='utf-8') as f:
        f.write(typst_code)
    
    # Compile to PDF
    result = subprocess.run(
        ['typst', 'compile', '--root', str(PROJECT_ROOT), 
         '--pdf-standard', '1.4', str(typ_path), str(output_path)],
        capture_output=True, text=True, encoding='utf-8', errors='replace'
    )
    
    if result.returncode != 0:
        print(f"FAILED: {result.stderr[:500]}")
        return False
    
    print(f"Generated: {output_path}")
    return True

if __name__ == "__main__":
    # Example usage
    sample_data = {
        'title': 'Student Progress Report',
        'student_name': 'John Smith',
        'score': 4,
        'description': 'Good progress this term with notable improvements.',
        'items': [
            {'label': 'Attendance', 'value': 95},
            {'label': 'Homework', 'value': 88},
        ]
    }
    generate_report(sample_data, PROJECT_ROOT / "outputs/example.pdf")
```

---

## Critical Rules

### 1. Strings vs Content Blocks

| Data Type | Syntax | Use Case |
|-----------|--------|----------|
| **String** | `"{{ value }}"` | Simple text without formatting |
| **Content Block** | `[{{ value }}]` | Text that MAY contain Typst markup |

> [!CAUTION]
> **0-Page PDF Error**: If you inject Typst markup (`#text[...]`) into a *string*, Typst treats `#` as a literal character and may fail silently. Always use content blocks for formatted content.

```typst
// ❌ WRONG - markup inside string
#let description = "{{ description }}"  // If description contains #text[...], fails!

// ✅ CORRECT - markup inside content block
#let description = [{{ description }}]
```

### 2. Escaping Special Characters

Always escape user content before injection:

```python
def escape_typst(text: str) -> str:
    """Escape special Typst characters."""
    if not text:
        return ""
    for char in ['\\', '#', '$', '%', '&', '@', '*', '_', '[', ']']:
        text = text.replace(char, f"\\{char}")
    return text
```

### 3. HTML to Typst Bold Conversion

If your source data contains `<b>...</b>` tags:

```python
import re

def html_bold_to_typst(text: str) -> str:
    """Convert <b>...</b> to Typst bold, then escape other chars."""
    if not text:
        return ""
    
    # Extract bold sections with placeholders
    bold_parts = []
    def save_bold(match):
        bold_parts.append(match.group(1))
        return f"ZZBOLD{len(bold_parts)-1}ZZ"
    
    text = re.sub(r'<b>(.*?)</b>', save_bold, text, flags=re.DOTALL)
    
    # Strip remaining HTML
    text = re.sub(r'<[^>]+>', '', text)
    
    # Escape Typst chars
    text = escape_typst(text)
    
    # Restore bold with Typst syntax
    for i, part in enumerate(bold_parts):
        escaped_part = escape_typst(part)
        text = text.replace(f"ZZBOLD{i}ZZ", f'#text(weight: "bold")[{escaped_part}]')
    
    return text
```

### 4. Prevent Page Breaks (Orphan Prevention)

```typst
// Wrap content that should stay together
#block(breakable: false)[
  #text(weight: "bold")[Section Header]
  #v(6pt)
  Content that must stay with header...
]
```

---

## Styling Patterns

### Color Theme

```typst
#let primary = rgb("#8B1538")   // Maroon (headers, accents)
#let gray-light = rgb("#F5F5F5") // Light gray (backgrounds)
#let gray-medium = rgb("#333333") // Dark gray (body text)
```

### Typography

```typst
#set text(font: "Charter", size: 11pt)
#set par(leading: 0.65em)
#let heading-font = "Helvetica"

// Header with custom font
#text(font: heading-font, 15pt, weight: "bold", fill: primary)[Title]
```

### Common Blocks

```typst
// Info card with left accent
#block(
  fill: gray-light,
  inset: (left: 12pt, right: 12pt, top: 8pt, bottom: 8pt),
  stroke: (left: 4pt + primary),
  width: 100%,
)[Content here]

// Bordered box
#block(
  stroke: 2pt + primary,
  radius: 6pt,
  inset: 12pt,
  width: 100%,
)[Content here]

// Full-width divider
#line(length: 100%, stroke: 3pt + primary)
```

### Lists with Custom Bullets

```typst
#for item in items [
  #block(inset: (left: 8pt, top: 4pt, bottom: 4pt))[
    #grid(
      columns: (16pt, 1fr),
      gutter: 6pt,
      [•],
      item
    )
  ]
]
```

### Alternating Row Shading

```typst
#for (i, item) in items.enumerate() [
  #block(
    fill: if calc.odd(i) { gray-light } else { white },
    inset: 10pt,
    width: 100%,
  )[#item]
]
```

---

## Batch Processing Pattern

For generating multiple PDFs (e.g., class reports):

```python
from pypdf import PdfReader, PdfWriter

def generate_batch(batch_name: str, output_path: Path):
    """Generate combined PDF with 4-page duplex padding."""
    
    json_files = sorted(batch_dir.glob("*.json"))
    final_writer = PdfWriter()
    
    for json_path in json_files:
        # Generate individual PDF
        temp_pdf = temp_dir / f"{json_path.stem}.pdf"
        generate_single_report(json_path, temp_pdf)
        
        # Append pages
        reader = PdfReader(str(temp_pdf))
        for page in reader.pages:
            final_writer.add_page(page)
        
        # Pad to 4 pages for duplex printing
        content_pages = len(reader.pages)
        padding = (4 - (content_pages % 4)) % 4
        if content_pages < 4:
            padding = 4 - content_pages
        for _ in range(padding):
            final_writer.add_blank_page()
    
    # Save combined PDF
    with open(output_path, 'wb') as f:
        final_writer.write(f)
```

---

## Compilation

### CLI Usage

```bash
# Basic compilation
typst compile template.typ output.pdf

# With project root (for image paths)
typst compile --root "C:/PROJECTS/MY_PROJECT" template.typ output.pdf

# PDF 1.4 for better viewer compatibility
typst compile --pdf-standard 1.4 template.typ output.pdf
```

### From Python

```python
import subprocess

result = subprocess.run(
    ['typst', 'compile', '--root', str(PROJECT_ROOT), 
     '--pdf-standard', '1.4', str(typ_path), str(pdf_path)],
    capture_output=True, text=True, encoding='utf-8', errors='replace'
)

if result.returncode != 0:
    print(f"Error: {result.stderr}")
```

---

## Debugging

### Silent Failures (0-Page PDF)

**Symptom:** PDF generated but has 0 pages or missing content.

**Cause:** Typst syntax error (often from unescaped characters or markup in strings).

**Fix:**
1. Open the rendered `.typ` file
2. Check for `#` characters inside string literals `"..."`
3. Switch to content blocks `[...]` for formatted data

### Windows Console Crashes

**Symptom:** Script fails with Unicode error.

**Fix:** Add at script start:
```python
import sys
sys.stdout.reconfigure(encoding='utf-8')
```

And use ASCII status symbols:
```python
print("[OK]")   # Not "✓"
print("[X]")    # Not "❌"
```

---

## Dependencies

```bash
# Install Typst CLI
# Windows: winget install typst
# macOS: brew install typst
# Linux: cargo install typst-cli

# Python dependencies
pip install jinja2 pypdf
```

---

## File Structure

```
project/
├── templates/
│   ├── feedback_report.typ
│   └── cohort_analysis.typ
├── scripts/
│   ├── generate_feedback.py
│   └── generate_cohort.py
├── outputs/
│   └── REPORTS/
└── images/
    └── logo.jpg
```

---

## Resources

- [Typst Documentation](https://typst.app/docs)
- [Typst Packages](https://typst.app/packages)
- [VS Code Extension: Typst LSP](https://marketplace.visualstudio.com/items?itemName=mgt19937.typst-lsp)
