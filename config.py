import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN",")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("24606042"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("77dd1e1cfdccd365a7aa3d43e1d9529d")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "7692452477"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("mongodb+srv://voqaloqi:dvvKgtshEfs2vXPC@cluster0.t8m1rep.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "vjsavecontentbot")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
