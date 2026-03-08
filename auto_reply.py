import requests
import time
import json
import os

# --- LIENXIN DISCORD AUTO-REPLY (V1.0) ---
# Memantau channel Discord dan membalas secara otomatis menggunakan AI.

# CONFIG
TOKEN = "YOUR_DISCORD_TOKEN"
CHANNEL_ID = "YOUR_CHANNEL_ID"
BRIDGE_URL = "http://127.0.0.1:5000/send"
MY_USER_ID = "YOUR_USER_ID" # abasuhuy

def get_latest_messages():
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit=5"
    headers = {"Authorization": TOKEN}
    try:
        r = requests.get(url, headers=headers)
        return r.json()
    except:
        return []

def send_reply(message_id, reply_text):
    payload = {
        "token": TOKEN,
        "channel_id": CHANNEL_ID,
        "message": reply_text,
        "reply_to": message_id
    }
    try:
        requests.post(BRIDGE_URL, json=payload)
        print(f"[+] Membalas: {reply_text}")
    except Exception as e:
        print(f"[-] Gagal kirim via bridge: {e}")

if __name__ == "__main__":
    print("[*] Abasuhuy AI Brain Aktif... Memantau Chat.")
    last_msg_id = None
    
    while True:
        messages = get_latest_messages()
        if messages and isinstance(messages, list):
            latest = messages[0]
            # Cek jika pesan baru, bukan dari diri sendiri, dan ditujukan ke kita atau baru muncul
            if latest['id'] != last_msg_id:
                if latest['author']['id'] != MY_USER_ID:
                    print(f"[*] Pesan baru dari {latest['author']['username']}: {latest['content']}")
                    # Di sini kita perlu "Otak" (AI) untuk mikir balasannya.
                    # Untuk sementara, kita tandai di log.
                last_msg_id = latest['id']
        
        time.sleep(10) # Cek tiap 10 detik
