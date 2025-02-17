def mask_account_card(data_card: str) -> str:
    """ Функция для зашифровки данных карт и счетов """
    name_of_card = "".join(alpha for alpha in data_card if alpha.isalpha())
    number_of_card = "".join(digit for digit in data_card if digit.isdigit())

    masked_data_card = ""

    if name_of_card != "Счет":
        masked_data_card = f"{name_of_card} {number_of_card[0:4]} {number_of_card[4:6]}** **** {number_of_card[-4:]}"
    elif name_of_card == "Счет":
        masked_data_card = f"{name_of_card} **{number_of_card[-4:]}"

    return masked_data_card


def get_date(date: str) -> str:
    """ Функция для перевода даты из вида ISO 8601 в привычный европейский """
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"
