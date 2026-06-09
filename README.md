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

## Configuration (Webhook Registration)

Webhooks must be registered via the API using `curl` in Termux. Make sure to enable the **Local Server** in the app settings. You will need your **Login**, **Password**, and **IP Address** from the Android app's "Home" tab.

### Registration Command
Replace `USERNAME`, `PASSWORD`, and `IP_ADDRESS` with values from your app:

```bash
curl -X POST -u "USERNAME:PASSWORD" \
     -H "Content-Type: application/json" \
     -d '{
           "url": "http://127.0.0.1:5049/sms-webhook",
           "event": "sms:received"
         }' \
     http://IP_ADDRESS:8080/webhooks
```

### List Registered Webhooks
To verify your registration:
```bash
curl -u "USERNAME:PASSWORD" http://IP_ADDRESS:8080/webhooks
```

## Automation (Termux:Boot)

To run the webhook automatically when your phone starts:

1. Install the [Termux:Boot](https://github.com/termux/termux-boot) app.
2. Open the Termux:Boot app once to register it.
3. Create the boot directory and copy the script:
   ```bash
   mkdir -p ~/.termux/boot
   cp ~/android-sms-gateway-to-ntfy-sh/start_webhook.sh ~/.termux/boot/
   chmod +x ~/.termux/boot/start_webhook.sh
   ```
4. **Important:** Edit `~/.termux/boot/start_webhook.sh` and set your `NTFY_TOPIC`.

## Environment Variables

- `NTFY_TOPIC`: (Required) Your ntfy.sh topic name.
- `NTFY_URL`: (Optional) Custom ntfy server URL. Defaults to `https://ntfy.sh`.
- `PORT`: (Optional) Port to listen on. Defaults to `5049`.

## License
MIT
