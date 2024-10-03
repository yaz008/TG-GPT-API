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

## Usage

Running `src/main.py` file will create a server listening on port `50027` (by default)

**Protocol:**

1. 16 bytes header (message length)
2. Message (in UTF-8)

Connect your TCP client to the server to start using GPT

### Recomended

Create a task in [Task Sceduler](https://learn.microsoft.com/en-us/windows/win32/taskschd/task-scheduler-start-page) that will run the server indefinitely starting at user logon

Thus, all projects that rely on this server will function correctly

## License

TG-GPT-API is a free, open-source software distributed under the [MIT License](LICENSE.txt)
