from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# Configuration from environment variables
NTFY_TOPIC = os.getenv("NTFY_TOPIC")
NTFY_URL = os.getenv("NTFY_URL", "https://ntfy.sh").rstrip("/")
PORT = int(os.getenv("PORT", "5049"))

def send_ntfy(title, text):
    if not NTFY_TOPIC:
        print("Error: NTFY_TOPIC is not set.")
        return 500, "Missing NTFY_TOPIC"

    url = f"{NTFY_URL}/{NTFY_TOPIC}"

    try:
        response = requests.post(
            url,
            data=text.encode("utf-8"),
            headers={
                "Title": title,
                "Tags": "message,incoming_envelope"
            },
            timeout=10
        )
        return response.status_code, response.text
    except Exception as e:
        print(f"Error sending to ntfy: {e}")
        return 500, str(e)

@app.route("/", methods=["GET"])
def index():
    return "SMS Gateway Webhook is running", 200

@app.route("/sms-webhook", methods=["POST"])
def sms_webhook():
    data = request.get_json(silent=True) or {}
    
    event = data.get("event", "unknown")
    payload = data.get("payload") or {}

    sender = payload.get("sender") or payload.get("phoneNumber") or "Unknown"
    message = payload.get("message") or payload.get("data") or "(no text)"
    
    title = f"SMS from {sender}"
    content = f"Event: {event}\nFrom: {sender}\n\n{message}"

    status_code, response_text = send_ntfy(title, content)

    return jsonify({
        "status": "success" if status_code == 200 else "error",
        "ntfy_status": status_code
    }), status_code

if __name__ == "__main__":
    if not NTFY_TOPIC:
        print("WARNING: NTFY_TOPIC environment variable is not set!")
    app.run(host="0.0.0.0", port=PORT)
