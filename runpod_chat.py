import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get pod ID from environment variable
POD_ID = os.getenv("POD_ID")

if not POD_ID:
    raise ValueError("POD_ID environment variable not set. Please create a .env file with your pod ID.")

url = f"https://{POD_ID}-8000.proxy.runpod.net/v1/chat/completions"
headers = {"Content-Type": "application/json"}

data = {
    "model": "neuralmagic/Meta-Llama-3.1-8B-Instruct-FP8",
    "messages": [
        {"role": "user", "content": "Explain Python in one sentence"}
    ],
    "max_tokens": 50,
    "temperature": 0.7
}

try:
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    result = response.json()
    print(result["choices"][0]["message"]["content"])
except requests.RequestException as e:
    print(f"Request failed: {e}")
except (KeyError, IndexError) as e:
    print(f"Unexpected response format: {e}\nFull response: {response.text}") 