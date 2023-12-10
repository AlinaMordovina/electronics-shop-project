"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Планшет", 20000, 10)


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_item_initial(item):
    """Проверяем инициализацию экземпляра класса."""

    assert item.name == "Планшет"
    assert item.price == 20000
    assert item.quantity == 10


def test_calculate_total_price(item):
    """Проверяем подщет общей суммы товара"""

    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    """Проверяем применение скидки к товару"""

    item.pay_rate = 0.7
    item.apply_discount()
    assert item.price == 14000


def test_instantiate_from_csv():
    Item.instantiate_from_csv('items_test.csv')
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_instantiate_from_csv_raises():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('item.csv')
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('../tests/items_test.csv')


def test_string_to_number():
    assert Item.string_to_number("5.5") == 5


def test_repr(item):
    assert repr(item) == "Item('Планшет', 20000, 10)"


def test_str(item):
    assert str(item) == 'Планшет'


def test_add(item, phone):
    assert item + phone == 15
    assert item + item == 20
    assert phone + phone == 10
    assert item + 10 == "10 не является экземпляром класса Item."
    assert phone + 23.5 == "23.5 не является экземпляром класса Phone."
