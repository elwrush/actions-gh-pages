# SYSTEM CONTEXT HANDOFF: Agent-to-Agent Architecture Brief

**TARGET AUDIENCE:** Gemini CLI Agent / AI Developer
**DOMAIN:** Automated Educational Material Generation (reveal.js Presentations & Worksheets)
**GOAL:** Migrate from linear Markdown generation to a structured, Jinja-templated YAML architecture to solve layout truncation, asset loss, and hallucinated animations.

---

## 1. The Core Problem Statement
The current approach of asking an LLM to generate raw Markdown or HTML for `reveal.js` slideshows fails because LLMs lack spatial awareness. They generate text linearly, leading to:
*   **Layout Spills:** Overfilling slides beyond visual bounds.
*   **Context/Asset Dropping:** Forgetting to persist background videos/images across slide transitions.
*   **Broken Animations:** Failing to correctly assign matching `data-id` attributes required for `reveal.js` `auto-animate` (Magic Move) transitions.

## 2. The Architectural Solution: "The Presentation Director" Pattern
We are adopting a strict **Model-View-Controller (MVC)** inspired architecture to separate content generation from visual rendering.

### A. The Agent's Role (The Controller/Model)
The agent MUST NOT write HTML or Markdown presentations directly. Instead, the agent acts as a "Presentation Director" whose sole output is a strict **YAML Manifest**. 
*   **Constraint-Driven:** The agent selects from a predefined list of layout IDs (e.g., `split-screen`, `title-center`).
*   **State Management:** The agent explicitly declares asset continuity (e.g., `retain_from_previous: true`).
*   **Micro-Directives:** The agent uses bracketed syntax for interactivity (e.g., `[REVEAL: word]`, `[STRIKE: error]`) instead of writing raw `<span>` tags.

### B. The Rendering Engine (The View)
The YAML manifest is passed to a Python script that uses **Jinja2** templates to render the final `reveal.js` HTML.
*   Jinja handles the translation of `[REVEAL: word]` into `<span class="fragment">word</span>`.
*   Jinja automatically injects `data-auto-animate` and manages the tedious `data-id` tracking required for morphing elements across slides.

---

## 3. Mandatory Data Structures

### The YAML Manifest Schema
You must enforce this schema when generating presentation data.

```yaml
presentation:
  title: "String"
  theme: "String"
  slides:
    - slide_id: "unique_string"
      layout: "Enum (title-center | bullet-points | split-screen | big-text | grammar-morph)"
      split_vertical: boolean # For 'deep dive' sub-slides
      background:
        type: "Enum (video | image | color | none)"
        src: "path/to/asset.mp4"
        retain_from_previous: boolean # CRITICAL for seamless transitions
      animation:
        type: "Enum (auto-animate | fade | none)"
      content:
        # Schema varies based on layout Enum
        body_text: "String with [DIRECTIVES]"
        morph_elements: # Used ONLY for grammar-morph layout
          - data_id: "subject"
            text: "The dog"
            position: "left"
```

### Supported ESL Directives (Text Parsing)
Your Jinja parser must support translating these agent-authored directives into `reveal.js` classes:
*   `[REVEAL: word]` -> Hides text until clicked (Fragment).
*   `[STRIKE: word]` -> Crosses out text on click (Error correction).
*   `[HIGHLIGHT: word]` -> Changes text color on click.

---

## 4. Required Development Tasks (The "To-Do" List)
Upon receiving this context, your first objectives are to evaluate the target project's existing "slideshow" and "worksheet" generation skills and execute the following:

1.  **Audit Existing Generators:** Review the current prompts and scripts. Identify where raw Markdown/HTML is being generated.
2.  **Create Design Documents:** Write technical specs detailing the new YAML schema and the Jinja templates required for both Slideshows and Worksheets.
3.  **Implement TDD (Test-Driven Development):**
    *   **"First Run the Tests":** Identify or create the project's test suite (e.g., `pytest`).
    *   **"Red-Green TDD":** Write failing tests for the YAML-to-HTML Jinja parser (e.g., asserting that `[REVEAL: cat]` outputs the correct HTML span). Do not write the parser logic until the test fails.
