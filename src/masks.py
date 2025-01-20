def get_mask_card_number(card_number: int) -> str:
    """
    Функция маскировки номера карты
    """
    card_number_str = str(card_number)
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(card_number_account: int) -> str:
    """
    Функция маскировки номера карты при просмотре окна аккаунта
    """
    card_number_account_str = str(card_number_account)
    return f"**{card_number_account_str[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number(7000792289606361))
    print(get_mask_account(73654108430135874305))
