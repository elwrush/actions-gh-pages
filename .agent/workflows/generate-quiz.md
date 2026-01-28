---
description: Initiates the multi-stage quiz generation process using Questgen.ai logic.
---
# Generate Quiz Workflow

1.  **Activate Skill**: Load [generating-quizzes/SKILL.md](file:///c:/PROJECTS/LESSONS%20AND%20SLIDESHOWS%202/skills/generating-quizzes/SKILL.md).
2.  **Define Blueprint**: Present the enumerated menu for CEFR level, quantity, types, and Bloom's levels.
3.  **Generate Key**: Create a randomized answer index list.
4.  **Execute Multi-Stage Logic**:
    -   Stage 1: Extract Assessment Anchors.
    -   Stage 2: Generate Questions matched to the Randomized Key.
5.  **Validate**: Run `python scripts/validate_quiz.py`.
6.  **Human Audit**: Present for subjective validation.
