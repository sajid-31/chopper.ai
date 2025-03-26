# Chopper AI - Your Terminal AI Assistant

Welcome to Chopper AI, a powerful AI assistant for your linux terminal! 🚀
![](chopper/assets/tutorial.gif)
## Prerequisites

Before installing Chopper AI, ensure that you have the following dependencies set up:

- **Linux OS or WSL**
- **Python 3.7+**  
  Chopper AI requires Python 3.7 or later. You can check your version using:  
  ```sh
  python3 --version
  ```
- **Pipx**
  ```sh
  pip install --user pipx
  pipx ensure path
  ```
  Restart your linux terminal after you install pipx for the first time



## 🔧 Installation

To install Chopper AI, follow these steps:
```
# Clone the repository
git clone https://github.com/sajid-31/chopper.ai.git
cd chopper.ai

# Run the setup script
chmod +x install.sh
./install.sh
```
 - Chopper.ai will ask for an API KEY
 - Create a free API KEY at [https://openrouter.ai/settings/keys](https://openrouter.ai/settings/keys) and paste it in the terminal
 - Chopper.ai uses [Fernet Module](https://github.com/pyca/cryptography/blob/main/src/cryptography/fernet.py) to encrypt and decrypt your API Keys and saves it locally.
 - Currently, Chopper.ai uses the [Deepseek-r1: Free Model](https://openrouter.ai/deepseek/deepseek-r1:free)

**What the setup does:**

- Installs Chopper AI globally using pipx.
- Runs the initial configuration (config.py) to set up API keys.
- Provides a quick overview of Chopper AI's features.

**🎮 Usage**

Once installed, you can start Chopper AI by running:
```
chopper
```
## Features:

✅ Integrates with various LLM APIs (OpenRouter, OpenAI, DeepSeek, etc.)\
✅ Securely encrypts & stores API keys locally\
✅ Simple CLI interface: just type chopper to begin!

## ❌ Uninstallation

To remove Chopper AI completely, run the following code in chopper.ai directory:
```
chmod +x uninstall.sh
./uninstall.sh
```
What the uninstall script does:
- Uninstalls Chopper AI from pipx.
- Removes configuration files (config.json, key.key).
- Clears Chopper AI from system paths.

## 🔄 Exiting Chopper AI

To exit the assistant, you can:

**Press CTRL + C**

## 🛠️ Contributing

Feel free to open issues and pull requests! 😊
