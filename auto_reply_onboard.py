import requests
import time
import json
import os
import random
import subprocess

# --- LIENXIN DISCORD AUTO-REPLY (ONBOARD AGENT VERSION) ---
# This version uses the local OpenClaw Agent (onboard brain) to generate replies.

# CONFIG
TOKEN = "YOUR_DISCORD_TOKEN"
CHANNELS = ["YOUR_CHANNEL_ID"]
BRIDGE_URL = "http://127.0.0.1:5000/send"
MY_USER_ID = "YOUR_USER_ID"

def get_onboard_reply(user_content, author_name, is_reply_to_me=False):
    # Prompting the onboard agent to act as a degen
    prompt = (
        f"Context: In Discord DegenVerse, {author_name} said: '{user_content}'. "
    )
    if is_reply_to_me:
        prompt += "They are replying to you. "
    
    prompt += (
        "Reply as a human degen: lowercase, casual, use slangs like 'fr', 'no cap', 'gm', 'lfg'. "
        "Keep it 1 sentence max. If asked about level, say you just joined and don't know. "
        "If called a bot, deny it naturally. Reply ONLY with the chat message content."
    )

    try:
        # Using OpenClaw 'agents_list' and 'sessions_spawn' via CLI (simulated here)
        # For simplicity in this script, we use a specialized one-shot brain command
        # or call the internal OpenClaw process if available.
        # Since this script runs INSIDE the workspace, we can use 'openclaw' command.
        
        cmd = ["openclaw", "gemini", "ask", prompt]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
        
        if result.returncode == 0:
            return result.stdout.strip().strip('"')
        else:
            print(f"[-] Onboard Agent Error: {result.stderr}")
            return None
    except Exception as e:
        print(f"[-] Onboard Exception: {e}")
        return None

def get_latest_messages(channel_id):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages?limit=5"
    headers = {"Authorization": TOKEN}
    try:
        r = requests.get(url, headers=headers, timeout=10)
        return r.json()
    except:
        return []

def send_reply(channel_id, message_id, reply_text):
    if not reply_text:
        return
        
    payload = {
        "token": TOKEN,
        "channel_id": channel_id,
        "message": reply_text,
        "reply_to": message_id
    }
    try:
        requests.post(BRIDGE_URL, json=payload, timeout=10)
        print(f"[+] Onboard Agent Replied in {channel_id}: {reply_text}")
    except Exception as e:
        print(f"[-] Bridge error: {e}")

if __name__ == "__main__":
    print(f"[*] Onboard Agent Discord Brain Active. Monitoring {len(CHANNELS)} channels...")
    last_processed_ids = {cid: None for cid in CHANNELS}
    
    while True:
        for channel_id in CHANNELS:
            messages = get_latest_messages(channel_id)
            if messages and isinstance(messages, list):
                latest = messages[0]
                latest_id = latest['id']
                author_id = latest['author']['id']
                author_name = latest['author']['username']
                content = latest['content']

                if author_id != MY_USER_ID and latest_id != last_processed_ids.get(channel_id):
                    is_reply_to_me = latest.get('referenced_message') and latest['referenced_message']['author']['id'] == MY_USER_ID
                    
                    print(f"[*] Asking Onboard Agent to analyze: {content}")
                    
                    # Call Onboard Agent for dynamic reply
                    ai_reply = get_onboard_reply(content, author_name, is_reply_to_me)
                    
                    if ai_reply:
                        send_reply(channel_id, latest_id, ai_reply)
                    
                    last_processed_ids[channel_id] = latest_id
            
            time.sleep(5) 
        
        wait_time = random.randint(130, 200)
        print(f"[*] Onboard Agent waiting {wait_time}s for next cycle...")
        time.sleep(wait_time)
