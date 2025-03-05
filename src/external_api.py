import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv("api_key")

def currency_transfer(transaction: dict) -> float:
    amount = transaction.get("operationAmount", {}).get("amount")
    currency_code = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if currency_code == "RUB":
        return amount
    elif currency_code != "RUB":
        url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}"
        headers = {
            "apikey": api_key
        }
        response = requests.get(url, headers=headers)
        result = response.text
        return float(result)


if __name__ == "__main__":
    print(currency_transfer({
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }))