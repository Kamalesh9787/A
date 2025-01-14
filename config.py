from os import environ

API_ID = int(environ.get("API_ID", "25599491"))
API_HASH = environ.get("API_HASH", "c8e3c0561cf148a6504f27b111fc3698")
BOT_TOKEN = environ.get("BOT_TOKEN", "")

AUTH_CHANNEL = int(environ.get("AUTH_CHANNEL", "-1002053727982"))
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", "-1002037384930"))
ADMINS = int(environ.get("ADMINS", "5983189506"))

# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = environ.get("DB_URI", "")
DB_NAME = environ.get("DB_NAME", "autoacceptbot")

# If this is True Then Bot Accept New Join Request 
NEW_REQ_MODE = bool(environ.get('NEW_REQ_MODE', True))
