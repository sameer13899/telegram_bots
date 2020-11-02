from telethon import TelegramClient, events
from settings import TELEGRAM_API_ID, TELEGRAM_API_HASH
client = TelegramClient('session', api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH)

@client.on(events.NewMessage)
async def my_event_handler(event):
    if 'hello' in event.raw_text:
        await event.reply('hi!')

client.start()
client.run_until_disconnected()