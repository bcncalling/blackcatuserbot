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
user_text = ("Hello! I am an assistant bot developed by @blackcatserver. You can't use this bot as it doesn't belong to you.")

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
async def start(app, message):
    user_id = message.from_user.id
    if user_id == owner_user_id:
        await message.reply_text(
            text=start_text,
            reply_markup=keyboard,
        )
    else:
        await message.reply_text(
            text=user_text,
            reply_markup=InlineKeyboardMarkup([
                [
                    InlineKeyboardButton("🔄 Updates", url="https://t.me/blackcatub"),
                    InlineKeyboardButton("👤 Owner", user_id=owner_user_id)
                ]
            ]),
        )
