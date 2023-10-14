import asyncio
import importlib
from pyrogram import Client, idle
from bcnplugs.addons import ALL_MODULES
from bcnplugs import clients, app, ids
from bcnadds.funcs import customize

async def import_modules():
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("bcnplugs.addons." + all_module)
            print(f"Successfully Imported {all_module} 💥")
        except Exception as e:
            print(f"Error importing {all_module}: {str(e)}")

async def start_clients():
    await app.start()
    print("LOGGER: Token Found booting your BOT")

    await import_modules()  

    for client in clients:
        try:
            await client.start()
            me = await client.get_me()
            await join(client) 
            print(f"Started {me.first_name} 🔥")
            ids.append(me.id)
        except Exception as e:
            print(f"Error starting a client: {str(e)}")

    await idle()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_clients())
    loop.run_until_complete(customize())
