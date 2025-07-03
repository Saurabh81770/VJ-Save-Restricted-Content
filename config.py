import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN","")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("21974035"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("3cb21442fc659e9eb763629a4e1f546b")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7651547474"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("mongodb+srv://3sonu8177:0FnZW7ZoUvWPNb25@cluster0.yfmr6sp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
