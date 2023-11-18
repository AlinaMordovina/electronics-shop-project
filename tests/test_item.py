"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Планшет", 20000, 10)


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
