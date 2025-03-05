import random

def filter_by_currency(list_of_transactions: list, currency: str) -> str:
    """
    Функция должна возвращать итератор, который поочередно выдает транзакции,
    где валюта операции соответствует заданной.
    """
    for elem in list_of_transactions:
        if elem["operationAmount"]["currency"]["code"] == currency:
            yield elem


def transaction_descriptions(list_of_transactions: list) -> str:
    """
    Функция принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди.
    """
    for elem in list_of_transactions:
        yield elem["description"]


def card_number_generator(start: int, stop: int) -> str:
    """
    Функция для генерации номера карты
    """
    for number in range(start, stop + 1):
        card_number = f"{number:0>16}"
        yield f"{card_number[:4]} {card_number[4:8]} {card_number[8:12]} {card_number[12:]}"
