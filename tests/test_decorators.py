import pytest

from src.decorators import log

def test_log_error_console(capsys):

    @log()
    def foo(x, y):
        return x + y

    with pytest.raises(TypeError):
        foo(1, "2")

    message = capsys.readouterr()
    assert "foo TypeError. Inputs (1, '2'), {}" in message.out

def test_log_file_success(capsys):

    @log(filename="mylog.txt")
    def foo(x, y):
        return x + y

    foo(1, 2)
    with open("mylog.txt", "r",encoding="utf-8") as file:
        all_lines = file.readlines()
        message = all_lines[-1]
    assert message == "foo ok\n"
