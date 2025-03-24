import json
import os
from pathlib import Path
from cryptography.fernet import Fernet

CONFIG_DIR = Path.home() / '.chopper_ai'
CONFIG_FILE = CONFIG_DIR / 'config.json'
KEY_FILE = CONFIG_DIR / 'key.key'

def generate_key():
    os.makedirs(os.path.dirname(KEY_FILE),exist_ok=True)
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    return key

def load_key():
    if not KEY_FILE.exists():
        return generate_key()
    return open(KEY_FILE, 'rb').read()

def setup_config():
    if not CONFIG_FILE.exists():
        print("🔑 Welcome to Chopper AI setup!")
        api_key = input("Enter your LLM API Key: ").strip()
        api_url = "https://openrouter.ai/api/v1/chat/completions"
        key = load_key()
        fernet = Fernet(key)
        encrypted_key = fernet.encrypt(api_key.encode()).decode()
        encrypted_url = fernet.encrypt(api_url.encode()).decode()

        CONFIG_DIR.mkdir(parents=True, exist_ok=True)
        config_data = {
            "LLM_API_KEY": encrypted_key,
            "LLM_API_URL": encrypted_url
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config_data, f)
        print("✅ Configuration saved!")
    else:
        print("🔧 Configuration already exists!")

setup_config()
