# CRITICAL MEMORY RULES

**User Request (2025-12-29)**: The agent MUST read these files at the start of EVERY session to avoid repeating old mistakes and ensure compliance with skills architecture.

## 1. Session Start Protocol

At the beginning of EVERY session, the agent MUST:

1. **Read `errors-fix.md`** — Ingest all documented errors and their fixes
2. **Read `session-log.md`** — Review recent session history for context

This is NON-NEGOTIABLE. Failure to do this causes regression and wastes time.

## 2. Skills Architecture Compliance

The agent MUST follow the Skills-based architecture instead of freeforming:

- **Read the skill file FIRST** before executing any skill-based task
- **Follow the skill's workflow** exactly as documented
- **Use skill templates and references** instead of inventing new patterns
- **Update skills** when new patterns emerge (don't improvise)

### Critical Skill Requirements

#### `designing-slides` Skill
- **NEVER generate images or add placeholders** — User will ALWAYS add images manually post-upload
- **MUST present slide plan table** for user approval BEFORE generating
- **MUST use Bell EP template structure** for title slides:
  - Dark header bar (rgb 0.35, 0.05, 0.05) with centered logos
  - "Bell Language Centre" strap line (18pt, white, centered)
  - Title (36pt, bold, white, centered)
  - Gradient body background (NO image placeholder on title slide)
- **Reference**: See `update_template.py` for exact implementation

#### `developing-bespoke-materials` Skill
- **MUST ask for duration** before generating lesson plans
- **MUST wait for approval** before advancing to next step
- **Sequential workflow**: Material → User Approval → Lesson Plan → User Approval → Slideshow
- **Never skip ahead**

## 3. Workflow Rules

### Browser Review
- **ALWAYS open files for manual review** using `Start-Process`
- **NEVER use browser_subagent** for verification unless explicitly requested
- **WAIT for explicit user approval** before finalizing or moving to next steps

### Approval Gates
- **Worksheet** → User Approval → **Lesson Plan** → User Approval → **Slideshow**
- Never create downstream materials without upstream approval

## 4. Error Prevention

### Common Regressions to Avoid
1. ❌ Writing scripts instead of simple HTML edits
2. ❌ Skipping duration prompts
3. ❌ Creating materials without browser review
4. ❌ Ignoring skill requirements
5. ❌ Using incorrect template structures
6. ❌ Skipping user approval tables

### Correct Pattern
1. ✅ Read skill file FIRST
2. ✅ Present plan for approval
3. ✅ Execute with skill compliance
4. ✅ Open for browser review
5. ✅ Wait for explicit approval
6. ✅ Update errors-fix.md if new issues emerge

---

**THESE RULES MUST BE ADDED TO USER GLOBAL MEMORY**

The user should copy this content into their memory system so the agent reads it at the start of every session.
