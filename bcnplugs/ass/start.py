from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bcnplugs import app

owner_user_id = 5810389985

start_text = (
    "Hello! I am your assistant bot.\n"
    "You can use me to perform various tasks.\n"
    "Click the buttons below to explore.\n"
)
keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("🔄 Updates", url="https://t.me/blackcatserver"),
            InlineKeyboardButton("👤 Owner", callback_data=f"user_id={owner_user_id}"),
        ]
    ]
)

@app.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        text=start_text,
        reply_markup=keyboard,
    )
