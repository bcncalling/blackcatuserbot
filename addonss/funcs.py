import random
import os
import asyncio
from pyrogram import Client, idle
from bcnplugs import app, client

chat_id = -1001916479883
file = "https://graph.org/file/84822e7a2cc307659439e.jpg"

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

        # Send commands to BotFather
        await client.send_message("botfather", "/cancel")
        await asyncio.sleep(1)
        await client.send_message("botfather", "/setuserpic")
        await asyncio.sleep(1)

        # Check if customization is successful
        response = await client.get_messages("botfather", limit=1)
        isdone = response[0].text

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

if __name__ == "__main__":
    asyncio.run(customize())
