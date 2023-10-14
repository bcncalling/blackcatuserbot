from pyrogram import Client
from config.config import (API_ID, API_HASH, 
                    SUDO_USERS, OWNER_ID, 
                    BOT_TOKEN, SESSION1,  
                    SESSION2, SESSION3,  
                    SESSION4, SESSION5, 
                    SESSION6, SESSION7, 
                    SESSION8, SESSION9, 
                    SESSION10)
from datetime import datetime
import time
from aiohttp import ClientSession

clients = []
ids = []

app = Client(
    name="bcn",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bcnplugs/ass"),
    in_memory=True,
)
clients.append(app)

for session in [SESSION1, 
                       SESSION2, 
                       SESSION3, 
                       SESSION4, 
                       SESSION5, 
                       SESSION6, 
                       SESSION7, 
                       SESSION8, 
                       SESSION9, 
                       SESSION10]:
    if session:
        client = Client(
            name="blackcat", 
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session,
            plugins=dict(root="bcncalls/addons"),
        )
        clients.append(client)
        print(f"Client: {len(session)} - Starting")
