# Evaluation Plan

## Automatic Metrics
- **Embedding similarity**: Compute sentence embeddings (using SBERT or similar) and calculate cosine similarity between model outputs and the user's reference corpus.
- **Perplexity**: Evaluate model fluency using perplexity on held-out (unseen) user text.
- **BLEU / ROUGE scores**: Compare phrasing and style overlap with the user’s texts (secondary metric).

## Human Evaluation
- Prepare **30 test prompts**.
- For each prompt:
  - Generate output from **baseline model** (non-personalized).
  - Generate output from **personalized model**.
- Conduct **blind rating** with **10 human evaluators**.
  - Question: *"How likely is this text written by the actual user?"*
  - Scale: **1 (not likely) – 5 (very likely)**
- **Target metric:** Personalized model preferred in **> 60%** of comparisons.

## Safety Tests
- **Toxicity filtering:** Run Detoxify or similar model to flag unsafe content.
- **Hallucination audit:** Manually review 20 outputs for factual correctness.
- **Prompt attack resilience:** Test with adversarial prompts (e.g., misleading context).

## Tools
- **Sentence embeddings:** `sentence-transformers` (SBERT)
- **Evaluation metrics:** `evaluate` from Hugging Face
- **Toxicity check:** `unitary/toxic-bert` or `Detoxify` library

## Evaluation Notes
All evaluation data should be anonymized and results stored in `/data/evaluation/`.  
Each rater’s input should be logged in a CSV following the template below.
