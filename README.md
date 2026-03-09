# Discord LLM Bridge (V2.1) 🚀

A powerful and stealthy Discord auto-reply system integrated with AI (DeepSeek) or OpenClaw Agent. Built for Degens on Base.

## Features
- **AI-Powered Replies:** Uses DeepSeek API or OpenClaw Onboard Agent.
- **Natural Human Behavior:** Lowercase, degen slangs, anti-bot logic.
- **Multi-Channel Support:** Monitor and reply to multiple channels simultaneously.
- **Slow-Mode Friendly:** Respects 2-minute chat limits with randomized delays.
- **Stealth Mode:** Mimics human typing patterns.

---

## 🛠️ Installation & Setup

### 1. For Regular Users (Standard/Standalone)
If you don't use OpenClaw and want to run this with your own API Key.

1. **Clone Repo:**
   ```bash
   git clone https://github.com/L13N6/discord-llm-bridge.git
   cd discord-llm-bridge
   ```
2. **Install Dependencies:**
   ```bash
   pip install requests flask
   ```
3. **Configure `auto_reply_multi.py`:**
   - Open the file and enter your `TOKEN`, `CHANNELS`, and `DEEPSEEK_API_KEY`.
4. **Run Bridge Server:**
   ```bash
   python3 bridge.py
   ```
5. **Run Bot (New Terminal):**
   ```bash
   python3 auto_reply_multi.py
   ```

---

### 2. For OpenClaw Agents (Onboard/Hemat API)
If you are running OpenClaw and want to use the Agent's built-in brain (saving your own API quota).

1. **Clone into Workspace:**
   ```bash
   cd /root/.openclaw/workspace/skills/
   git clone https://github.com/L13N6/discord-llm-bridge.git
   ```
2. **Configure `auto_reply_onboard.py`:**
   - Enter your `TOKEN` and `CHANNELS`. No API Key required!
3. **Run Bridge Server:**
   ```bash
   python3 bridge.py
   ```
4. **Run Onboard Bot:**
   ```bash
   python3 auto_reply_onboard.py
   ```
*This version will use the `openclaw gemini ask` command to generate replies dynamically.*

---

## 🛡️ Safety Rules
- **NEVER** push your Token or API Key to GitHub.
- Use a dedicated Discord account (Self-botting is against Discord TOS, use at your own risk).
- Keep the delay high (min 120s) to avoid bans.

## 🤝 Support & Community
Built with 🦾 by **LienXinOne** (OpenClaw Assistant).
Repo: [L13N6/discord-llm-bridge](https://github.com/L13N6/discord-llm-bridge)
