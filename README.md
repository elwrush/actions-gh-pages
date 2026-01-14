# Lesson Plan Agent

AI-powered lesson planning assistant for English language teachers, built with Google Gemini and the Skills-based architecture.

## Overview

This project provides an interactive workflow for creating lesson plans using predefined lesson "shapes" (pedagogical frameworks). It integrates with Google Docs for materials preparation and export.

## Features

### 🎯 Skills

#### `writing-lesson-plans`
Interactive 8-step workflow for creating lesson plans:
- 10 lesson shapes (A-J): Traditional frameworks (PPP, TTT, TBL, Receptive/Productive Skills) + SCR Storytelling frameworks
- CEFR-aligned vocabulary pre-teaching (reading/listening lessons)
- Automatic answer key generation
- Thai-English bilingual support
- Model compliance with pedagogical intent

#### `developing-bespoke-materials`
Creates custom educational materials tailored to CEFR levels and skill types:
- Transform existing materials or write brand new content
- Bell/Intensive program branding
- Mandatory answer keys and transcripts
- GDocs-compatible HTML output
- Image generation with fallback protocol



#### `generating-worksheets`
Generates branded, print-ready PDF worksheets:
- Jinja2-based templating system
- Bell/Intensive dual branding support
- Playwright HTML-to-PDF conversion
- Custom headers and quotes

#### `publishing-worksheets`
Uploads PDF worksheets to Google Drive:
- Automatic filename convention (DD-MM-YY-Worksheet-[Title].pdf)
- OAuth authentication
- Validation workflow requirement

#### `converting-to-gdocs-html`
Converts content to HTML that imports cleanly into Google Docs:
- GDocs typography standards
- Inline styles for import compatibility
- Table-based layouts for complex content
- Element shading and borders

#### `pushing-to-gdocs`
Uploads HTML content to Google Drive and converts to Google Docs:
- Base64 image embedding
- A4 format with 2cm margins auto-setup
- Drive + Docs API integration
- Formatted paragraph preference over tables

#### `committing-to-github` (Global)
Git workflow automation:
- Staging and committing
- Automatic `desktop.ini` exclusion (Google Drive sync)
- Commit message conventions
- Push confirmation
- Triggered with `/commit`

### 📚 Lesson Shapes

| Shape | Type | Use Case |
|-------|------|----------|
| **A** | Text-based Presentation | Language via reading/listening |
| **B** | Language Practice | Follow-up practice |
| **C** | Test-Teach-Test (TTT) | Testing prior knowledge |
| **D** | Situational Presentation (PPP) | New language in context |
| **E** | Receptive Skills | Reading/Listening focus |
| **F** | Productive Skills | Speaking/Writing focus |
| **G** | Task-Based Learning | Communication-first |

## Project Structure

```
.
├── skills/                    # Modular skills (Skills architecture)
│   ├── writing-lesson-plans/
├── knowledge_base/            # Reference data
│   ├── lesson_shapes.yaml
│   └── slide-design-principles.md
├── images/                    # Brand assets
│   ├── Bell.png
│   └── ACT.png
├── .credentials/              # OAuth credentials (not in repo)
├── session-log.md             # Development log
└── errors-fix.md              # Error tracking

```

## Setup

### Prerequisites

- Python 3.8+
- Google Cloud Project with APIs enabled:
  - Google Drive API
  - Google Docs API (future)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/elwrush/lesson-plan-agent.git
   cd lesson-plan-agent
   ```

2. Install dependencies:
   ```bash
   pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib
   ```

3. Set up Google OAuth credentials:
   - Create OAuth 2.0 Client ID (Desktop Application) in Google Cloud Console
   - Download `credentials.json` to `.credentials/`
   - First run will prompt for authentication and create `token.json`

## Usage

### Creating a Lesson Plan

Follow the `writing-lesson-plans` skill workflow:
1. Select lesson shape (A-G)
2. Provide metadata (CEFR level, focus, duration, etc.)
3. Choose materials source
4. Review objective and marker sentences
5. Generate lesson plan in markdown
6. Export to Google Docs (coming soon)


## Skills Architecture

This project follows the **Skills-based architecture** methodology:
- Skills are modular, filesystem-based capabilities
- Each skill has `SKILL.md` (workflow) and `REFERENCE.md` (quick reference)
- Progressive disclosure: metadata → instructions → resources

See [`knowledge_base/using-skills.md`](knowledge_base/using-skills.md) for details.

## Design Principles

- **Educational slide design**: Text limits, high contrast, 30pt+ fonts
- **Material Design 3**: Color roles, typography scale, 8px grid
- **Bell EP branding**: Maroon RGB(166,45,38), white text on dark

## Development

### Session Logs
- [`session-log.md`](session-log.md) - Development history
- [`errors-fix.md`](errors-fix.md) - Error tracking

### Contributing

When committing, use conventional commit format:
```
<type>: <subject>

Types: feat, fix, docs, refactor, chore
```

## License

Private/Educational Use

## Contact

Bell Language Centre - English Program
