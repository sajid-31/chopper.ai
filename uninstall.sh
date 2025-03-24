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

# Step 3: Remove binary if any residue remains (extra safety, pipx handles this)
CHOPPER_BIN="$(which chopper 2>/dev/null)"
if [ -n "$CHOPPER_BIN" ]; then
    echo "🗑️  Removing leftover binary: $CHOPPER_BIN"
    rm -f "$CHOPPER_BIN"
fi

echo ""
echo "======================================="
echo "🧹 Chopper AI Uninstallation Complete!"
echo "======================================="
