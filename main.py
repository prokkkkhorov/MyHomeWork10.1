# Примеры входных данных для проверки функции
# Maestro 1596837868705199
# Счет 64686473678894779589
# MasterCard 7158300734726758
# Счет 35383033474447895560
# Visa Classic 6831982476737658
# Visa Platinum 8990922113665229
# Visa Gold 5999414228426353
# Счет 73654108430135874305

list_of_dict = [
{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
{'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
{'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]

from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card
from src.processing import filter_by_state, sort_by_date

if __name__ == "__main__":
    masked_card = get_mask_card_number(7000792289606361)
    masked_account = get_mask_account(73654108430135874305)

    print(masked_card)
    print(masked_account)

    masked_account_card = mask_account_card('Счет 73654108430135874305')
    reform_date = get_date('2024-03-11T02:26:18.671407')

    print(masked_account_card)
    print(reform_date)

    filter_by_state_main = filter_by_state(list_of_dict)
    sorted_date = sort_by_date(list_of_dict)

    print(filter_by_state_main)
    print(sorted_date)
