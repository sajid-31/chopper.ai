#!/bin/bash

echo "⚙️  Starting Chopper AI Uninstallation..."

# Step 1: Uninstall chopper-ai package via pipx
if pipx list | grep -q 'chopper-ai'; then
    echo "📦 Uninstalling chopper-ai package..."
    pipx uninstall chopper-ai
else
    echo "ℹ️  Chopper AI is not installed via pipx."
fi

# Step 2: Remove config directory and keys
CONFIG_DIR="$HOME/.chopper_ai"
if [ -d "$CONFIG_DIR" ]; then
    echo "🗑️  Removing Chopper AI config files..."
    rm -rf "$CONFIG_DIR"
else
    echo "ℹ️  No config directory found at $CONFIG_DIR"
fi

# Step 3: Remove symlink from /usr/local/bin
CHOPPER_SYMLINK="/usr/local/bin/chopper-cli"
if [ -L "$CHOPPER_SYMLINK" ]; then
    echo "🗑️  Removing Chopper AI symlink..."
    sudo rm -f "$CHOPPER_SYMLINK"
else
    echo "ℹ️  No symlink found at $CHOPPER_SYMLINK"
fi

echo ""
echo "======================================="
echo "🧹 Chopper AI Uninstallation Complete!"
echo "======================================="
