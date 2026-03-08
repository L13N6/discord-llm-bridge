import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# --- LIENXIN DISCORD BRIDGE V1.3 (MULTI-CHANNEL) ---

@app.route('/send', methods=['POST'])
def bridge_send():
    data = request.json
    token = data.get("token")
    channel_id = data.get("channel_id") # Dynamic Channel ID
    message = data.get("message")
    reply_to = data.get("reply_to")

    if not token or not channel_id:
        return jsonify({"status": "error", "message": "Missing token or channel_id"}), 400

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
    print("\n=== LIENXIN DISCORD BRIDGE V1.3 (MULTI-CHANNEL) ACTIVE ===")
    print("[*] Ready to handle requests for ANY channel ID.")
    app.run(host='127.0.0.1', port=5000)
