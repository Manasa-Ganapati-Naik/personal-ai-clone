# Personal AI Clone — Sprint 1 Complete

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

Personal AI Clone — Sprint 2 Summary

Key Steps & Files
1. Data Preparation
Cleaned, normalized, and split user corpus into train/validation sets.

Files: data/processed/user_corpus.jsonl, data/processed/user_corpus_val.jsonl, scripts/preprocess.py, notebooks/data_preprocessing.ipynb

2. Tokenization & Stats
Tokenized dataset, inspected example count, average tokens, and vocab issues.

Files: notebooks/data_preprocessing.ipynb

3. Training Setup
Fine-tuning approach: LoRA + 8-bit (small dataset)

Files: training/train.py

4. Training Run
Short proof-of-concept run to validate pipeline

Saved logs and loss plots
Files: logs/train_run_YYYYMMDD.txt, docs/loss_plots.png

5. Inference API
FastAPI server exposing /generate
Tested with demo client
Local URL: Swagger Docs

Files: backend/model_server.py, demo/generate_sample.py

6. Frontend Demo
Simple UI to send prompts and display outputs
Local URL: Demo UI

Files: frontend/ui.html

7. Safety & Guardrails
Toxicity filtering and human-in-the-loop
Logging of prompts and outputs securely

Files: backend/safety.py, updates in backend/model_server.py


