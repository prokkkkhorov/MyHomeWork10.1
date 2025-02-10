from src.masks import get_mask_card_number, get_mask_account


def test_get_mask_card_number(card_number_func):
    """
    Функция для тестирования маскировки номера карты из модуля masks.py
    """
    assert get_mask_card_number(7000792289606361) == card_number_func

def test_get_mask_account(mask_account_func):
    """
    Функция для тестирования маскировки номера карты
    при просмотре окна аккаунта из модуля masks.py
    """
    assert get_mask_account(73654108430135874305) == mask_account_func
