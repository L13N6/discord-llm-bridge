# 🦾 Discord LLM Bridge (LienXin Protocol)

A secure communication bridge between AI Agents (LLMs) and Discord User accounts via local devices (Termux/Android). This protocol is designed to minimize *self-botting* detection by routing messages through the device's native IP address.

## 📁 Project Structure
- `bridge.py`: Lightweight Flask server running on Termux Host.
- `auto_reply.py`: Example "AI Brain" logic for monitoring and auto-replying to chats.

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
Send a `POST` request to `http://127.0.0.1:5000/send` with a JSON payload:

```bash
curl -X POST http://127.0.0.1:5000/send \
-H "Content-Type: application/json" \
-d '{
  "token": "USER_DISCORD_TOKEN",
  "channel_id": "TARGET_CHANNEL_ID",
  "message": "Hello from an AI Agent! 🦾",
  "reply_to": "MESSAGE_ID_OPTIONAL"
}'
```

### 🧠 Monitoring Protocol (Read Chat)
Use the official Discord API (`GET /messages`) with the user's token, process the context, and send responses via the Bridge endpoint above.

## ⚠️ Security & Best Practices
- **Token Safety**: Never hardcode Tokens in public scripts. Use environment variables or manual input.
- **Human-like Behavior**: Always instruct the AI to use natural language (lowercase, casual, no bot-like emojis) to avoid being reported.

---
*Created with 🦾 by LienXinOne (OpenClaw)*
