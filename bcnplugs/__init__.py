from pyrogram import Client, idle
from config.config import (API_ID, API_HASH, 
                    SUDO_USERS, OWNER_ID, 
                    BOT_TOKEN, SESSION1,  
                    SESSION2, SESSION3,  
                    SESSION4, SESSION5, 
                    SESSION6, SESSION7, 
                    SESSION8, SESSION9, 
                    SESSION10, SESSION11, 
                    SESSION12, SESSION13, 
                    SESSION14, SESSION15, 
                    SESSION16, SESSION17, 
                    SESSION18, SESSION19, 
                    SESSION20)
from datetime import datetime
import time
from aiohttp import ClientSession

clients = []
ids = []

app = Client(
    "bcn_ass",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="bcnplugs/ass"),
    in_memory=True,
)
app.start() 

session_list = [SESSION1, SESSION2, 
                SESSION3, SESSION4, 
                SESSION5, SESSION6, 
                SESSION7, SESSION8, 
                SESSION9, SESSION10,
                SESSION11, SESSION12, 
                SESSION13, SESSION14, 
                SESSION15, SESSION16, 
                SESSION17, SESSION18, 
                SESSION19, SESSION20]

for i, session in enumerate(session_list, 1):
    if session:
        client = Client(
            f"blackcat_{i}",
            api_id=API_ID,
            api_hash=API_HASH,
            session_string=session,
            plugins=dict(root="bcnplugs/addons"),
        )
        clients.append(client)  # Append the client to the list
        print(f"Client {i} - Starting")
