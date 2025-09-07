
# AG Algo Lab — simple Telegram sender using python-telegram-bot (v21+)

import asyncio
from telegram import Bot
from telegram.error import TelegramError

# WARNING:
# This is a minimal educational example.
# Never hardcode your TOKEN or CHAT_ID in public repositories.
# Always use environment variables (.env file) for security

TG_TOKEN = "XXXXX"
TG_CHAT_ID = XXXXX

async def send_message(text: str):
    bot = Bot(token=TG_TOKEN)
    try:
        await bot.send_message(chat_id=TG_CHAT_ID, text=text)
    except TelegramError as e:
        raise RuntimeError(f"Telegram send failed: {e}") from e

async def send_photo(photo_path_or_url: str, caption: str | None = None):
    bot = Bot(token=TG_TOKEN)
    try:
        if photo_path_or_url.lower().startswith(("http://", "https://")):
            await bot.send_photo(chat_id=TG_CHAT_ID, photo=photo_path_or_url, caption=caption)
        else:
            with open(photo_path_or_url, "rb") as f:
                await bot.send_photo(chat_id=TG_CHAT_ID, photo=f, caption=caption)
    except TelegramError as e:
        raise RuntimeError(f"Telegram photo failed: {e}") from e

async def send_document(file_path: str, caption: str | None = None):
    bot = Bot(token=TG_TOKEN)
    try:
        with open(file_path, "rb") as f:
            await bot.send_document(chat_id=TG_CHAT_ID, document=f, caption=caption)
    except FileNotFoundError:
        raise RuntimeError(f"File not found: {file_path}")
    except TelegramError as e:
        raise RuntimeError(f"Telegram document failed: {e}") from e

# ----------------------------- Execution -------------------------------

asyncio.run(send_message("Hello from python-telegram-bot 🚀"))
