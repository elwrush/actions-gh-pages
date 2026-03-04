# Alignment Audit: Frankenstein Presentation

## 1. TEMPLATE → TASK ALIGNMENT

| Task | Source Task | Planned Layout | Current Layout | Status |
|:---|:---|:---|:---|:---|
| Task 1: Genre | "Before you read" | `split_table` | `split_table` | ✅ Aligned |
| Task 2: Mary's Life | "Who is Mary?" (implied) | `split_table` | `split_table` | ✅ Aligned |
| Task 3: Sequencing | "Sequence" (5 items) | `ranking` | `ranking` | ⚠️ See Issue #1 |
| Task 4: Flaws | "Flaws" (Page 147) | `split_table` | `split_table` | ⚠️ See Issue #2 |
| Task 5: Themes | "Themes" (Page 147) | `split_table` | `split_table` | ⚠️ See Issue #2 |

## 2. SOURCE → JSON VERBATIM ALIGNMENT

### Task 1 (Genre) ✅
| Field | SOURCE_TEXT.md | JSON | Match |
|:---|:---|:---|:---|
| Answer | "classic horror story, early science fiction" | "Classic horror story & Early science fiction" | ✅ |
| Evidence | [Intro Para 3] | [Intro Para 3] | ✅ |

### Task 2 (Mary's Life) ✅
| Field | SOURCE_TEXT.md | JSON | Match |
|:---|:---|:---|:---|
| Answer | London & Geneva | "Born in London / Geneva in 1816" | ✅ |
| Evidence | [Para 1-2] | [Para 1] [Para 2] | ✅ |

### Task 3 (Sequence) ⚠️ ISSUE
| Field | SOURCE_TEXT.md | JSON | Match |
|:---|:---|:---|:---|
| Items | 6 items (e-d-b-a-f-c) | 6 items (A-F) | ⚠️ |
| Order | 1=e, 2=d, 3=b, 4=a, 5=f, 6=c | F→E→D→A→B→C | ⚠️ |

**Issue #1**: SOURCE_TEXT.md uses letters (e, d, b, a, f, c) but JSON uses different labels. Need to verify mapping.

### Task 3 Items Mapping (NEEDS VERIFICATION):
```
SOURCE_TEXT.md:
1. e (Professor Waldman)
2. d (learns about death)
3. b (given laboratory/mast)
4. a (works hard/machine)
5. f (electricity brings to life)
6. c (scared/wakes up)

JSON:
A. The machine started to work
B. He saw the huge creature's yellow eyes
C. Victor ran away in fear
D. He worked for two years without a holiday
E. Victor went to visit Professor Waldman
F. Victor's mother died

ORDER GIVEN: F -> E -> D -> A -> B -> C
```

**PROBLEM**: "Victor's mother died" is NOT in SOURCE_TEXT.md! This is a HALLUCINATION.

### Task 4 (Flaws) ⚠️ ISSUE
| Field | SOURCE_TEXT.md | JSON | Match |
|:---|:---|:---|:---|
| Answers | irresponsible, obsessive, reckless | Obsessive, Irresponsible, Reckless | ✅ |
| Evidence | [Page 147 Literary Strategy] | [Page 147 Literary Strategy] | ✅ |

**Issue #2**: `split_table` layout doesn't match the task type. This is a CHECKLIST task, should use `checklist` layout.

### Task 5 (Themes) ⚠️ ISSUE
| Field | SOURCE_TEXT.md | JSON | Match |
|:---|:---|:---|:---|
| Answers | "dangerous and forbidden knowledge", "morals and distinguishing right from wrong" | "Dangerous Knowledge & Morality" | ✅ |
| Evidence | [Page 147 Literature] | [Page 147 Literature] | ✅ |

**Issue #2**: Same as Task 4 - should use `checklist` layout for selection tasks.

## 3. VOCABULARY ALIGNMENT

| Source Vocab | JSON Vocab | Match |
|:---|:---|:---|
| promising | ❌ Missing | ⚠️ |
| how life begins | ❌ Missing | ⚠️ |
| isolated | ❌ Missing | ⚠️ |
| a storm | ❌ Missing | ⚠️ |
| fear | ❌ Missing | ⚠️ |
| mast | ✅ Present | ✅ |
| awful | ✅ Present | ✅ |
| irresponsible | ✅ Present | ✅ |
| obsessive | ✅ Present | ✅ |
| reckless | ✅ Present | ✅ |

**Issue #3**: JSON has 5 vocab items (mast, awful, irresponsible, obsessive, reckless) but SOURCE_TEXT.md lists 5 DIFFERENT items (promising, how life begins, isolated, a storm, fear).

This suggests vocab was sourced from a DIFFERENT task (Page 147 analysis words) vs the cloze task (Task 3 Page 144).

## 4. CRITICAL ISSUES SUMMARY

| # | Issue | Severity | Action |
|:---|:---|:---|:---|
| 1 | Task 3 item F "Mother died" is HALLUCINATED - not in SOURCE_TEXT.md | 🔴 Critical | Remove or verify |
| 2 | Tasks 4 & 5 use wrong layout (`split_table` vs `checklist`) | 🟡 Medium | Change layout |
| 3 | Vocab mismatch - JSON has Page 147 words, not Task 3 cloze words | 🟡 Medium | Clarify with user |
| 4 | Task 3 evidence is vague | 🟢 Low | Add specific paragraph refs |

## 5. TEMPLATE COVERAGE CHECK

Available templates:
- ✅ `title` - Used
- ✅ `schema_activation` - Used
- ✅ `mission` - Used
- ✅ `segue` - Used (4x)
- ✅ `strategy` - Used (5x)
- ✅ `split_table` - Used (3x)
- ✅ `ranking` - Used (1x)
- ✅ `answer_detail` - Used (5x)
- ✅ `vocab` - Used (5x)
- ❌ `checklist` - NOT used (should be for Tasks 4-5)

## 6. RECOMMENDATION

Before refactoring, clarify:
1. **Which vocab set?** Cloze (promising/isolated/etc) OR Character analysis (mast/awful/etc)?
2. **Task 3 correct items?** The current item F ("mother died") is hallucinated.

---

*Audit completed. Skill loaded: creating-html-presentation*
