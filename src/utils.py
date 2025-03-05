import os
import json
import requests
from json import JSONDecodeError
from dotenv import load_dotenv


def parse_data(parse: str) -> list[dict]:
    try:
        with open(parse, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        return []
    except JSONDecodeError:
        return []

if __name__ == "__main__":
    parse = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "operations.json")
    print(parse_data(parse))