# Примеры входных данных для проверки функции
# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305

def mask_account_card(data_card: str) -> str:
    """" Функция для зашифровки данных карт и счетов """
    name_of_card = "".join(alpha for alpha in data_card if alpha.isalpha())
    number_of_card = "".join(digit for digit in data_card if digit.isdigit())

    if name_of_card != "Счет":
        return f'{name_of_card} {number_of_card[0:4]} {number_of_card[4:6]}** **** {number_of_card[-4:]}'
    elif name_of_card == "Счет":
        return f'{name_of_card} **{number_of_card[-4:]}'


if __name__ == "__main__":
    print(mask_account_card('Счет 73654108430135874305'))


def get_date(date: str) -> str:
    """ Функция для перевода даты из вида ISO 8601 в привычный европейский"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


if __name__ == "__main__":
    print(get_date('2024-03-11T02:26:18.671407'))
