import random
import os
import asyncio
from pyrogram import Client, idle
from bcnplugs import app, client

chat_id = -1002342903276
file = "https://graph.org/file/3203d845588d8a4c01a95.jpg"

async def customize():
    rem = None
    try:
        me = await app.get_me()

        if me.photo:
            return

        print("Customizing Your Assistant Bot in @Botfather")
        UL = f"@{me.username}"
        bcn = me
        if not bcn.username:
            sir = bcn.first_name
        else:
            sir = f"@{bcn.username}"
        msg = await app.send_message(chat_id, "**Auto Customisation** Started on @Botfather")
        await asyncio.sleep(1)
        await client.send_message("botfather", "/cancel")
        await asyncio.sleep(1)
        await client.send_message("botfather", "/setuserpic")
        await asyncio.sleep(1)
        async for message in app.get_chat_history("botfather", limit=1):
            isdone = message.text
        await client.send_photo("botfather", file)
        if isdone.startswith("Invalid bot"):
            print("Error while trying to customize the assistant, skipping...")
            return

        await client.send_message("botfather", UL)
        await asyncio.sleep(1)
        await client.send_document("botfather", file)
        await asyncio.sleep(2)
        await client.send_message("botfather", "/setabouttext")
        await asyncio.sleep(1)
        await client.send_message("botfather", UL)
        await asyncio.sleep(1)
        await client.send_message("botfather", f"✨ Hello ✨!! I'm Assistant Bot of {sir}")
        await asyncio.sleep(2)
        await client.send_message("botfather", "/setdescription")
        await asyncio.sleep(1)
        await client.send_message("botfather", UL)
        await asyncio.sleep(1)
        await client.send_message("botfather", f"Developed and designed by @Blackcatfighters & @blackcatserver")
        await asyncio.sleep(2)
        await msg.edit("Completed **Auto Customisation** at @BotFather.")
        if rem:
            os.remove(file)
        print("Customization Done")
    except Exception as e:
        print(e)
