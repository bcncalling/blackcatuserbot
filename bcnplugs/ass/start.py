from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bcnplugs import app
from config.config import OWNER_ID

owner_user_id = OWNER_ID

start_text = (
    "Hello! I am your assistant bot.\n"
    "You can use me to perform various tasks.\n"
    "Click the buttons below to explore.\n"
)
user_text = ("Hello iam an assistant bot some others developed by @blackcatserver you can't use this bot due to this bot not your's")
keyboard = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton("Admin commands", callback_data="admin_cmds"),
        ],
        [
            InlineKeyboardButton("Settings", callback_data="settings")
        ]
    ]
)

@app.on_message(filters.command("start"))
async def start_command(app, message):
    user_id = message.from_user.id
    if user_id == owner_user_id:
        await message.reply_text(
            text=start_text,
            reply_markup=keyboard,
        )
    else:
        await message.reply_text(
            text=user_text,
            reply_markup=InlineKeyboardMarkup(
                   InlineKeyboardButton("🔄 Updates", url="https://t.me/blackcatserver"),
                   InlineKeyboardButton("👤 Owner", user_id=f"{owner_user_id}")
            )
        )
                
