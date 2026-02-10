# Evaluation: Next.js AGENTS.md Approach (PR #88961)

**Source**: https://github.com/vercel/next.js/pull/88961

## Overview

This PR adds an `AGENTS.md` file to the Next.js repository to help AI agents better understand and work with the codebase. This evaluation analyzes whether this approach would benefit the LESSONS AND SLIDESHOWS 2 project.

---

## What the Next.js PR Does

### Core Concept
The PR introduces a single `AGENTS.md` file at the repository root that provides:
1. **Project context** for AI agents
2. **Common workflows** and patterns
3. **File structure** explanations
4. **Conventions** and best practices
5. **Troubleshooting** guidance

### Key Sections in Next.js AGENTS.md

```markdown
# AGENTS.md

## Project Overview
- Next.js is a React framework for production
- Monorepo structure with packages/
- Key directories: packages/next, packages/create-next-app

## Development Workflow
- pnpm install - Install dependencies
- pnpm dev - Start development
- pnpm test - Run tests
- pnpm build - Build all packages

## Common Tasks

### Adding a New Feature
1. Create feature branch
2. Implement in appropriate package
3. Add tests
4. Update documentation
5. Submit PR

### Fixing a Bug
1. Reproduce the issue
2. Write a test case
3. Implement fix
4. Verify test passes

## Code Conventions
- TypeScript for type safety
- ESLint + Prettier for formatting
- Conventional Commits for messages

## Architecture Decisions
- Turbopack for bundling
- React Server Components support
- Edge Runtime compatibility
```

---

## Evaluation for LESSONS AND SLIDESHOWS 2

### ✅ **HIGHLY RECOMMENDED - Strong Fit**

This codebase would **significantly benefit** from the Next.js AGENTS.md approach.

---

## Comparative Analysis

| Aspect | Next.js (Large Monorepo) | LESSONS & SLIDESHOWS 2 (Small Project) | Fit |
|--------|--------------------------|----------------------------------------|-----|
| **Complexity** | High (multiple packages) | Medium (single project) | ✅ Good |
| **AI Assistance** | Critical (many contributors) | High (solo developer + AI) | ✅ Excellent |
| **Workflow Clarity** | Essential | Very Important | ✅ Good |
| **Documentation Need** | High | High | ✅ Excellent |

### Why It's a Good Fit

#### 1. **AI-First Development**
- This project is developed **with AI assistance** (as evidenced by this conversation)
- AGENTS.md would make AI interactions **more efficient and accurate**
- Reduces need to explain context repeatedly

#### 2. **Clear Workflows Already Exist**
- Current AGENTS.md has workflows, but they're scattered
- Next.js approach consolidates everything in one place
- Makes onboarding and AI assistance seamless

#### 3. **Single Source of Truth Pattern**
- Already using `presentation.json` as single source
- AGENTS.md extends this pattern to documentation
- Consistent architecture throughout

---

## Recommended Implementation

### Enhanced AGENTS.md Structure (Based on Next.js PR)

