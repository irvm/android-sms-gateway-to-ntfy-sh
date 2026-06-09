# Android SMS Gateway to ntfy.sh (Termux)

Simple Python webhook to forward SMS messages from [android-sms-gateway](https://github.com/capcom6/android-sms-gateway) to [ntfy.sh](https://ntfy.sh). Optimized for running on Android via **Termux**.

## Setup in Termux

1. **Install Python & Git:**
   ```bash
   pkg update
   pkg install python git
   ```

2. **Clone & Install:**
   ```bash
   git clone https://github.com/irvm/android-sms-gateway-to-ntfy-sh.git
   cd android-sms-gateway-to-ntfy-sh
   pip install -r requirements.txt
   ```

3. **Run:**
   Replace `your_topic` with your actual ntfy topic name.
   ```bash
   export NTFY_TOPIC=your_topic
   python sms_webhook.py
   ```

## Configuration (Android App)

In the app settings, set the Webhook URL to:
`http://localhost:5049/sms-webhook`

## Environment Variables

- `NTFY_TOPIC`: (Required) Your ntfy.sh topic name.
- `NTFY_URL`: (Optional) Custom ntfy server URL. Defaults to `https://ntfy.sh`.
- `PORT`: (Optional) Port to listen on. Defaults to `5049`.

## License
MIT
