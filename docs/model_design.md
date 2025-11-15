# Model Design — Personal AI Clone
Author: Manasa Ganapati Naik
Section: C
Degree: Master's in Data Science and Business Management
Sprint: 2 (Nov 1 – Nov 14, 2025)

## Chosen Approach
Approach: LoRA-based parameter-efficient fine-tuning  
Rationale:
- Current dataset size is small: ~630 tokens (87 examples)
- Limited personal data initially available
- Efficient on small GPUs or Google Colab
- Lower risk of overfitting vs full fine-tuning

## Base Model & Tools
- Base Model: distilgpt2 (lighter & faster than GPT-2 small)
- Frameworks: Hugging Face Transformers + PEFT
- Tokenizer: GPT-2 compatible tokenizer
- Training Strategy: LoRA adapter layers on attention modules
- Deployment: FastAPI-based backend for text generation

## Data Strategy
- Format: JSONL, text-only
- Initial data from synthetic corpora
- Additional data via:
  - Automated style augmentation
  - Retrieval-augmented examples
- Min target tokens for Sprint 2 model: ≥ 5,000 tokens
- PII removal ensured before training

## Training Parameters (initial)
- Batch size: 4
- Max length: 128 tokens
- Epochs: 3–5
- Learning rate: 2e-4
- Evaluation every 200 steps
- Early stopping if val loss increases

## Inference & Serving
- FastAPI endpoint: `/generate`
- Editable output before sending
- Logging of prompts only in dev mode (for evaluation)

## Evaluation Plan
- Automated: Perplexity, embedding similarity (SBERT)
- Human: A/B testing with ~15 prompts
- Safety: Toxicity test before response display

## Risks & Mitigation
| Risk | Mitigation |
|------|------------|
| Low dataset size | Use LoRA + augmentation + RAG |
| Style mismatch | Target specific domains of writing |
| Privacy | Consent & anonymization before processing |

## Next Steps for Sprint 2
1. Expand dataset to ≥ 5k tokens
2. Preprocess and tokenize dataset
3. Implement LoRA training script
4. Model server endpoint with safety checks
5. Evaluation and demo
