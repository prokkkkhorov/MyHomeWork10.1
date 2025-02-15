import pytest

@pytest.fixture()
def card_number_func():
    return '7000 79** **** 6361'


@pytest.fixture()
def mask_account_func():
    return '**4305'


@pytest.fixture()
def get_date_func():
    return '11.03.2024'
