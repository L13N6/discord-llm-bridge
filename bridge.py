import requests
import time
import json
import os
from flask import Flask, request, jsonify

# --- LIENXIN DISCORD BRIDGE (V1.1) ---
# Jalankan di Termux Utama (Android).
# Menghubungkan LienXin (Proot) ke Discord via IP HP Bos.

app = Flask(__name__)
CONFIG_FILE = "bridge_config.json"

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"token": "MASUKKAN_TOKEN_DISINI", "channel_id": "MASUKKAN_CHANNEL_ID_DISINI"}

@app.route('/send', methods=['POST'])
def bridge_send():
    data = request.json
    config = load_config()
    
    token = data.get("token", config["token"])
    channel_id = data.get("channel_id", config["channel_id"])
    message = data.get("message", "")

    if not token or token == "MASUKKAN_TOKEN_DISINI":
        return jsonify({"status": "error", "message": "Token belum diatur!"}), 400

    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {"Authorization": token, "Content-Type": "application/json"}
    payload = {"content": message}

    try:
        r = requests.post(url, headers=headers, json=payload)
        return jsonify({"status": "success", "code": r.status_code, "response": r.json()})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    print("\n=== LIENXIN DISCORD BRIDGE AKTIF ===")
    print("[*] Menunggu perintah dari LienXin di Proot...")
    print("[!] Jangan tutup jendela Termux ini selama bot jalan.")
    app.run(host='127.0.0.1', port=5000)
