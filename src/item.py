from csv import DictReader


class InstantiateCSVError(Exception):

    def __init__(self, massage):
        self.massage = massage
        super().__init__(self.massage)


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

        if self not in Item.all:
            Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        else:
            return f"{other} не является экземпляром класса {self.__class__.__name__}."

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """

        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_items):
        """Иницииализирует экземпляры класса из файла."""

        cls.all = []

        try:
            with open(file_items, encoding='cp1251') as csv_file:
                file = DictReader(csv_file)

                for element in file:
                    __name = element['name']
                    price = float(element['price'])
                    quantity = int(element['quantity'])
                    cls(__name, price, quantity)

        except FileNotFoundError:
            raise FileNotFoundError(f'Отсутствует файл {file_items}.')
        except KeyError:
            raise InstantiateCSVError(f'Файл {file_items} поврежден.')

    @staticmethod
    def string_to_number(str_num):
        """Возвращает число из числа строки."""

        return int(float(str_num))
