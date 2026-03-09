import requests
import time
import json
import os

# --- LIENXIN DISCORD AUTO-REPLY (V1.2 MULTI-CHANNEL) ---
# Monitoring multiple Discord channels and replying automatically.

# CONFIG
TOKEN = "YOUR_DISCORD_TOKEN"
CHANNELS = ["CHANNEL_ID_1", "CHANNEL_ID_2", "CHANNEL_ID_3"] # Add your IDs here
BRIDGE_URL = "http://127.0.0.1:5000/send"
MY_USER_ID = "YOUR_USER_ID"

# SAFETY RULES
MAX_REPLIES_PER_MSG = 2
reply_history = {}

def get_latest_messages(channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=5"
    headers = {"Authorization": TOKEN}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        return r.json()
    except:
        return []

def send_reply(channel_id, message_id, reply_text):
    current_count = reply_history.get(message_id, 0)
    if current_count >= MAX_REPLIES_PER_MSG:
        return

    payload = {
        "token": TOKEN,
        "channel_id": channel_id,
        "message": reply_text,
        "reply_to": message_id
    }
    try:
        requests.post(BRIDGE_URL, json=payload, timeout=10)
        reply_history[message_id] = current_count + 1
        print(f"[+] Replied in {channel_id}: {reply_text}")
    except Exception as e:
        print(f"[-] Bridge error: {e}")

if __name__ == "__main__":
    print(f"[*] Monitoring {len(CHANNELS)} channels...")
    last_processed_ids = {cid: None for cid in CHANNELS}
    
    while True:
        for channel_id in CHANNELS:
            messages = get_latest_messages(channel_id)
            if messages and isinstance(messages, list):
                latest = messages[0]
                latest_id = latest['id']
                author_id = latest['author']['id']

                if author_id != MY_USER_ID and latest_id != last_processed_ids.get(channel_id):
                    print(f"[*] New message in {channel_id} from {latest['author']['username']}: {latest['content']}")
                    # AI Brain logic here...
                    last_processed_ids[channel_id] = latest_id
            
            time.sleep(2) # Short gap between channels to avoid rate limit
        
        time.sleep(30) # Check cycle every 30s
