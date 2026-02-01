# Slide Architecture: B1 Pronunciation (Intensive)

**Source**: `inputs/31-01-2026-Pronunciation-Bell/31-01-2026-Pronunciation-Bell.typ`
**Theme**: `thai-heritage.css` (Academic Gold Standard)

## 🗺️ Learning Journey Map

| Slide | Layout | Content / Purpose | Bridge? |
| :--- | :--- | :--- | :--- |
| 1 | `title` | **PRONUNCIATION** | No |
| 2 | `strategy` | **THE MISSION**: Why sound symbols matter for B1 PET. | **YES** |
| 3 | `strategy` | **BRIDGE**: Navigating the Code (Intro to IPA). | **YES** |
| 4 | `split_table` | **PHONEMIC CHART**: Consonants Reference. | No |
| 5 | `split_table` | **PHONEMIC CHART**: Vowels & Diphthongs Reference. | No |
| 6 | `strategy` | **BRIDGE**: The Transcription Challenge. | **YES** |
| 7 | `split_table` | **TASK 1**: Sentences 1-4 (Tom, Jane, Sue, Joe). | No |
| 8 | `split_table` | **TASK 1**: Sentences 5-8 (Liz, Paul, Tom/Liz, Joe). | No |
| 9 | `answer` | **TASK 1 ANSWERS**. | No |
| 10 | `strategy` | **BRIDGE**: Spotting the Difference (/ɒ/, /ɔː/, /əʊ/). | **YES** |
| 11 | `split_table` | **TASK 2**: Listen and Tick (10 items). | No |
| 12 | `answer` | **TASK 2 ANSWERS**. | No |
| 13 | `strategy` | **BRIDGE**: Categorization Speed Run. | **YES** |
| 14 | `split_table` | **TASK 3**: Word Sorting Box. | No |
| 15 | `answer` | **TASK 3 ANSWERS**. | No |

## 🏗️ Layout Gap Analysis
*   **Phonemic Chart**: Will use `split_table` with a dense HTML `<table>`. This fits the current library.
*   **Transcription**: Standard `split_table` with numbering.
*   **Vignette Requirement**: I will apply `data-background-gradient` to the Mission slide to ensure readability.

## 📦 Asset Strategy
*   `assets/hero_pron.jpg`: Title/Mission background.
*   `assets/characters.png`: Task 1 visual.
*   `assets/fox-cock.png`, `assets/forks-cork.png`, `assets/folks-coke.png`: Task 2 visuals.
