def filter_by_state(my_list: list, state='EXECUTED') -> list:
    return [elem for elem in my_list if elem['state'] == state]


def sort_by_date(my_list: list, reverse=False) -> list:
    return sorted(my_list, key=lambda x: x['date'], reverse=reverse)
