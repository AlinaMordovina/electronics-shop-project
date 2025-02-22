from src.item import Item


class Phone(Item):
    """Класс для представления группы товара - телефон."""

    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}"\
               f"('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        if isinstance(value, int) and value > 0:
            self.__number_of_sim = value
        else:
            self.__number_of_sim = self.__number_of_sim
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

