
# 🤖 Discord Auto Messenger with Local AI Rephrasing (Selfbot)

A simple yet powerful selfbot script to send automated, human-like messages in Discord channels at scheduled intervals — with AI-powered rephrasing using a local Transformer model (`T5_Paraphrase_Paws`).

---

## ✨ Features

- ✅ Auto-sends messages to specified channels every ~12 hours
- 🧠 Rephrases messages using a local NLP model (no API keys or external services)
- 🕒 Randomized delays to mimic natural typing and sending behavior
- 🔄 Easy to customize channels and message sets
- 🧼 Clean and readable Python code

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/vm10ks/Discord-Auto-Messenger-with-Local-AI-Rephrasing-Selfbot-
cd Discord-Auto-Messenger-with-Local-AI-Rephrasing-Selfbot-
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### 🔐 Add Your Discord User Token

In `messenger.py`, replace:

```python
TOKEN = "YOUR_USER_TOKEN"
```

> ⚠️ This is a **selfbot**. You must use a user token (not a bot token).
> ⚠️ Using a selfbot violates [Discord's Terms of Service](https://discord.com/terms) — use at your own risk!

### 📨 Set Channels & Messages

Edit the `targets` dictionary:

```python
targets = {
    123456789012345678: [
        "Hey! Just launched ScaleScrape — a powerful tool for scraping at scale. Who should I talk to about it?"
    ],
}
```

You can add multiple channel IDs and multiple messages per channel.

---

## 🧠 Local AI Rephrasing (Optional)

This script uses a local rephrasing model:

```python
from transformers import pipeline
rephrase = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")
```

Before sending, the message is paraphrased into a more human, varied version.
This helps avoid looking automated or spammy.

---

## ▶️ Run the Script

```bash
python messenger.py
```

You'll see logs like:

```
[2025-06-10 12:00:00] Sending messages...
[⏱] Sleeping for ~12.34 hours...
```

---

## ❗ Disclaimer

* ⚠️ **This is a selfbot. It breaks Discord’s TOS.**
  Use responsibly, only with your own accounts, and understand the risks (e.g., account termination).
* 🧪 Intended for educational or controlled-use automation only.

---

Enjoy 👨‍💻🚀

