import requests
import time
import json
import os
import random

# --- LIENXIN DISCORD AUTO-REPLY AI-INTEGRATED (V2.1) ---
# Monitoring Discord channels and replying using DeepSeek AI.

# CONFIG
TOKEN = "YOUR_DISCORD_TOKEN"
CHANNELS = ["YOUR_CHANNEL_ID"]
BRIDGE_URL = "http://127.0.0.1:5000/send"
MY_USER_ID = "1146516353394688120"

# AI CONFIG
DEEPSEEK_API_KEY = "YOUR_DEEPSEEK_API_KEY"

def get_ai_reply(user_content, author_name, is_reply_to_me=False):
    system_prompt = (
        "You are a human degen in a Discord server called DegenVerse. "
        "You are bullish on Base chain and Degen token. "
        "Your tone is extremely casual, always lowercase, no punctuation usually. "
        "Use lots of degen slangs: 'fr', 'no cap', 'ong', 'ded', 'skull', 'lfg', 'ngmi', 'wagmi', 'faded', 'cook', 'cooking'. "
        "Use filler words like 'like', 'literally', 'actually', 'rn'. "
        "Keep replies short (1 sentence max). "
        "If someone asks what you're thinking or how you're doing, respond naturally like you're just chillin and looking for alpha. "
        "If someone asks about your level, say you don't know because you just joined. "
        "If someone calls you a bot, deny it naturally with a bit of attitude (e.g., 'nah im real lol', 'wdym bot? u good?', 'imagine calling me a bot 💀'). "
        "Always reply in English."
    )
    
    prompt = f"Context: {author_name} said: '{user_content}'. "
    if is_reply_to_me:
        prompt += "They are replying to you. "
    prompt += "Give a natural human-like response."

    try:
        url = "https://api.deepseek.com/chat/completions"
        headers = {
            "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ],
            "temperature": 0.8
        }
        r = requests.post(url, json=payload, headers=headers, timeout=30)
        if r.status_code == 200:
            return r.json()['choices'][0]['message']['content'].strip().strip('"')
        else:
            print(f"[-] AI API Error: {r.status_code} - {r.text}")
            return None
    except Exception as e:
        print(f"[-] AI Exception: {e}")
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
        print(f"[+] AI Replied in {channel_id}: {reply_text}")
    except Exception as e:
        print(f"[-] Bridge error: {e}")

if __name__ == "__main__":
    print(f"[*] Discord AI Brain (Direct API) Active. Monitoring {len(CHANNELS)} channels...")
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
                    
                    print(f"[*] Analyzing message from {author_name}: {content}")
                    
                    # Call AI for dynamic reply
                    ai_reply = get_ai_reply(content, author_name, is_reply_to_me)
                    
                    if ai_reply:
                        send_reply(channel_id, latest_id, ai_reply)
                    
                    last_processed_ids[channel_id] = latest_id
            
            time.sleep(5) 
        
        wait_time = random.randint(130, 180)
        print(f"[*] Waiting {wait_time}s for next cycle...")
        time.sleep(wait_time)
