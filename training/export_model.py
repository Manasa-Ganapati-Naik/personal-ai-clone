from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

MODEL_NAME = "gpt2"
FINETUNED_MODEL_PATH = "models/user_clone"

# Load base model + LoRA adapters
base = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model = PeftModel.from_pretrained(base, FINETUNED_MODEL_PATH)

# Save adapter weights again (clean export)
model.save_pretrained(FINETUNED_MODEL_PATH)
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
tokenizer.save_pretrained(FINETUNED_MODEL_PATH)

print("✅ Model export complete! Saved to models/user_clone/")
