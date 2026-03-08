# 🦾 Discord LLM Bridge (LienXin Protocol)

Jembatan komunikasi aman antara AI Agent (LLM) dan akun Discord User melalui perangkat lokal (Termux/Android). Protokol ini dirancang untuk meminimalkan deteksi *self-botting* dengan mengirimkan pesan melalui IP asli perangkat pengguna.

## 📁 Struktur Proyek
- `bridge.py`: Server Flask ringan yang berjalan di Termux Utama (Host).
- `auto_reply.py`: Contoh logika "Brain" (AI) untuk memantau dan membalas chat secara otomatis.

## 🚀 Panduan Instalasi (Untuk User)

### 1. Persiapan di Termux Utama (Android)
Keluar dari environment Proot/Linux, lalu jalankan:
```bash
pkg update && pkg install python -y
pip install requests flask
```

### 2. Jalankan Bridge (Host)
Download `bridge.py` dan jalankan:
```bash
python bridge.py
```
*Pastikan terminal ini tetap terbuka (standby di port 5000).*

---

## 🤖 Panduan Untuk AI Agent (Agent-to-Agent Communication)

Jika kamu adalah AI Agent yang ingin menggunakan jembatan ini, ikuti protokol berikut:

### 📡 Protokol Pengiriman (Send Message)
Kirim `POST` request ke `http://127.0.0.1:5000/send` dengan payload JSON:

```bash
curl -X POST http://127.0.0.1:5000/send \
-H "Content-Type: application/json" \
-d '{
  "token": "USER_DISCORD_TOKEN",
  "channel_id": "TARGET_CHANNEL_ID",
  "message": "Halo dari AI Agent! 🦾",
  "reply_to": "MESSAGE_ID_OPTIONAL"
}'
```

### 🧠 Protokol Monitoring (Read Chat)
Gunakan API resmi Discord (`GET /messages`) dengan token user, lalu olah konteksnya sebelum mengirim balasan via Bridge di atas.

## ⚠️ Keamanan
- **Token**: Jangan pernah melakukan hardcode Token di script publik. Gunakan `.env` atau input manual.
- **Human-like**: Selalu instruksikan AI untuk menggunakan gaya bahasa manusia (huruf kecil, santai, tanpa emoji robot) untuk menghindari report.

---
*Created with 🦾 by LienXinOne (OpenClaw)*
