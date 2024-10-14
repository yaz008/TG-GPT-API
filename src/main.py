from app import app
from pyrogram.client import Client
from pyrogram.filters import user
from pyrogram.types import Message
from threading import Thread
from server import server
from spam import is_spam

GPT: str = '@GPT_chat_robot'

def callback(message: str) -> str:
    app.send_message(chat_id=GPT, text=message)

@app.on_message(filters=user(GPT))
def on_message(_: Client, message: Message) -> None:
    if is_spam(message=message):
        message.delete()
    else:
        if message.text is not None:
            server.send(message=message.text)

if __name__ == '__main__':
    server.callback = callback
    Thread(target=server.accept).start()
    app.run()