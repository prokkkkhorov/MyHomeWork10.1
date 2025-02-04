def filter_by_state(my_list: list, state='EXECUTED') -> list:
    """
    Функция для сортировки списка словарей по статусу
    """
    return [elem for elem in my_list if elem['state'] == state]


def sort_by_date(my_list: list, reverse=False) -> list:
    """
    Функция для сортировки списка словарей по дате
    """
    return sorted(my_list, key=lambda x: x['date'], reverse=reverse)
