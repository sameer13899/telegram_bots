from telethon import TelegramClient, events
from settings import TELEGRAM_API_ID, TELEGRAM_API_HASH, COMBINATIONS

client = TelegramClient('session', api_id=TELEGRAM_API_ID, api_hash=TELEGRAM_API_HASH)
@client.on(events.NewMessage)
async def my_event_handler(event):
    sender_chat_id = event.sender_id
    if sender_chat_id in list(COMBINATIONS.keys()):
        msg_text = event.raw_text
        contains_blacklisted_word = False
        blacklisted_words = COMBINATIONS.get(sender_chat_id).get("blacklists")
        for word in blacklisted_words:
            if word in msg_text:
                contains_blacklisted_word = True
        contains_whitelisted_word = False
        whitelisted_words = COMBINATIONS.get(sender_chat_id).get("whitelists")
        for word in whitelisted_words:
            if word in msg_text:
                contains_whitelisted_word = True
        if not contains_blacklisted_word and contains_whitelisted_word:
            destination_chat_ids = COMBINATIONS.get(sender_chat_id).get("destinations")
            for chat_id in destination_chat_ids:
                await client.send_message(chat_id,event.raw_text)
client.start()
client.run_until_disconnected()