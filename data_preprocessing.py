import os

raw_path = "data/raw"
files = os.listdir(raw_path)
files


for fname in files:
    with open(os.path.join(raw_path, fname), 'r', encoding='utf8') as f:
        lines = f.readlines()
    print(f"--- {fname} ---")
    print(lines[:5])

from html import unescape
import re

def normalize(text):
    text = unescape(text)  # convert HTML entities
    text = re.sub(r'\s+', ' ', text).strip()  # remove extra spaces/newlines
    return text

import re

def remove_emails(text):
    return re.sub(r'\b[\w\.-]+?@\w+\.\w+?\b', '<EMAIL>', text)

def remove_phones(text):
    return re.sub(r'\b(\+?\d[\d \-]{7,}\d)\b', '<PHONE>', text)

def clean_text(text):
    text = normalize(text)
    text = remove_emails(text)
    text = remove_phones(text)
    return text

import json, os

def process_file(path):
    out = []
    with open(path, 'r', encoding='utf8') as f:
        for line in f:
            text = clean_text(line)
            # only keep lines longer than 3 words
            if len(text.split()) > 3:
                out.append({"text": text})
    return out

processed = []
raw_files = os.listdir("data/raw")  # only approved files here
for fname in raw_files:
    processed += process_file(os.path.join("data/raw", fname))

# Example for 2-line dialogues
train_examples = []
for ex in processed:
    text = ex["text"]
    # assuming delimiter "->" between prompt and response
    if "->" in text:
        prompt, response = text.split("->", 1)
        train_examples.append({"prompt": prompt.strip(), "response": response.strip()})

import random

random.shuffle(processed)
n = len(processed)
train = processed[:int(n*0.95)]
val = processed[int(n*0.95):]
test = train_examples[:1000]  # first 1000 examples for testing

os.makedirs("data/processed", exist_ok=True)

# Train file
with open("data/processed/user_corpus.jsonl", "w", encoding="utf8") as f:
    for ex in train:
        f.write(json.dumps(ex, ensure_ascii=False) + "\n")

# Validation file
with open("data/processed/user_corpus_val.jsonl", "w", encoding="utf8") as f:
    for ex in val:
        f.write(json.dumps(ex, ensure_ascii=False) + "\n")
