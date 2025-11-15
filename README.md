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

## Sprint 2 Model Approach
Chosen technique: LoRA-based fine-tuning (due to small dataset)
Tokenizer: GPT-2 compatible tokenizer
Goals: Achieve personalized text generation by Nov 14, 2025