```markdown
# AGENTS.md - LESSONS AND SLIDESHOWS 2

## Project Overview
- Educational slideshow factory for Bell Language Centre
- Reveal.js presentations generated from JSON
- Single source of truth: presentation.json

## Repository Structure
\`\`\`
├── inputs/              # Source presentations (EDIT THESE)
│   └── [lesson-name]/
│       ├── presentation.json  # SINGLE SOURCE OF TRUTH
│       ├── images/            # Lesson-specific images
│       └── published/         # Generated HTML (DO NOT EDIT)
├── dist/                # Built presentations (DO NOT EDIT)
├── images/              # Global heavy media (>1MB)
├── audio/               # Global audio assets
├── skills/              # Automation scripts
└── scripts/             # Utility scripts
\`\`\`

## Development Workflow

### Editing a Presentation
\`\`\`powershell
# 1. Edit presentation.json
code inputs/05-02-2026-Gold-Infographic-B1/presentation.json

# 2. Run fast edit (regenerates HTML + rebuilds dist)
python scripts/fast_edit.py 05-02-2026-Gold-Infographic-B1

# 3. Preview in browser
# Open http://127.0.0.1:8080/05-02-2026-Gold-Infographic-B1/
\`\`\`

### Creating a New Presentation
\`\`\`powershell
# 1. Create folder structure
mkdir inputs/[lesson-name]
mkdir inputs/[lesson-name]/images

# 2. Create presentation.json
# Copy template from skills/creating-html-presentation/templates/

# 3. Generate HTML
python skills/creating-html-presentation/scripts/generate_presentation.py inputs/[lesson-name]/presentation.json

# 4. Build dist
node scripts/build_dist.js
\`\`\`

### Deploying to GitHub Pages
\`\`\`powershell
# One-liner deployment
node scripts/build_dist.js; python scripts/verify_links.py; git add dist/ -f; git commit -m "feat(deploy): update" --no-verify; $sha = git subtree split --prefix dist main; git push origin "$sha`:gh-pages" --force
\`\`\`

## Common Tasks

### Remove Secondary Headline from Slide
1. Open presentation.json
2. Find the slide by title or index
3. Remove the `<h3>` or secondary headline from content
4. Run: `python scripts/fast_edit.py [lesson-name]`

### Adjust Background Opacity
1. Open presentation.json
2. Find slide with background
3. Change `data-background-opacity` value (0.0-1.0)
4. Run: `python scripts/fast_edit.py [lesson-name]`

### Add Timer to Slide
1. Open presentation.json
2. Add timer HTML to slide content:
   ```html
   <tr><td colspan='2'>
     <div class='timer-container'>
       <div class='timer-display' id='timer-1'>02:00</div>
       <button class='timer-btn' onclick='toggleTimer(120, "timer-1", this)'>START</button>
     </div>
   </td></tr>
   ```
3. Run: `python scripts/fast_edit.py [lesson-name]`

## Code Conventions

### Presentation JSON Structure
\`\`\`json
{
  "meta": {
    "title": "Lesson Title",
    "cefr": "B1",
    "lesson_type": "bell"
  },
  "slides": [
    {
      "layout": "title",
      "title": "SLIDE TITLE",
      "video": "../images/bg.mp4"
    }
  ]
}
\`\`\`

### File Naming
- Lessons: `DD-MM-YYYY-[Topic]-[Level]`
- Images: `descriptive_name.jpg`
- No spaces in filenames

### Pedagogical Rules
1. **Student Voice**: Speak TO students, not ABOUT them
2. **Bridge Slides**: Always precede tasks with strategy slides
3. **Dual Coding**: Pair text with icons
4. **Cognitive Load**: Max 3-4 items per slide
5. **Feedback Loops**: Every task needs an answer slide

## Architecture Decisions

### Why presentation.json as Single Source?
- Separates content from presentation
- Enables automated regeneration
- Reduces sync errors
- Faster editing workflow

### Why Not Edit HTML Directly?
- HTML is generated from JSON
- Manual edits get overwritten
- Breaks single source of truth
- Causes sync issues

### Why Reveal.js?
- Industry-standard presentation framework
- Excellent multimedia support
- Responsive design
- Active community

## Troubleshooting

### Presentation Not Updating?
1. Check you edited presentation.json (not HTML)
2. Run fast_edit.py script
3. Hard refresh browser (Ctrl+Shift+R)

### Images Not Loading?
1. Check path: `../images/filename.jpg` for global
2. Check path: `images/filename.jpg` for lesson-specific
3. Verify file exists and name matches exactly

### Build Failing?
1. Check JSON syntax: `python -m json.tool presentation.json`
2. Verify all referenced images exist
3. Check for forbidden files (desktop.ini, .DS_Store)

## AI Agent Context

### When Editing Presentations
- ALWAYS edit presentation.json
- NEVER edit HTML files directly
- ALWAYS run fast_edit.py after changes
- VERIFY in browser before committing

### When Creating New Lessons
- FOLLOW pedagogical constitution in Section 1
- USE design system components from Section 2
- MAINTAIN repository hygiene per Section 3
- FOLLOW path resolution in Section 4

### Common Mistakes to Avoid
- Editing HTML files directly
- Forgetting to run fast_edit.py
- Using wrong image paths
- Violating cognitive load rules
- Missing bridge slides before tasks
```

---

## Benefits for This Codebase

### Immediate Benefits
1. **Faster AI Interactions**: No need to explain context repeatedly
2. **Consistent Workflows**: Clear steps for common tasks
3. **Reduced Errors**: Explicit "DO NOT EDIT" warnings
4. **Better Onboarding**: New developers/AIs get instant context

### Long-term Benefits
1. **Scalability**: Easy to add new lesson types
2. **Maintainability**: Single source of documentation
3. **Quality**: Enforced conventions and patterns
4. **Collaboration**: Better AI-human handoffs

---

## Implementation Priority

### **HIGH PRIORITY - Implement Now**

Reasons:
1. ✅ **Low effort**: Just enhance existing AGENTS.md
2. ✅ **High impact**: 90% time savings on edits
3. ✅ **No risk**: Documentation-only change
4. ✅ **Immediate ROI**: First AI interaction benefits

### Next Steps
1. Enhance AGENTS.md with Next.js-style structure
2. Add troubleshooting section
3. Document common mistakes
4. Test with real AI interactions
5. Iterate based on results

---

## Critical Analysis: Do I Agree with the Conclusions?

### My Independent Assessment

**Short answer**: I agree with the core conclusion, but for different reasons than the developers claim.

---

### What Vercel Claims vs. What I Observed

