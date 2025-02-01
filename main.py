# Примеры входных данных для проверки функции
# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    masked_card = get_mask_card_number(7000792289606361)
    masked_account = get_mask_account(73654108430135874305)

    print(masked_card)
    print(masked_account)

    masked_account_card = mask_account_card('Visa Platinum 8990922113665229')
    reform_date = get_date('2024-03-11T02:26:18.671407')

    print(masked_account_card)
    print(reform_date)
