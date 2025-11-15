# training/evaluate_model.py

import json
import torch
import matplotlib.pyplot as plt
from transformers import AutoTokenizer, AutoModelForCausalLM
from sentence_transformers import SentenceTransformer, util
import os

# -------------------------------
# Step 0: Setup paths
# -------------------------------
DATA_PATH = "data/processed/user_corpus.jsonl"
MODEL_PATH = "models/user_clone"
LOG_FILE = "logs/train_run_20251106.txt"
REPORT_PATH = "docs/training_report.md"
LOSS_PLOT_PATH = "docs/train_loss_plot.png"
TEST_OUTPUT_PATH = "docs/test_outputs/sample_generation.txt"

os.makedirs("docs/test_outputs", exist_ok=True)

# -------------------------------
# Step 1: Load dataset & tokenizer
# -------------------------------
tokenizer = AutoTokenizer.from_pretrained("gpt2")
tokenizer.pad_token = tokenizer.eos_token

with open(DATA_PATH, "r", encoding="utf8") as f:
    dataset = [json.loads(line) for line in f]

num_examples = len(dataset)
num_tokens = sum(len(tokenizer(d["text"]).input_ids) for d in dataset)

# -------------------------------
# Step 2: Load LoRA model
# -------------------------------
model = AutoModelForCausalLM.from_pretrained(MODEL_PATH)

# -------------------------------
# Step 3: Plot training loss
# -------------------------------
losses = []
try:
    with open(LOG_FILE, "r") as f:
        for line in f:
            if "loss:" in line:
                try:
                    val = float(line.split("loss:")[1].split()[0])
                    losses.append(val)
                except:
                    continue
except FileNotFoundError:
    print("Log file not found. Skipping loss plot.")

if losses:
    plt.plot(losses, label="train_loss")
    plt.xlabel("Step")
    plt.ylabel("Loss")
    plt.title("Training Loss")
    plt.legend()
    plt.savefig(LOSS_PLOT_PATH)
    plt.close()

# -------------------------------
# Step 4: Inference examples
# -------------------------------
prompts = [
    "Hey, are we still meeting tomorrow?",
    "Dear team, please review the document attached.",
    "Happy birthday! Hope your day is amazing!"
]

outputs = []
for prompt in prompts:
    inputs = tokenizer(prompt, return_tensors="pt")
    output = model.generate(**inputs, max_length=50, do_sample=True, temperature=0.7)
    gen_text = tokenizer.decode(output[0], skip_special_tokens=True)
    outputs.append((prompt, gen_text))

with open(TEST_OUTPUT_PATH, "w", encoding="utf8") as f:
    for p, g in outputs:
        f.write(f"Prompt: {p}\nGenerated: {g}\n\n")

# -------------------------------
# Step 5: Compute metrics
# -------------------------------
def calculate_perplexity(model, tokenizer, text):
    inputs = tokenizer(text, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs, labels=inputs["input_ids"])
        loss = outputs.loss
    return torch.exp(loss).item()

perplexities = [calculate_perplexity(model, tokenizer, p) for p, _ in outputs]

# Embedding similarity using SBERT
sbert_model = SentenceTransformer('paraphrase-MiniLM-L6-v2')
user_texts = [p for p, _ in outputs]
generated_texts = [g for _, g in outputs]

emb1 = sbert_model.encode(user_texts, convert_to_tensor=True)
emb2 = sbert_model.encode(generated_texts, convert_to_tensor=True)
embedding_similarities = util.pytorch_cos_sim(emb1, emb2).diag().tolist()

# -------------------------------
# Step 6: Write training_report.md
# -------------------------------
with open(REPORT_PATH, "w", encoding="utf8") as f:
    f.write("# Training Report\n\n")

    f.write("## Dataset Information\n")
    f.write(f"- Number of training examples: {num_examples}\n")
    f.write(f"- Number of tokens: {num_tokens}\n\n")

    f.write("## Training Hyperparameters\n")
    f.write("- Model: GPT-2 / DistilGPT2\n")
    f.write("- LoRA: r=8, alpha=32, dropout=0.05\n")
    f.write("- Batch size: 2\n")
    f.write("- Gradient accumulation: 4\n")
    f.write("- Epochs: 3\n")
    f.write("- Learning rate: 2e-4\n")
    f.write("- FP16: True\n")
    f.write("- Max token length: 256\n\n")

    f.write("## Loss Graphs\n")
    if losses:
        f.write(f"![Training Loss]({LOSS_PLOT_PATH})\n\n")
    else:
        f.write("Loss graph not available.\n\n")

    f.write("## Sample Inference\n")
    for i, (p, g) in enumerate(outputs):
        f.write(f"**Prompt {i+1}:** {p}\n")
        f.write(f"**Generated:** {g}\n\n")

    f.write("## Metrics\n")
    for i, (p, g, pp, sim) in enumerate(zip(user_texts, generated_texts, perplexities, embedding_similarities)):
        f.write(f"**Prompt {i+1}:** {p}\n")
        f.write(f"- Generated: {g}\n")
        f.write(f"- Perplexity: {pp:.2f}\n")
        f.write(f"- SBERT similarity: {sim:.2f}\n\n")
