import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_initial(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0
    with pytest.raises(ValueError):
        phone.number_of_sim = 5.5

    phone.number_of_sim = 4
    assert phone.number_of_sim == 4
