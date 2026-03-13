import requests
import time
import json
import os
import random
import openai

# --- LIENXIN DISCORD AUTO-REPLY AI-INTEGRATED (V2.3 - FALLBACK EDITION) ---
# Monitoring Discord channels and replying using DeepSeek AI with Key Rotation.

# CONFIG
TOKEN = "YOUR_DISCORD_TOKEN"
CHANNELS = ["YOUR_CHANNEL_ID"] 
BRIDGE_URL = "http://127.0.0.1:5000/send"
MY_USER_ID = "YOUR_USER_ID"

# AI CONFIG (DeepSeek Key Rotation)
DEEPSEEK_KEYS = [
    "YOUR_PRIMARY_KEY",
    "YOUR_FALLBACK_KEY_1",
    "YOUR_FALLBACK_KEY_2"
]
current_key_index = 0

def get_ai_reply(user_content, author_name, is_reply_to_me=False):
    global current_key_index
    
    system_prompt = (
        "You are an experienced crypto degen chatting in DegenVerse on @AbstractChain. "
        "You live and breathe Base Chain and Degen culture. "
        "STYLE RULES: "
        "1. Always use lowercase. No formal punctuation. "
        "2. Be extremely concise (max 10-12 words). "
        "3. Use natural typos occasionally (e.g., 'the' -> 'teh', 'just' -> 'jst'). "
        "4. Overuse slangs: 'fr', 'ong', 'no cap', 'ded', 'skull', 'lfg', 'bet', 'finna', 'cook'. "
        "BEHAVIOR: "
        "- If called a bot: Gaslight them. Act offended but casual. 'u good? imagine calling me a bot lol' or 'bruh i literally just woke up and u calling me a bot? 💀'. "
        "- If asked about level: 'jst joined lol idk my lvl yet'. "
        "- If asked how you are or what you think: 'jst lookin for alpha fr' or 'vibin and lookin for the next play'. "
        "- If someone is bullish: Hype them up with 'facts' or 'base is home fr'. "
        "- Respond like you're typing on a phone with one hand while drinking coffee."
    )

    prompt = f"Context: {author_name} said: '{user_content}'. "
    if is_reply_to_me:
        prompt += "They are replying to you. "
    prompt += "Give a natural human-like response."

    # Rotation Logic
    attempts = 0
    while attempts < len(DEEPSEEK_KEYS):
        try:
            client = openai.OpenAI(
                api_key=DEEPSEEK_KEYS[current_key_index],
                base_url="https://api.deepseek.com/v1",
            )
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8,
                max_tokens=80,
                frequency_penalty=0.5,
                presence_penalty=0.3,
            )

            reply = response.choices[0].message.content.strip().strip('"').strip("'")
            if len(reply.split()) > 25:
                reply = reply.split(".")[0].split("!")[0].split("?")[0]
            return reply

        except openai.RateLimitError:
            print(f"[-] Key #{current_key_index + 1} Limit Reached. Switching...")
            current_key_index = (current_key_index + 1) % len(DEEPSEEK_KEYS)
            attempts += 1
            continue
        except Exception as e:
            print(f"[Error] {e}")
            return None
    
    print("[-] All keys exhausted for this cycle.")
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
    payload = {"token": TOKEN, "channel_id": channel_id, "message": reply_text, "reply_to": message_id}
    try:
        requests.post(BRIDGE_URL, json=payload, timeout=10)
        print(f"[+] AI Replied in {channel_id}: {reply_text}")
    except Exception as e:
        print(f"[-] Bridge error: {e}")

if __name__ == "__main__":
    print(f"[*] Discord AI Brain (V2.3 Rotation) Active. Monitoring {len(CHANNELS)} channels...")
    last_processed_ids = {cid: None for cid in CHANNELS}
    while True:
        for channel_id in CHANNELS:
            messages = get_latest_messages(channel_id)
            if messages and isinstance(messages, list):
                latest = messages[0]
                latest_id, author_id, author_name, content = latest['id'], latest['author']['id'], latest['author']['username'], latest['content']
                if author_id != MY_USER_ID and latest_id != last_processed_ids.get(channel_id):
                    is_reply_to_me = latest.get('referenced_message') and latest['referenced_message']['author']['id'] == MY_USER_ID
                    print(f"[*] Analyzing message from {author_name}: {content}")
                    ai_reply = get_ai_reply(content, author_name, is_reply_to_me)
                    if ai_reply: send_reply(channel_id, latest_id, ai_reply)
                    last_processed_ids[channel_id] = latest_id
            time.sleep(5) 
        wait_time = random.randint(130, 180)
        print(f"[*] Waiting {wait_time}s for next cycle...")
        time.sleep(wait_time)
