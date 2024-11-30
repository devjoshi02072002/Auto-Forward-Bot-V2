from os import environ 

class Config:
    API_ID = environ.get("API_ID", "27944955")
    API_HASH = environ.get("API_HASH", "2e045584d56a1c086d4091a1b02eb36f")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8186269324:AAGd-NiojVHapTQYaIZnepjTOwMRG12jfDc") 
    BOT_SESSION = environ.get("BOT_SESSION", "ethinic") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://devjoshi02072002:gcrmllb5qYr208oY@cluster0.xqf3b.mongodb.net/")
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1370755311').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
