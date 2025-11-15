# training/train.py
import json
import os
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForCausalLM, Trainer, TrainingArguments, DataCollatorForLanguageModeling
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training

# -------------------------
# Step 0: Optional: concatenate short messages
# -------------------------
def concatenate_short_examples(jsonl_path, min_tokens=20):
    """Read JSONL and merge short messages into examples >= min_tokens."""
    concatenated = []
    buffer = ""
    with open(jsonl_path, "r", encoding="utf8") as f:
        for line in f:
            ex = json.loads(line)
            text = ex["text"].strip()
            buffer += text + " "
            if len(buffer.split()) >= min_tokens:
                concatenated.append({"text": buffer.strip()})
                buffer = ""
    if buffer:
        concatenated.append({"text": buffer.strip()})
    return concatenated

# Paths
train_path = "data/processed/user_corpus.jsonl"
val_path = "data/processed/user_corpus_val.jsonl"

train_data = concatenate_short_examples(train_path)
val_data = concatenate_short_examples(val_path)

# Save temporary JSON files for datasets
os.makedirs("data/temp", exist_ok=True)
with open("data/temp/train.jsonl", "w", encoding="utf8") as f:
    for ex in train_data:
        f.write(json.dumps(ex, ensure_ascii=False) + "\n")
with open("data/temp/val.jsonl", "w", encoding="utf8") as f:
    for ex in val_data:
        f.write(json.dumps(ex, ensure_ascii=False) + "\n")

# -------------------------
# Step 1: Model & tokenizer
# -------------------------
model_name = "gpt2"  # or "distilgpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
tokenizer.pad_token = tokenizer.eos_token  # GPT-2 has no pad token

# -------------------------
# Step 2: Load datasets
# -------------------------
train_ds = load_dataset("json", data_files="data/temp/train.jsonl")["train"]
val_ds = load_dataset("json", data_files="data/temp/val.jsonl")["train"]

# -------------------------
# Step 3: Tokenization
# -------------------------
def tokenize(example):
    return tokenizer(example["text"], truncation=True, max_length=512)

train_ds = train_ds.map(tokenize, batched=True, remove_columns=["text"])
val_ds = val_ds.map(tokenize, batched=True, remove_columns=["text"])

# -------------------------
# Step 4: Load model with 8-bit (Windows-safe)
# -------------------------
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    load_in_8bit=True  # works on Windows; ignore deprecation warning
)
model = prepare_model_for_kbit_training(model)

# -------------------------
# Step 5: Configure LoRA
# -------------------------
lora_config = LoraConfig(
    r=8,
    lora_alpha=32,
    target_modules=["c_attn", "c_proj"],
    lora_dropout=0.05,
    bias="none"
)
model = get_peft_model(model, lora_config)

# -------------------------
# Step 6: Training arguments
# -------------------------
training_args = TrainingArguments(
    output_dir="models/user_clone",
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    gradient_accumulation_steps=8,
    num_train_epochs=3,
    learning_rate=2e-4,
    fp16=True,
    logging_steps=10,
    save_strategy="epoch"  # compatible with all Transformers >=4.x
)

# -------------------------
# Step 7: Data collator (handles variable-length sequences)
# -------------------------
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer,
    mlm=False  # causal LM
)

# -------------------------
# Step 8: Trainer
# -------------------------
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_ds,
    eval_dataset=val_ds,
    data_collator=data_collator
)

# -------------------------
# Step 9: Train & save
# -------------------------
trainer.train()
trainer.save_model("models/user_clone")

print("✅ LoRA training complete! Model saved in models/user_clone")
