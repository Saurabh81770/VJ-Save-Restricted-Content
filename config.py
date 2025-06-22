import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN","")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("25292226"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("a7d366626f54ca13916a01bd4ef121ab")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7445035418"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("mongodb+srv://vafabol902:5yVC8KLFmWdTLEfy@cluster0.ghld1c1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
