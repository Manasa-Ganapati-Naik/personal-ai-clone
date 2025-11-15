# scripts/count_tokens.py
import os, json
from transformers import AutoTokenizer

raw_dir = "data/raw"
tokenizer = AutoTokenizer.from_pretrained("gpt2")

total_tokens = 0
total_chars = 0
file_count = 0
examples = 0

for fname in os.listdir(raw_dir):
    path = os.path.join(raw_dir, fname)
    if os.path.isfile(path):
        file_count += 1
        with open(path, "r", encoding="utf8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                examples += 1
                toks = tokenizer(line).input_ids
                total_tokens += len(toks)
                total_chars += len(line)

print(f"Files scanned: {file_count}")
print(f"Text examples: {examples}")
print(f"Total tokens (approx): {total_tokens}")
print(f"Avg tokens per example: {total_tokens/examples if examples else 0:.2f}")
print(f"Total chars: {total_chars}")
