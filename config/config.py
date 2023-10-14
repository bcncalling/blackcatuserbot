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

SESSION1 = getenv("SESSION1", "BQF0iCwAjA4bq0Znf_dmEsQxJ-8r6ddrXvxylFSE8yr0yjHgPBW4c8mGb_8NdBJaW1d258f7mhQQQ2PtWbFYLIJOa6zaHrgAmnimdugQPZDjQ_f8AU_jYF0nf68q0yRPCjyzEP1m_K8suDcmVPD3jX52rIuzR8cstc8GTz5MJHpR5KJJmCD9iuPEKrFit-Qej1iuNImyH4WhKq2hlFiXTTAA9_M3YB65UMpEu2Cn0pqfSAYL8Q3WUfTqLIEArbSOEbn0hrcN0TuvTbFV3Kasvibv31TaCnHnVe0y_zpqVDQICN9k8p0dy6qDhBa4VgKuI-dyNeYEYpOMGYPTvqmxUt8Prk9YhwAAAAFaU4PhAA")
SESSION2 = getenv("SESSION2", "")
SESSION3 = getenv("SESSION3", "")
SESSION4 = getenv("SESSION4", "")
SESSION5 = getenv("SESSION5", "")
SESSION6 = getenv("SESSION6", "")
SESSION7 = getenv("SESSION7", "")
SESSION8 = getenv("SESSION8", "")
SESSION9 = getenv("SESSION9", "")
SESSION10 = getenv("SESSION10", "")
