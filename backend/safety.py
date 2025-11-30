# backend/safety.py
from detoxify import Detoxify
import logging
from datetime import datetime
import os

# Initialize Detoxify model
detox = Detoxify('original')

# Create encrypted/log directory if needed
os.makedirs("logs/safety", exist_ok=True)

# Setup simple logging (consider encryption for production)
logging.basicConfig(
    filename=f"logs/safety/safety_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

def safe_generate(generate_func, prompt):
    """
    Wraps model generation with toxicity filter.

    Args:
        generate_func: callable that takes prompt -> text
        prompt: str input

    Returns:
        Safe generated text
    """
    # Generate text from the model
    text = generate_func(prompt)

    # Run toxicity check
    tox_scores = detox.predict(text)
    if tox_scores.get('toxicity', 0) > 0.6:
        safe_text = "[Generation blocked due to toxicity]"
    else:
        safe_text = text

    # Log safely (prompt + output)
    logging.info(f"Prompt: {prompt} | Output: {safe_text}")

    return safe_text

