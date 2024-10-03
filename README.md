# TG-GPT-API

## Installation

Clone the repository

```sh
git clone https://github.com/yaz008/TG-GPT-API.git
```

Create Python virtual environment, activate it and run

```sh
pip install -r requirements.txt
```

Create `.env` file with the following environment variables

```env
API_KEY="your-api-key"
API_HASH="your-api-hash"
```

**Note:** If you have no idea what `API_KEY` and `API_HASH` are, check out the official [Telegram Documentation](https://core.telegram.org/api/obtaining_api_id)

## Usage

Running `src/main.py` file will create a server listening on port `50027` (by default)

**Protocol:**

1. 16 bytes header (message length)
2. Message (in UTF-8)

Connect your TCP client to the server to start using GPT

### Testing

To test if everything is installed correctly, run the server an connect to it with this client

```python
from socket import socket, AddressFamily, SocketKind

SERVER_ADDRESS = ('localhost', 50027)
ENCODING: str = 'UTF-8'

def send(message: str) -> None:
    data: bytes = message.encode(encoding=ENCODING)
    size: bytes = f'{len(data):16}'.encode(encoding=ENCODING)
    _ = client.send(size)
    _ = client.send(data)

def receive() -> str:
    size: int = int(client.recv(16).decode(encoding=ENCODING).strip())
    data: str = client.recv(size).decode(encoding=ENCODING)
    return data

if __name__ == "__main__":
    with socket(family=AddressFamily.AF_INET,
                type=SocketKind.SOCK_STREAM) as client:
        client.connect(SERVER_ADDRESS)

        message: str = input('user> ')
        send(message=message)
        response: str = receive()
        print(f"server> {response}")
```

### Recomended

Create a task in [Task Sceduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) that will run the server indefinitely starting at user logon

Thus, all projects that rely on this server will function correctly

## License

TG-GPT-API is a free, open-source software distributed under the [MIT License](LICENSE.txt)
