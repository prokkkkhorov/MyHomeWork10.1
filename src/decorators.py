from time import time
from typing import Optional, Callable

def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для расчета времени выполнения функции и вывода
    результатов в консоль и текстовый "mylog.txt" файл, а также для
    вывода ошибок в консоль или "mylog.txt" файл, в случае неправильной работы функции
    """
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            try:
                time_before = time()
                result = func(*args, **kwargs)
                time_after = time()
                duration = time_after - time_before
                message = f"{func.__name__} ok\n"
                if not filename:
                    print(message)
                else:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(message)
                return result
            except Exception as e:
                message = f"{func.__name__} {type(e).__name__}. Inputs {args}, {kwargs}\n"
                if not filename:
                    print(message)
                else:
                    with open(filename, 'a', encoding='utf-8') as file:
                        file.write(message)
                raise e
        return wrapper
    return my_decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


# print(my_function(1, 2))
