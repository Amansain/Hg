import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6473757387:AAGNghL5FDdt0w1XM4wwKsYG1L6FcLaKQ2c")

API_ID = int(os.environ.get("API_ID", "8540740"))

API_HASH = os.environ.get("API_HASH", "76d20ed4f2e657e4ad0609ca1f8eef79")

STRING = os.environ.get("STRING", "")



bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
