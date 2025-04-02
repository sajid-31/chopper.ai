import requests
import json
import os
from pathlib import Path
from cryptography.fernet import Fernet

def load_key(KEY_FILE):
    return open(KEY_FILE, 'rb').read()

class LLMClient:
    def __init__(self):
        CONFIG_FILE = Path.home() / '.chopper_ai' / 'config.json'
        KEY_FILE = Path.home() / '.chopper_ai' / 'key.key'
        key = load_key(KEY_FILE)
        fernet = Fernet(key)
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        LLM_API_KEY = fernet.decrypt(config['LLM_API_KEY'].encode()).decode()
        self.headers = {
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json"
        }

    def query(self, user_input):
        payload = {
            "model": "deepseek/deepseek-r1:free",
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        }
        CONFIG_FILE = Path.home() / '.chopper_ai' / 'config.json'
        KEY_FILE = Path.home() / '.chopper_ai' / 'key.key'
        key = load_key(KEY_FILE)
        fernet = Fernet(key)
        with open(CONFIG_FILE, 'r') as f:
            config = json.load(f)
        LLM_API_URL = fernet.decrypt(config['LLM_API_URL'].encode()).decode()
        if not LLM_API_URL:
            raise ValueError("LLM_API_URL is not set! Please check your environment variables or configuration.")

        response = requests.post(LLM_API_URL, headers=self.headers, json=payload)
        return response.json()
