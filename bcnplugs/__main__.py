import asyncio
import importlib
from pyrogram import Client, idle
from bcnplugs.addons import ALL_MODULES
from bcnplugs import clients, app, ids
from addonss import customize

async def import_modules():
    for all_module in ALL_MODULES:
        try:
            importlib.import_module("bcnplugs.addons" + all_module)
            print(f"Successfully Imported {all_module} 💥")
        except Exception as e:
            print(f"Error importing {all_module}: {str(e)}")

async def start_clients():
    await import_modules()

    for client in clients:
        try:
            await client.start()
            me = await client.get_me()
            await client.join_chat("blackcatub")
            print(f"Started {me.first_name}")
            ids.append(me.id)
        except Exception as e:
            print(f"Error starting a client: {str(e)}")

async def main():
    await start_clients()
    await customize()
    await idle()
    

if __name__ == "__main__":
    asyncio.run(main())

