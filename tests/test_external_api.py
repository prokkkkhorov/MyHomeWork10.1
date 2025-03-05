import pytest
from src.external_api import currency_transfer
from unittest.mock import patch

@patch("requests.get")
def test_currency_transfer(mock_get):
    mock_get.return_value.text = 1.0
    assert currency_transfer({
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
  }) == 1.0