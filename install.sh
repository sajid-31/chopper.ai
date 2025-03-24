#!/bin/bash

echo "🚀 Starting Chopper AI Setup..."

# Step 1: Check if pipx is installed
if ! command -v pipx &> /dev/null
then
    echo "❌ pipx not found. Installing pipx..."
    python3 -m pip install --user pipx
    python3 -m pipx ensurepath
    echo "✅ pipx installed! Please restart your terminal or source your shell config if needed."
fi

# Step 2: Install Chopper AI package using pipx
echo "📦 Installing Chopper AI via pipx..."
pipx install . --force

# Step 3: Run config.py to collect API keys
echo "🔑 Running initial configuration..."
python3 config.py

# Step 4: Overview
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
echo "🔧 chopper"
echo ""
echo "Happy Hacking! 🛠️🤖"
echo "======================================="
