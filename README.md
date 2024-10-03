# TG GPT API

## Installation

Clone the repository

```sh
git clone https://github.com/yaz008/TG-GPT-API.git
```

Create Python virtual environment, activate it and run

```sh
pip install -r requirements.txt
```

## Usage

Running `src/main.py` file will create a server listening on port `50027` (by default)

It follows a very simple protocol:

-   message length in bytes is encoded into a string of length 16 and sent
-   the message itself is encoded and sent afterwards

Connect your TCP client to the server to start using GPT

## License

TG GPT API is a free, open-source software distributed under the [MIT License](LICENSE.txt)
