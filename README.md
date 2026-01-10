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

# Personal AI Clone — Sprint 2 Report

## Title Page
**Project:** Personal AI Clone  
**Author:** Manasa Ganapati Naik  
**Section:** C
**Dates:** Nov 01 – Nov 14, 2025

### Tasks
- Decide fine-tuning approach depending on data size:
  - Plenty of text (≥50k tokens): full fine-tuning (GPT-2 small / distil-GPT2) or LLaMA-like checkpoint
  - Limited data (<50k tokens): LoRA / adapter tuning + prompt engineering
  - Very small data: RAG + prompt templates
- Decide model provider: Local (Hugging Face + PyTorch) or hosted API (OpenAI)
- Create `docs/model_design.md` explaining chosen method + rationale


**Tasks:**

- Prepare backend and training environments
- Add required packages in:
  - `backend/requirements.txt`
  - `training/requirements.txt`
- Create virtual environment and install dependencies

**Files created/updated:**

- `backend/requirements.txt`
- `training/requirements.txt`
- `.venv/` folder (local virtual environment)

**Tasks:**

- Load only approved raw data (do NOT commit raw files)
- Normalize text and remove PII
- Split dialogs/messages into prompt→response pairs
- Create JSONL training examples
- Shuffle and split into train/validation sets
- Save processed data to:
  - `data/processed/user_corpus.jsonl`
  - `data/processed/user_corpus_val.jsonl`

**Files created/updated:**

- `scripts/preprocess.py`
- `notebooks/data_preprocessing.ipynb`
- `data/processed/user_corpus.jsonl`
- `data/processed/user_corpus_val.jsonl`

**Tasks:**

- Tokenize dataset using selected tokenizer
- Inspect dataset statistics:
  - Number of examples
  - Average tokens per example
  - Vocabulary issues
- Concatenate messages if average tokens per example is too small

**Files created/updated:**

- `notebooks/data_preprocessing.ipynb` (updated with tokenization and stats)


**Tasks:**

- Choose training method:
  - Recommended: LoRA + 8-bit training for small datasets
- Prepare small proof-of-concept training run
- Adjust hyperparameters for hardware constraints

**Files created/updated:**

- `training/train.py`

**Tasks:**

- Run training on a small dataset to validate pipeline
- Monitor logs for errors; reduce batch size if necessary
- Save logs and loss/validation loss plots:
  - `logs/train_run_YYYYMMDD.txt`
  - `docs/loss_plots.png` (or any chart format)
- Create reproducible `requirements.txt`

**Files created/updated:**

- `logs/train_run_YYYYMMDD.txt`
- `docs/` (plots and documentation)

**Tasks:**

- Document dataset size (#examples, #tokens)
- Record hyperparameters and training/validation loss
- Generate inference examples
- Compute metrics:
  - Perplexity
  - Embedding similarity (SBERT)
  - Human-rated evaluation (if possible)

**Files created/updated:**

- `docs/training_report.md`


**Tasks:**

- Save final model to `models/user_clone/`
  - If using LoRA, save base model and adapters
- Optionally upload to Hugging Face Hub (private repo)
- Ensure folder contains all necessary files:
  - `config.json`
  - `pytorch_model.bin`
  - Adapter files (if using PEFT/LoRA)

**Files created/updated:**

- `models/user_clone/` (all model files)


**Tasks:**

- Create FastAPI server to serve the model
- Load tokenizer and model
- Expose endpoint `/generate` for inference
- Test server with demo client
- Handle CPU/GPU device 


**Local URLs for reference:**

- Swagger API docs: [FastAPI Docs](http://127.0.0.1:8000/docs#/default/generate_generate_post)

**Files created/updated:**

- `backend/model_server.py`
- `demo/generate_sample.py`


**Tasks:**

- Create small UI (React or HTML) to send requests to `/generate`
- Handle prompt input and display generated output
- Configure proxy if frontend/backend run on same host

**Frontend Demo URL (local server):**

- [Demo UI](http://127.0.0.1:3000/ui.html)


**Files created/updated:**

- `frontend/src/App.jsx` (or `frontend/ui.html` if simple HTML)


## Day K — Safety & Guardrails (Nov 11)

**Tasks:**

- Add output filtering pipeline (toxicity check)
- Implement human-in-the-loop for text approval
- Log prompts and outputs securely (do NOT commit logs to VCS)
- Integrate safety functions into inference API

**Files created/updated:**

- `backend/safety.py`
- Updates in `backend/model_server.py` to use safety filters


