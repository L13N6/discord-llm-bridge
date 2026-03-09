# Discord LLM Bridge (V2.2) 🚀

A powerful and stealthy Discord auto-reply system integrated with AI (DeepSeek) or OpenClaw Agent. Built for Degens on Base.

> [!WARNING]  
> **EXPERIMENTAL ONLY:** This project is for educational/experimental purposes. Using self-bots is against Discord's Terms of Service. **ALWAYS** use a dummy or alt account to avoid the risk of your main account being banned.

## 🧠 Two Brain Options
Choose the mode that fits your setup:
1.  **Standalone Mode (`auto_reply_multi.py`):** Direct DeepSeek API integration. Best for users without OpenClaw.
2.  **OpenClaw Onboard Mode (`auto_reply_onboard.py`):** Integrated with OpenClaw Agent. **Safe API Key handling** via onboard settings (no need to hardcode keys in the script).

---

## 🛠️ Installation & Setup

### 1. Standalone Mode (Standard)
*For users who want to run the bot independently with their own API Key.*

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

### 2. OpenClaw Onboard Mode (Safe & Integrated)
*For OpenClaw users who want to use their Agent's brain. Safer because your API Key is managed by OpenClaw's secure environment.*

1. **Clone into OpenClaw Workspace:**
   ```bash
   cd ~/.openclaw/workspace/
   git clone https://github.com/L13N6/discord-llm-bridge.git
   ```
2. **Configure `auto_reply_onboard.py`:**
   - Enter your `TOKEN` and `CHANNELS`. 
   - **No API Key needed here!** It uses the Agent's secure onboard settings.
3. **Run Bridge Server:**
   ```bash
   python3 bridge.py
   ```
4. **Run Onboard Bot:**
   ```bash
   python3 auto_reply_onboard.py
   ```
*This version uses the `openclaw gemini ask` command, meaning it inherits whatever model and safety settings you've already configured in OpenClaw.*

---

## 🛡️ Safety Rules
- **NEVER** push your Token or API Key to GitHub.
- Use a dedicated Discord account (Self-botting is against Discord TOS).
- Randomized delays (120s+) are enabled by default to mimic human behavior.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Support
Built with 🦾 by **LienXinOne** (OpenClaw Assistant).
Repo: [L13N6/discord-llm-bridge](https://github.com/L13N6/discord-llm-bridge)
