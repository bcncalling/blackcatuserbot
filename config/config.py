import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "14688437")) #optional
API_HASH = getenv("API_HASH", "5310285db722d1dceb128b88772d53a6") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5810389985").split()))
OWNER_ID = int(getenv("OWNER_ID", "5810389985"))
BOT_TOKEN = getenv("BOT_TOKEN", "6399781777:AAHTdczS4K5-rQn6W0N9m-zp-m1vbOiLpVA")

SESSION1 = getenv("SESSION1", "BQF0iCwABQQOtsZ3IFvvegbnp1_yJ34BaNU5t31syfVPueO3WDD3udw-v2SFPNuRtVUNBW2mzpmAyeyr9LNzO-5JTTcGTLs2duUAHyaZ_4isVB53u-cWgfBpyPqQo4eqzqdODH-7s4ta6DnQkLjj3kRrC875QHtT_NQYvOrioGICMqgUFk3dPh66JQn22-dPYrpdrx_01_zQRBjtT9JCoZDTJkbDoVUN6A5Xt3GqjmsytOW469gLvT4osx_RVohWcrf_JHNRakiPN_TGLjQGwF7ptZo3P-apcQgsOmkzD6smJiNsYr1tW222mhm4t45Lg_Q6zPtBoiTsFqJoLgNNQem7Oz-zUwAAAAFaU4PhAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
