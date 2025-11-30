# Personal AI Clone — Sprint 3 Report

**Author:** Manasa Ganapati Naik  
**Section:** C  
**Timeline:** Nov 15 – Nov 28, 2025  

## Overview
Sprint 3 focused on improving the personalized AI model’s performance, adding advanced features, integrating with a UI, performing safety & evaluation enhancements, and preparing deliverables for submission.

---

## Key Tasks & Workflow

### 1. Dataset Expansion & Augmentation
- Added new user conversation data (approved only).
- Performed text normalization and augmentation (paraphrasing, synonyms).
- Re-generated JSONL datasets for training and validation.

**Files:**
- `data/processed/user_corpus_aug.jsonl`
- `data/processed/user_corpus_val_aug.jsonl`

---

### 2. Model Enhancements
- Fine-tuned the LoRA adapter with augmented dataset.
- Tested different hyperparameters for improved perplexity and output diversity.
- Saved updated model to `models/user_clone_v2/`.

**Files:**
- `training/train_v2.py`
- `logs/train_run_v2_YYYYMMDD.txt`

---

### 3. Advanced Evaluation
- Compared baseline GPT-2 vs personalized LoRA model.
- Computed embedding similarity using SBERT for 30 prompts.
- Conducted human evaluation with 3 reviewers on 15 prompt pairs.
- Recorded results in `docs/eval_examples_v2.md`.

**Files:**
- `docs/eval_examples_v2.md`

---

### 4. Frontend Integration
- Updated `ui.html` to interact with new model version.
- Added user-friendly controls:
  - Max tokens
  - Temperature slider
- Configured CORS and proxy settings for local testing.

**Local UI URL:**  
- [http://127.0.0.1:3000/ui.html](http://127.0.0.1:3000/ui.html)

**Files:**
- `frontend/ui.html`


---

### 5. Safety & Guardrails
- Enhanced toxicity checks with updated Detoxify thresholds.
- Logged all generated outputs securely in encrypted audit logs.
- Ensured human-in-the-loop mechanism for sensitive outputs.

**Files:**
- `backend/safety.py` (updated)
- `backend/model_server.py` (integrated safety features)

---

### 6. Documentation & Reports
- Updated training report with:
  - New dataset stats (#examples, #tokens)
  - Updated hyperparameters
  - Training/validation loss graphs
  - Sample outputs and evaluation metrics

**Files:**
- `docs/training_report_v2.md`


---

### 7. Final Deliverables
- All model files saved to `models/user_clone_v2/`.
- Committed frontend, backend, and documentation.
- Tagged release for Sprint 3:  
  ```bash
  git tag -a sprint3 -m "Sprint 3 complete: model improvements & frontend integration"
  git push origin sprint3 --tags
