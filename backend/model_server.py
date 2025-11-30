# backend/model_server.py
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel
import torch
from dotenv import load_dotenv
from backend.safety import safe_generate
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()

app = FastAPI(title="User Clone Model Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development only; allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration (can override with env vars)
MODEL_DIR = os.getenv("MODEL_DIR", "models/user_clone")
BASE_MODEL_NAME = os.getenv("BASE_MODEL_NAME", "gpt2")  # base used during training
MAX_ALLOWED_LENGTH = int(os.getenv("MAX_ALLOWED_LENGTH", "512"))

# Device
device = "cuda" if torch.cuda.is_available() else "cpu"

def generate_from_model(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    out = model.generate(**inputs, max_new_tokens=100, temperature=0.8)
    return tokenizer.decode(out[0], skip_special_tokens=True)


# Load tokenizer
# Prefer loading tokenizer from MODEL_DIR (if saved there), otherwise from base
if os.path.isdir(MODEL_DIR) and os.path.exists(os.path.join(MODEL_DIR, "tokenizer_config.json")):
    tokenizer = AutoTokenizer.from_pretrained(MODEL_DIR)
else:
    tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL_NAME)
tokenizer.pad_token = tokenizer.eos_token

# Load base model & apply PEFT adapters
print("Loading base model:", BASE_MODEL_NAME)
base_model = AutoModelForCausalLM.from_pretrained(BASE_MODEL_NAME, device_map="auto" if device=="cuda" else None)
print("Loading adapters from:", MODEL_DIR)
model = PeftModel.from_pretrained(base_model, MODEL_DIR)
model.to(device)
model.eval()

class GenIn(BaseModel):
    prompt: str
    max_length: int = 100
    temperature: float = 0.8
    top_p: float = 0.9
    do_sample: bool = True

@app.post("/generate")
def generate(req: GenIn):
    prompt = (req.prompt or "").strip()
    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt is empty")
    if req.max_length < 1 or req.max_length > MAX_ALLOWED_LENGTH:
        raise HTTPException(status_code=400, detail=f"max_length must be 1..{MAX_ALLOWED_LENGTH}")

    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=req.max_length,
            temperature=req.temperature,
            top_p=req.top_p,
            do_sample=req.do_sample,
            pad_token_id=tokenizer.eos_token_id
        )
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return {"generated_text": text}

@app.post("/generate")
def generate(req: GenIn):
    return {"generated_text": safe_generate(generate_from_model, req.prompt)}
