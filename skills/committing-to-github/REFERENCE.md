# Git Commands Reference

Quick reference for common git operations.

## Status and Inspection

```bash
# Check current status
git status

# View commit history
git log --oneline

# Show current branch
git branch --show-current

# List all branches
git branch -a
```

## Staging

```bash
# Stage specific file
git add <file>

# Stage all changes
git add .

# Stage all files of a type
git add *.md

# Unstage file
git restore --staged <file>
```

## Committing

```bash
# Commit with message
git commit -m "feat: add new feature"

# Commit with detailed message
git commit -m "feat: add new feature" -m "Detailed description here"

# Amend last commit
git commit --amend -m "Updated message"
```

## Pushing and Pulling

```bash
# Push to remote
git push origin <branch>

# Push and set upstream (first time)
git push -u origin <branch>

# Pull latest changes
git pull origin <branch>

# Force push (use with caution)
git push --force origin <branch>
```

## Branching

```bash
# Create new branch
git branch <branch-name>

# Switch to branch
git checkout <branch-name>

# Create and switch
git checkout -b <branch-name>

# Delete branch
git branch -d <branch-name>
```

## Remote Management

```bash
# View remotes
git remote -v

# Add remote
git remote add origin <url>

# Change remote URL
git remote set-url origin <new-url>
```

## Removing Files

```bash
# Remove from git but keep local
git rm --cached <file>

# Remove all desktop.ini files from tracking
git rm --cached **/desktop.ini
git commit -m "chore: remove desktop.ini from tracking"
```

## .gitignore Patterns

```gitignore
# Specific file
desktop.ini

# All desktop.ini in subdirectories
**/desktop.ini

# All files with extension
*.log
*.tmp

# Entire directory
node_modules/
.venv/

# Everything in directory except one file
folder/*
!folder/important.txt
```

## Commit Message Conventions

### Format
```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types
- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation only
- **style**: Formatting, missing semicolons, etc.
- **refactor**: Code change that neither fixes a bug nor adds a feature
- **test**: Adding missing tests
- **chore**: Updating build tasks, package manager configs, etc.

### Examples
```bash
git commit -m "feat: add lesson planning skill"
git commit -m "fix: correct phonemic script formatting"
git commit -m "docs: update README with installation steps"
git commit -m "chore: update .gitignore for desktop.ini files"
```
