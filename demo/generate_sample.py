# demo/generate_sample.py
import requests

URL = "http://127.0.0.1:8000/generate"
payload = {
    "prompt": "Hey, could you write a friendly reminder about the meeting tomorrow?",
    "max_length": 60,
    "temperature": 0.7,
    "top_p": 0.9,
    "do_sample": True
}

resp = requests.post(URL, json=payload, timeout=30)
print("Status:", resp.status_code)
print("Response JSON:", resp.json())
