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

SESSION1 = getenv("SESSION1", "AQF0iCwAF_OscRVtoaAdzcAijFxSFfxlKLHpL-OP3i0Uamb1-59zV_0-2slJ25f_AoGSsVzkLmR0u221K9zplxvDsuqCUVVsrPNoNwkwmZY9A3varyrMkFZzhcUlii39uygV45FCdpFtERZvwFE3UtLhgEIQlyZhSmU0fAJ8T3mnMVIoTuBhEQ38BU45kFVIKOy4cf9lp8032KTTAeX8_N-duw_uQAc4b2lG5Z54CRlQcxVUWoHomFagFuvaFYICzxFTOoxmc7tT631Q3AzwTuKkPdz5tUEL0uMxD5i5GbfDzwV1bhMU0lNsOyDjjUC17Q2nwMSw-hPVeeCQ-INI5dihAbDIAgAAAAFDBECWAA")
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
