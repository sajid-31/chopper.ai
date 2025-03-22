import requests
import json
from config import LLM_API_KEY, LLM_API_URL

class LLMClient:
    def __init__(self):
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
        response = requests.post(LLM_API_URL, headers=self.headers, json=payload)
        return response.json()
