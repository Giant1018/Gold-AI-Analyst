from telegram import Bot
import asyncio

# Replace these with your own values
BOT_TOKEN = 8845398374:AAHHERfZZPlnNcWxAh_XKRjePvK5p10SNwo
CHAT_ID = "5267781738"

async def send_message():
    bot = Bot(token=BOT_TOKEN)
    await bot.send_message(
        chat_id=CHAT_ID,
        text="✅ Gold AI Analyst is now online!"
    )

asyncio.run(send_message())