4.  **Build the Jinja Engine:**
    *   Create the `auto-animate` macro for seamless transitions.
    *   Create the `slide.html` base template that respects the `retain_from_previous` background flag.
5.  **Refactor Agent Prompts:** Update the system instructions for the slideshow/worksheet skills to strictly output the YAML manifest using the "Presentation Director" persona.

## 5. Universal Repository Search Script
To prevent hallucinations and provide ground-truth documentation for Typst, Meander, and reveal.js, use this "Smart Discovery" script. It searches repository trees and fetches raw source documentation directly from GitHub.

```python
import sys
import os
import json
import time
import urllib.request

def get_temp_dir():
    return os.environ.get("GEMINI_TEMP_DIR", os.path.join(os.getcwd(), ".gemini", "tmp"))

def update_typst_timestamp():
    """Satisfies the specific guard hook for Typst files."""
    temp_dir = get_temp_dir()
    os.makedirs(temp_dir, exist_ok=True)
    consult_file = os.path.join(temp_dir, "typst_github_last_consulted.json")
    with open(consult_file, "w") as f:
        json.dump({"timestamp": time.time()}, f)
    print("--- [SUCCESS] Typst consultation timestamp updated ---")

def get_tree(repo):
    temp_dir = get_temp_dir()
    os.makedirs(temp_dir, exist_ok=True)
    repo_slug = repo.replace("/", "_")
    tree_cache = os.path.join(temp_dir, f"tree_{repo_slug}.json")
    
    if os.path.exists(tree_cache) and time.time() - os.path.getmtime(tree_cache) < 86400:
        try:
            with open(tree_cache, "r") as f:
                return json.load(f)
        except Exception:
            pass
            
    url = f"https://api.github.com/repos/{repo}/git/trees/main?recursive=1"
    req = urllib.request.Request(url, headers={'User-Agent': 'Gemini-CLI-Agent'})
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            if repo.lower() == "typst/typst":
                paths = [item["path"] for item in data.get("tree", []) if item["type"] == "blob" and item["path"].startswith("crates/typst-library/src/")]
            else:
                paths = [item["path"] for item in data.get("tree", []) if item["type"] == "blob"]
            with open(tree_cache, "w") as f:
                json.dump(paths, f)
            return paths
    except Exception:
        url = f"https://api.github.com/repos/{repo}/git/trees/master?recursive=1"
        req = urllib.request.Request(url, headers={'User-Agent': 'Gemini-CLI-Agent'})
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                if repo.lower() == "typst/typst":
                    paths = [item["path"] for item in data.get("tree", []) if item["type"] == "blob" and item["path"].startswith("crates/typst-library/src/")]
                else:
                    paths = [item["path"] for item in data.get("tree", []) if item["type"] == "blob"]
                with open(tree_cache, "w") as f:
                    json.dump(paths, f)
                return paths
        except Exception as e:
            return []

def search_and_fetch(repo, query, ext=None):
    paths = get_tree(repo)
    if not paths: return
    query_clean = query.lower().strip()
    if ext: paths = [p for p in paths if p.endswith(ext)]
    matches = [p for p in paths if p.split('/')[-1].split('.')[0].lower() == query_clean]
    if not matches: matches = [p for p in paths if query_clean in p.lower()]
    if not matches: return
    best_match = matches[0]
    raw_url = f"https://raw.githubusercontent.com/{repo}/main/{best_match}"
    req = urllib.request.Request(raw_url, headers={'User-Agent': 'Gemini-CLI-Agent'})
    try:
        try:
            with urllib.request.urlopen(req) as response:
                content = response.read().decode()
        except:
            raw_url = f"https://raw.githubusercontent.com/{repo}/master/{best_match}"
            req = urllib.request.Request(raw_url, headers={'User-Agent': 'Gemini-CLI-Agent'})
            with urllib.request.urlopen(req) as response:
                content = response.read().decode()
        if "typst/typst" in repo.lower(): update_typst_timestamp()
        print(f"--- Content of {best_match} below ---\n")
        print(content)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    repo = sys.argv[1]; query = sys.argv[2]
    ext = sys.argv[3] if len(sys.argv) > 3 else None
    search_and_fetch(repo, query, ext)
```

---
**End of Handoff Context.** Please begin with Task 1: Audit Existing Generators.