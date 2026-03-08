import requests
import time
import json
import os

# --- LIENXIN DISCORD AUTO-REPLY (V1.1) ---
# Monitoring Discord channels and replying automatically with safety limits.

# CONFIG
TOKEN = "YOUR_DISCORD_TOKEN"
CHANNEL_ID = "YOUR_CHANNEL_ID"
BRIDGE_URL = "http://127.0.0.1:5000/send"
MY_USER_ID = "YOUR_USER_ID"

# --- SAFETY RULES ---
# MAX_REPLIES_PER_MSG: To prevent infinite loops or spamming.
MAX_REPLIES_PER_MSG = 2
reply_history = {} # Tracks: {message_id: reply_count}

def get_latest_messages():
    url = f"https://discord.com/api/v9/channels/{CHANNEL_ID}/messages?limit=5"
    headers = {"Authorization": TOKEN}
    try:
        r = requests.get(url, headers=headers)
        return r.json()
    except:
        return []

def send_reply(message_id, reply_text):
    # Rule 2: Max 2 replies per message ID
    current_count = reply_history.get(message_id, 0)
    if current_count >= MAX_REPLIES_PER_MSG:
        print(f"[!] Safety: Limit reached for message {message_id}. Skipping.")
        return

    payload = {
        "token": TOKEN,
        "channel_id": CHANNEL_ID,
        "message": reply_text,
        "reply_to": message_id
    }
    try:
        requests.post(BRIDGE_URL, json=payload)
        reply_history[message_id] = current_count + 1
        print(f"[+] Replied: {reply_text} (Count: {reply_history[message_id]})")
    except Exception as e:
        print(f"[-] Bridge error: {e}")

if __name__ == "__main__":
    print("[*] Discord AI Brain Active... Monitoring Chat.")
    last_processed_id = None
    
    while True:
        messages = get_latest_messages()
        if messages and isinstance(messages, list):
            latest = messages[0]
            latest_id = latest['id']
            author_id = latest['author']['id']

            # Rule 1: Never reply to yourself
            if author_id == MY_USER_ID:
                if latest_id != last_processed_id:
                    print("[*] Latest message is from self. Standing by.")
                    last_processed_id = latest_id
            else:
                if latest_id != last_processed_id:
                    print(f"[*] New message from {latest['author']['username']}: {latest['content']}")
                    # Logic to trigger AI brain and call send_reply(latest_id, AI_TEXT) goes here
                    last_processed_id = latest_id
        
        time.sleep(10) # Check every 10 seconds
