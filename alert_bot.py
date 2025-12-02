# alert_bot.py - Add dummy server for Render Web Service
from pyrogram import Client, filters
import os
import threading  # For running dummy server in background
from http.server import HTTPServer, BaseHTTPRequestHandler

# ─── CONFIG (environment variables) ───
API_ID      = int(os.environ["API_ID"])
API_HASH    = os.environ["API_HASH"]
BOT_TOKEN   = os.environ["BOT_TOKEN"]
CHANNEL     = "@stunner75trading"
ALERT_TO    = ["Stunner_v75"]

app = Client("first_people_bot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.chat(CHANNEL))
async def first_people_detector(client, message):
    if not message.text:
        return

    text = message.text.lower()
    if "first" in text and "people" in text:
        alert = "9134816284 OPAY"  # Your custom message

        for username in ALERT_TO:
            try:
                await client.send_message(username, alert)
                print(f"Alert sent to @{username}")
            except Exception as e:
                print(f"Failed to send to @{username}: {e}")

# Dummy HTTP server to satisfy Render's port binding (runs in background thread)
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")

def run_dummy_server():
    port = int(os.environ.get("PORT", 8080))  # Render sets PORT env var
    server = HTTPServer(("", port), DummyHandler)
    print(f"Dummy server running on port {port}")
    server.serve_forever()

# Start dummy server in thread
threading.Thread(target=run_dummy_server, daemon=True).start()

print("Bot started — monitoring @stunner75trading for 'first' + 'people'...")
app.run()
