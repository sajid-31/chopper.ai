#!/bin/bash

echo "🚀 Starting Chopper AI Setup..."

# Step 1: Store the current directory (chopper.ai path)
INSTALL_DIR="$(pwd)"

# Step 2: Check if pipx is installed
if ! command -v pipx &> /dev/null
then
    echo "❌ pipx not found. Installing pipx..."
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
    echo "✅ pipx installed! Please restart your terminal or source your shell config if needed."
fi

# Step 3: Install Chopper AI package using pipx
echo "📦 Installing Chopper AI via pipx..."
pipx install . --force

# Step 4: Run config.py to collect API keys
echo "🔑 Running initial configuration..."
python3 config.py

# Step 5: Adding SymLink
echo "🔗 Creating CLI shortcut..."
echo '#!/bin/bash
PYTHONPATH="'"$INSTALL_DIR"'" python3 -m chopper.main "$@"' | sudo tee /usr/local/bin/chopper-cli > /dev/null

echo "🔐 Enter password to give execute permission for /usr/local/bin/chopper"
sudo chmod +x /usr/local/bin/chopper-cli

# Step 6: Overview
echo ""
echo "======================================="
echo "🎉 Chopper AI Installation Complete! 🎉"
echo "======================================="
echo ""
echo "Welcome to Chopper AI - your terminal-based AI assistant!"
echo ""
echo "Features:"
echo "✅ Integrates with various LLM APIs (OpenRouter, OpenAI, DeepSeek, etc.)"
echo "✅ API keys are securely encrypted & stored locally"
echo "✅ Simple CLI interface: just type 'chopper' to begin!"
echo ""
echo "Usage:"
echo ""
echo "🔧 chopper-cli"
echo ""
echo "Happy Hacking! 🛠️🤖"
echo "======================================="
