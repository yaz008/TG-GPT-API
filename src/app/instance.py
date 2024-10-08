from os import getenv
from dotenv import load_dotenv
from sys import path
from pyrogram import Client

if not load_dotenv():
    raise Exception('Unable to load .env file')
app: Client = Client(name='TG-GPT-API',
                     api_id=getenv(key='API_KEY'),
                     api_hash=getenv(key='API_HASH'),
                     workdir=f'{path[0]}\\app\\__session__')