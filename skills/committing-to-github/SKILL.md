---
name: committing-to-github
description: >
  Git workflow for staging, committing, and pushing changes to GitHub.
  Automatically handles desktop.ini files from Google Drive sync.
---

# Committing to GitHub

Interactive workflow for committing and pushing code to a GitHub repository.

## Prerequisites

- Git installed and configured
- GitHub repository initialized or cloned
- Remote repository URL configured

## Workflow

### Step 1: Check Status and .gitignore

1. Run `git status` to see current changes
2. Check if `.gitignore` exists
3. If not, or if `desktop.ini` not ignored, update `.gitignore`:
   ```
   # Google Drive sync files
   desktop.ini
   **/desktop.ini
   ```

### Step 2: Review Changes

Present changes to user:
- **Untracked files** (new files)
- **Modified files** (changed files)
- **Deleted files**

Ask user which files to stage, or suggest staging all non-ignored files.

### Step 3: Stage Files

Execute staging commands:
```bash
git add <file1> <file2> ...
# or
git add .
```

Confirm staged changes with `git status`.

### Step 4: Commit

Ask user for commit message. Suggest format:
```
<type>: <subject>

<body (optional)>
```

**Common types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `refactor`: Code restructuring
- `chore`: Maintenance tasks

Execute: `git commit -m "message"`

### Step 5: Push to Remote

1. Check current branch: `git branch --show-current`
2. Execute: `git push origin <branch>`
3. If first push on new branch: `git push -u origin <branch>`

### Step 6: Confirm Success

Display push confirmation and provide GitHub URL if available.

---

## Common Issues

### desktop.ini keeps appearing
- **Solution**: Already in .gitignore, run `git rm --cached **/desktop.ini` to remove from tracking

### Merge conflicts
- **Solution**: User must resolve manually, not handled by this skill

### Authentication required
- **Solution**: User must configure Git credentials or SSH keys

---

## Reference

See [REFERENCE.md](REFERENCE.md) for detailed git commands.
