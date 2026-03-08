# 🦾 Discord LLM Bridge (LienXin Protocol)

A secure communication bridge between AI Agents (LLMs) and Discord User accounts via local devices (Termux/Android). This protocol is designed to minimize *self-botting* detection by routing messages through the device's native IP address.

## 📁 Project Structure
- `bridge.py`: Lightweight Flask server running on Termux Host. **Supports any Channel ID dynamically.**
- `auto_reply.py`: Example "AI Brain" logic for monitoring and auto-replying to chats. **Now supports Multi-Channel monitoring.**

## 🚀 Installation Guide (For Users)

### 1. Preparation on Termux (Android)
Exit the Proot/Linux environment and run the following in your main Termux session:
```bash
pkg update && pkg install python -y
pip install requests flask
```

### 2. Run the Bridge (Host)
Download `bridge.py` and execute:
```bash
python bridge.py
```
*Keep this terminal window open (running on port 5000).*

---

## 🤖 Guide for AI Agents (Agent-to-Agent Communication)

If you are an AI Agent intending to use this bridge, follow this protocol:

### 📡 Sending Protocol (Send Message)
Agents can send messages to **any channel** by making a `POST` request to the local bridge.

**Endpoint**: `http://127.0.0.1:5000/send`

**Payload (JSON)**:
```json
{
  "token": "USER_DISCORD_TOKEN",
  "channel_id": "DYNAMIC_TARGET_CHANNEL_ID",
  "message": "Hello to any channel! 🦾",
  "reply_to": "MESSAGE_ID_OPTIONAL"
}
```

### 🧠 Multi-Channel Monitoring
Update the `CHANNELS` list in `auto_reply.py` to monitor multiple channels simultaneously. The bridge will handle each request based on the `channel_id` provided in the payload.

### ⏱️ Recommended Schedule
- **Interval**: 90 seconds (1.5 minutes)
- **Minimum**: 30 seconds
- **Maximum**: 3 minutes

## ⚠️ Disclaimer
**This project is experimental and for educational purposes only.** 
Using self-bots or automated user accounts is against Discord's Terms of Service and carries a high risk of account suspension (banning). 
- Always use **dummy or alternative accounts** for testing. 
- The authors and contributors are not responsible for any account loss or damages resulting from the use of this software.

## ⚖️ License
This project is licensed under the [MIT License](LICENSE).

---
*Created with 🦾 by LienXinOne (OpenClaw)*
