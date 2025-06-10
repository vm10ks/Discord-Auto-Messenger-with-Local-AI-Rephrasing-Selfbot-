import discord
import asyncio
import random
from datetime import datetime
from transformers import pipeline

# Load paraphrasing model
rephrase = pipeline("text2text-generation", model="Vamsi/T5_Paraphrase_Paws")

TOKEN = "YOUR_USER_TOKEN"

# Channels and your custom message(s)
targets = {
    123456789012345678: [  # Replace with actual channel ID
        "I have built a new thing: ScaleScrape – a simple but powerful tool for scraping at scale.\n\n"
        "I made this after getting tired of clunky scraping libraries. This one’s quick, clean, and dev-friendly — "
        "also bypasses Cloudflare bot protection and can scrape from any explorer directly without rate limiting or anything stopping us. "
        "Whom should I reach out to propose it?"
    ],
}

client = discord.Client(self_bot=True)

def rephrase_message(text):
    try:
        out = rephrase(f"paraphrase: {text} </s>", max_length=256, num_return_sequences=1, do_sample=True)
        return out[0]['generated_text']
    except Exception as e:
        print(f"[!] Rephrase failed: {e}")
        return text

async def send_message(channel, messages):
    try:
        async with channel.typing():
            delay = random.uniform(1.0, 3.5)
            await asyncio.sleep(delay)
        original_msg = random.choice(messages)
        msg = rephrase_message(original_msg)
        await channel.send(msg)
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sent to {channel.name} in {channel.guild.name}")
    except Exception as e:
        print(f"[!] Failed to send message in {channel.id}: {e}")

async def message_loop():
    await client.wait_until_ready()

    while not client.is_closed():
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Sending messages...")

        for channel_id, messages in targets.items():
            channel = client.get_channel(channel_id)
            if channel:
                await send_message(channel, messages)
            else:
                print(f"[!] Channel {channel_id} not found or not accessible.")

        # Random sleep between 11.5 and 12.5 hours
        sleep_time = random.randint(41400, 45000)
        print(f"[⏱] Sleeping for ~{sleep_time/3600:.2f} hours...\n")
        await asyncio.sleep(sleep_time)

@client.event
async def on_ready():
    print(f" Logged in as {client.user} ({client.user.id})")

client.loop.create_task(message_loop())
client.run(TOKEN, bot=False)
