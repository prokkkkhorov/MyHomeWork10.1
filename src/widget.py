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
    name_of_card = ''
    number_of_card = ''
    for alpha in data_card:
        if alpha.isalpha():
            name_of_card += alpha
    for digit in data_card:
        if digit.isdigit():
            number_of_card += digit

    if name_of_card != "Счет":
        return f'{name_of_card} {number_of_card[0:4]} {number_of_card[4:6]}** **** {number_of_card[-4:]}'

    if name_of_card == "Счет":
        return f'{name_of_card} **{number_of_card[-4:]}'


if __name__ == "__main__":
    print(mask_account_card('Счет 73654108430135874305'))
