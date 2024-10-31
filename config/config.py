import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "11163590")) #optional
API_HASH = getenv("API_HASH", "fa76f31e5f7a64d906d4978dd0e5d3b3") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7398382204").split()))
OWNER_ID = int(getenv("OWNER_ID", "5750403406"))
BOT_TOKEN = getenv("BOT_TOKEN", "7350463633:AAE-7oHRLStcf6Wc2ccQNmHZ-rHtts8_zDA")

SESSION1 = getenv("SESSION1", "BQDgILUAbQN9pexKBryrY_JQWFRhW2iIvLdUFEhx-aGRXkPj3WuRJ3UchPySJorQq4sibiuYk6fv_U_AGIe1YDb7j3_cZ6hBY0v-VvStWdjCCv1Jk2JKqWIb5eDRSvkOthhj5RYnnLYdJfMORAIt8eHWjGYwLHDvGU4tQ50UdCwQ8INvqIGGhFoCJv48E68vg3X5kdMWTkQYaxKLqu8_EnA69vs8wn5RiLUjIScTub-zitTB2HEwjPwLBrAgkbNNrVnamYEWA2MfZsj0hyM-pe8VxOf90BAynis8CySqX-ADoTwzuPg6FNLaGTmfO9RLISjicilvU9xsoaB02azuL2uw-S0KIgAAAAFWwDFOAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
SESSION11 = getenv("SESSION11", "")
SESSION12 = getenv("SESSION12", "")
SESSION13= getenv("SESSION13", "")
SESSION14 = getenv("SESSION14", "")
SESSION15 = getenv("SESSION15", "")
SESSION16 = getenv("SESSION16", "")
SESSION17 = getenv("SESSION17", "")
SESSION18 = getenv("SESSION18", "")
SESSION19 = getenv("SESSION19", "")
SESSION20 = getenv("SESSION20", "")
