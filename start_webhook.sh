#!/bin/bash

# Configuration
# Replace 'your_topic_here' with your actual ntfy topic
export NTFY_TOPIC="your_topic_here"
# export NTFY_URL="https://ntfy.sh" # Optional
# export PORT=5049 # Optional

# Path to the project
PROJECT_DIR="$HOME/android-sms-gateway-to-ntfy-sh"

# Wait for network to be ready
sleep 30

if [ -d "$PROJECT_DIR" ]; then
    cd "$PROJECT_DIR"
    # Run in background and redirect output to a log file
    python sms_webhook.py > webhook.log 2>&1 &
fi
