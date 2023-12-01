from src.item import Item


class MixinKeyboard:
    """Класс-миксин с дополнительным функционалом."""

    default_language = "EN"

    def __init__(self):
        self.__language = self.default_language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Изменяет язык клавиатуры (EN, RU)."""

        if self.__language == "EN":
            self.__language = "RU"
            return self.__language
        else:
            self.__language = "EN"
            return self.__language


class Keyboard(Item, MixinKeyboard):
    """Класс для представления группы товара - клавиатура."""

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
