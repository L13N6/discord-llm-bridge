# LienXin Discord Bridge - Public Structure

## 1. Project Folder Structure
```text
discord-bridge/
├── bridge.py         # Script utama (Flask Server)
├── config.json       # File konfigurasi (Token & Channel)
├── run.sh            # Shortcut untuk menjalankan bot
└── README.md         # Instruksi penggunaan
```

## 2. Main Script (`bridge.py`)
Script ini akan berjalan di localhost (127.0.0.1) sehingga aman dari deteksi luar.
```python
import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/send', methods=['POST'])
def bridge_send():
    data = request.json
    token = data.get("token")
    channel_id = data.get("channel_id")
    message = data.get("message")
    reply_to = data.get("reply_to") # Support reply message

    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": token, 
        "Content-Type": "application/json"
    }
    
    payload = {"content": message}
    if reply_to:
        payload["message_reference"] = {"message_id": reply_to}

    try:
        r = requests.post(url, headers=headers, json=payload)
        return jsonify({"status": "ok", "code": r.status_code, "res": r.json()})
    except Exception as e:
        return jsonify({"status": "error", "msg": str(e)}), 500

if __name__ == "__main__":
    print("\n=== LIENXIN DISCORD BRIDGE ACTIVE ===")
    app.run(host='127.0.0.1', port=5000)
```

## 3. How to Use (Command)
Untuk mengirim pesan dari luar (misal dari script lain atau proot):
```bash
curl -X POST http://127.0.0.1:5000/send \
-H "Content-Type: application/json" \
-d '{
  "token": "YOUR_DISCORD_TOKEN",
  "channel_id": "CHANNEL_ID",
  "message": "Halo bos!",
  "reply_to": "MESSAGE_ID_OPTIONAL"
}'
```
