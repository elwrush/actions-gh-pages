# Universal Quiz JSON Schema

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "tasks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "task_type": { 
            "type": "string",
            "enum": ["antecedent", "mcq", "boolean", "vocab", "inference", "short_answer", "gapfill", "matching", "error_correction", "reordering", "faq", "paraphrase"]
          },
          "instructions": { "type": "string" },
          "questions": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "query": { "type": "string" },
                "choices": { "type": "array", "items": { "type": "string" } },
                "answer": { "type": ["integer", "string", "array"] },
                "bloom_level": { 
                  "type": "string", 
                  "enum": ["Remembering", "Understanding", "Applying", "Analyzing", "Evaluating", "Creating"] 
                },
                "explanation": { "type": "string" },
                "anchor_text": { "type": "string" },
                "target_text": { "type": "string" },
                "pairs": { "type": "array", "items": { "type": "object" } }
              },
              "required": ["query", "answer", "explanation", "bloom_level", "anchor_text"]
            }
          }
        },
        "required": ["task_type", "instructions", "questions"]
      }
    }
  },
  "required": ["tasks"]
}
```

# Questgen Multi-Stage Prompt Logic

To generate high-quality questions, follow this internal reasoning process:

## Stage 1: Assessment Anchoring
Identify key sentences in the text that contain high-value information. These are your "Anchors".
*   **Prompt**: "Extract 5-10 key sentences from the text that represent central facts, relationships, or inferences. For each, identify a 'Keyword' or 'Concept' that could be the target of a question."

## Stage 2: Randomized Answer Key
Generate a random list of integers (0-3) corresponding to the number of questions.
*   **Example**: For 5 questions, the key might be `[1, 3, 0, 2, 1]`.
*   **Purpose**: This ensures the correct answer is moved to a random position *before* the prompt is finalized, avoiding AI bias toward option 'C'.

## Stage 3: Question & Distractor Generation
For each Anchor, generate a question aligned with a specific Bloom's level, matching the `answer` index to the **Randomized Answer Key**.
*   **MCQ Logic**:
    1.  **Stem**: The question query.
    2.  **Key**: The correct answer (grounded in the anchor, placed at the index specified by the key).
    3.  **Distractors**: 3 plausible but incorrect options. Use 'Sense2vec' style logic: distractors should be members of the same semantic class as the key.
    4.  **Pedagogical Feedback**: Explain *why* the correct answer is correct and *why* each distractor is incorrect based *only* on the text provided.

## Stage 4: Human Subjective Validation
Before finalizing, analyze the quiz using the following criteria:
1.  **Distractor Plausibility**: Are they "clean"? No grammatical giveaways or obvious falsehoods that don't require context to solve.
2.  **CEFR Alignment**: Does the vocabulary match the target level without being too archaic or simple?
3.  **Narrative Flow**: Does the sequence of questions follow the logical progression of the text?
4.  **Paper Trail**: Is every "correct" answer definitively provable using the provided text?

# Question Type Definitions

| Type | Description | Key Properties |
| :--- | :--- | :--- |
| **mcq** | Standard 4-option multiple choice. | `choices` (4 strings), `answer` (0-3). |
| **boolean** | True/False or Yes/No. | `choices` (["True", "False"]), `answer` (0 or 1). |
| **faq** | Frequently Asked Questions style. | `query` (Question), `answer` (Concise answer from text). |
| **paraphrase** | Identify the best paraphrase of a sentence. | `query` (Original), `choices` (Paraphrases), `answer`. |
| **vocab** | Word meaning or synonym. | `query` (context sentence), `choices`, `answer`. |
| **inference** | Implied meaning/author intent. | `query`, `choices`, `answer`, `explanation`. |
| **gapfill** | Grammatical or lexical cloze. | `query` (with `___`), `answer`. |
| **matching** | Definitions to words. | `pairs` (list of {A: "word", B: "def"}). |
