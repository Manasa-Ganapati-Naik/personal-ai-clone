# Personal AI Clone — Sprint 1 

## Overview
Personal AI Clone is a personalized conversational text generator that adapts to a user's unique style, providing draft messages and suggestions.

## Sprint 1 Deliverables
- `research/lit_review.md`
- `docs/requirements.md`
- `data_plan/data_collection_plan.md`
- `docs/ethics_privacy.md`
- `docs/architecture.png`
- `docs/evaluation.md`
- `docs/sprint1_report.pdf` (final)

## How to Run Dev (Backend)
```bash

python3 -m venv .venv



.venv\Scripts\Activate.ps1

source .venv/bin/activate


pip install -r backend/requirements.txt


uvicorn backend.app:app --reload

**# Personal AI Clone — Sprint 2 Summary**


## Overview
This sprint focused on fine-tuning a personalized AI model, building a minimal inference API, adding a demo frontend, implementing basic safety filters, and documenting the workflow.

---

## Key Tasks & Workflow

### 1. Dataset Preparation
- Cleaned and preprocessed user text data.
- Created JSONL training and validation sets:
  - `data/processed/user_corpus.jsonl`
  - `data/processed/user_corpus_val.jsonl`
- Tokenized dataset and inspected statistics.

**Files:**
- `scripts/preprocess.py`
- `notebooks/data_preprocessing.ipynb`
- `data/processed/*.jsonl`

---

### 2. Model Training
- Fine-tuned GPT-2 using LoRA adapters (PEFT).
- Small proof-of-concept run to validate training pipeline.
- Saved model and adapters to `models/user_clone/`.

**Files:**
- `training/train.py`
- `logs/train_run_YYYYMMDD.txt`
- `docs/loss_plots.png`

---

### 3. Model Evaluation
- Documented dataset size, hyperparameters, training/validation loss.
- Generated inference examples and computed metrics:
  - Perplexity
  - Embedding similarity (SBERT)


**Files:**
- `docs/training_report.md`

---

### 4. Model Serving (FastAPI)
- Created endpoint `/generate` for infere


**Files created/updated:**

- `backend/safety.py`
- Updates in `backend/model_server.py` to use safety filters