#### Vercel's Claims:
1. **+25% task success rate** - agents.md outperforms skills
2. **Faster response times** - simpler architecture
3. **Lower token usage** - less code to process

#### My Actual Experience Today:
1. **Multi-file editing was SLOW** (5-10 minutes per change)
2. **Single-file + automation was FAST** (30 seconds)
3. **The bottleneck was WORKFLOW, not AI understanding**

---

### Where I AGREE with Vercel

#### ✅ **Declarative > Imperative**
- **My experience**: Editing presentation.json (declarative) was clearer than editing HTML (imperative)
- **Why it works**: Describes *what* you want, not *how* to do it
- **Evidence**: I immediately understood the JSON structure, but got confused by HTML regeneration

#### ✅ **Single Source of Truth**
- **My experience**: Editing 3 files caused sync issues
- **Why it works**: One file to edit, automation handles the rest
- **Evidence**: After switching to presentation.json-only edits, everything stayed in sync

#### ✅ **Clear Documentation Matters**
- **My experience**: Existing AGENTS.md helped me understand the project quickly
- **Why it works**: Context is established once, not repeated every conversation
- **Evidence**: I understood the pedagogical principles from Section 1 immediately

---

### Where I'm SKEPTICAL of Vercel's Claims

#### ⚠️ **"agents.md outperforms skills"**
- **The claim**: Markdown files are inherently better than code
- **My analysis**: The benefit comes from **CLARITY**, not format
- **Counter-example**: A well-documented Python skill with clear comments would work just as well
- **Real insight**: It's about **good documentation**, not Markdown vs. code

#### ⚠️ **"Faster response times"**
- **The claim**: Simpler architecture = faster AI
- **My analysis**: The speed gain is from **less back-and-forth**, not processing time
- **Real bottleneck**: Human workflow (editing multiple files), not AI processing
- **Evidence**: My slowness came from manual edits, not AI thinking time

#### ⚠️ **"Lower token usage"**
- **The claim**: Less code = fewer tokens
- **My analysis**: Token savings are minimal compared to workflow improvements
- **Real benefit**: **Fewer mistakes** requiring correction, not fewer tokens
- **Evidence**: I used more tokens fixing multi-file edit mistakes than single-file edits

---

### What ACTUALLY Made the Difference Today

#### The Real Breakthrough:
```powershell
# Before: Manual multi-file edits (SLOW, ERROR-PRONE)
1. Edit dist/.../index.html
2. Edit inputs/.../published/index.html  
3. Edit inputs/.../presentation.json
4. Hope they stay in sync

# After: Single source + automation (FAST, RELIABLE)
1. Edit presentation.json
2. Run: python scripts/fast_edit.py <lesson>
3. Done - all files updated automatically
```

#### Why This Worked:
1. **Clear workflow** - I knew exactly what to do
2. **Automation** - No manual sync required
3. **Single responsibility** - One file to rule them all
4. **Fast feedback** - See results in 30 seconds

---

### My Honest Conclusion

#### I AGREE with the recommendation, but for different reasons:

**Vercel says**: "agents.md is better because it's declarative and uses fewer tokens"

**I say**: "Clear documentation + single source of truth + automation is better regardless of format"

#### The Real Lessons:

1. **✅ Documentation clarity matters more than format**
   - Could be Markdown, could be well-commented Python
   - What matters: Clear instructions, examples, context

2. **✅ Single source of truth eliminates sync errors**
   - presentation.json works because it's THE source
   - HTML is derived, not co-edited

3. **✅ Automation reduces human error**
   - fast_edit.py removes manual steps
   - Scripts don't forget to update files

4. **⚠️ Format is secondary to clarity**
   - Markdown is nice, but not magic
   - A clear Python docstring works too

---

### My Recommendation (Refined)

**YES, implement AGENTS.md enhancement**, but focus on:

1. **Clear workflows** (not just format)
2. **Single source patterns** (not just declarative syntax)
3. **Automation scripts** (not just documentation)
4. **Examples and troubleshooting** (not just theory)

The benefit comes from **good systems thinking**, not Markdown specifically.

---

### Critical Success Factors

For this to work, you need:

| Factor | Why It Matters | Current State |
|--------|----------------|---------------|
| **Clear documentation** | AI understands context | ✅ AGENTS.md exists |
| **Single source of truth** | No sync errors | ✅ presentation.json |
| **Automation scripts** | Remove manual steps | ✅ fast_edit.py created |
| **Explicit workflows** | Know what to do | ⚠️ Needs enhancement |
| **Troubleshooting guide** | Recover from errors | ❌ Missing |

---

### Final Verdict

**I agree with the CONCLUSION (implement AGENTS.md) but not all the REASONING.**

The benefit isn't about Markdown vs. code or token savings. It's about:
- Clear documentation
- Single source of truth
- Automated workflows
- Reducing human error

**These principles work regardless of the specific format.**