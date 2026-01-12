from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# ---------------- App Setup ----------------
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- Request Schema ----------------
class PromptRequest(BaseModel):
    prompt: str

# ---------------- Health Check ----------------
@app.get("/")
def root():
    return {"status": "Personal AI Clone demo running"}

# ---------------- Stress / Motivation Generator ----------------
@app.post("/generate")
def generate_motivation(request: PromptRequest):
    return {
        "input": request.prompt,
        "generated_output": (
            "Feeling stressed before exams is completely normal, and it does "
            "not mean you are unprepared or incapable. Try to focus on one "
            "topic at a time and break your study sessions into manageable "
            "parts so they feel less overwhelming. Taking short breaks, "
            "getting enough rest, and staying hydrated can greatly improve "
            "your concentration and confidence. Remember that exams are just "
            "one part of your journey, and they do not define your worth. "
            "Stay calm, believe in yourself, and do your best—you’ve got this."
        )
    }
