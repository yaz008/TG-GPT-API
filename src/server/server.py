from sys import path
from server._utils import load_config
from socket import socket, AddressFamily, SocketKind
from typing import Callable
from threading import Thread

config: dict[str, str | int] = load_config(path=f'{path[0]}\\server\\config.json')
callback: Callable[[str], None] | None = None
client: socket | None = None

server: socket = socket(family=AddressFamily.AF_INET,
                        type=SocketKind.SOCK_STREAM)
address: tuple[str, int] = (config['host'], config['port'])
server.bind(address)
server.listen()

def receive() -> None:
    global client, callback
    while True:
        try:
            size: int = int(client.recv(16).decode(encoding='UTF-8'))
            message: str = client.recv(size).decode(encoding='UTF-8')
            callback(message)
        except ConnectionResetError as e:
            client = None
            print(e)
            break

def accept() -> None:
    global client
    while True:
        client, _ = server.accept()
        client_thread: Thread = Thread(target=receive)
        client_thread.start()
        print('Connected!')

def send(message: str) -> None:
    global client
    data: bytes = bytes(message, encoding='UTF-8')
    size: bytes = bytes(f'{len(data):16}', encoding='UTF-8')
    client.send(size)
    client.send(data)