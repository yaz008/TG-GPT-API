from json import load

def load_config(path: str) -> dict[str, str | int]:
    with open(file=path, mode='r', encoding='UTF-8') as config:
        return load(config)