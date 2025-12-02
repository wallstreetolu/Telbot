# alert_bot.py - Monitors @stunner75trading for "first" + "people" and alerts @Stunner_v75
from pyrogram import Client, filters
import os

# ─── CONFIG (set as environment variables on Railway) ───
API_ID      = int(os.environ["API_ID"])
API_HASH    = os.environ["API_HASH"]
BOT_TOKEN   = os.environ["BOT_TOKEN"]
CHANNEL     = "@stunner75trading"  # Pre-set: Your public channel
ALERT_TO    = ["Stunner_v75"]      # Pre-set: Your username (without @)

app = Client("first_people_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(CHANNEL))
async def first_people_detector(client, message):
    if not message.text:  # Skip pure media messages
        return

    text = message.text.lower()
    if "first" in text and "people" in text:
        # Build alert message
        alert = "9134816284 OPAY" 

        # Send to the user
        for username in ALERT_TO:
            try:
                await client.send_message(username, alert)
                print(f"Alert sent to @{username}")
            except Exception as e:
                print(f"Failed to send to @{username}: {e}")

print("Bot started — monitoring @stunner75trading for 'first' + 'people'...")
app.run()
