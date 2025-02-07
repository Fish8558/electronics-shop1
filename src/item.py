import csv
from config import ROOT_DIR
from src.csv_err import InstantiateCSVError


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f"{self.__name}"

    def __add__(self, other):
        """
        Сложение экземпляров одного класса
        """
        if not isinstance(other, self.__class__):
            raise ValueError('Складывать можно только обьекты Item и Phone.')
        return self.quantity + other.quantity

    @property
    def name(self):
        """Getter"""
        return self.__name

    @name.setter
    def name(self, name):
        """Setter"""
        if len(name) <= 10:
            self.__name = name
        else:
            self.__name = name[:10]

    @classmethod
    def instantiate_from_csv(cls, patch_file):
        """класс-метод, инициализирующий экземпляры класса Item"""
        cls.all.clear()
        try:
            with open(patch_file, encoding="windows-1251") as file:
                file_csv = csv.DictReader(file)
                for i in file_csv:
                    name = i['name']
                    price = float(i['price'])
                    quantity = int(i['quantity'])
                    cls(name, price, quantity)
        except KeyError:
            raise InstantiateCSVError('Файл поврежден')
        except FileNotFoundError('Нет такого файла')

    @staticmethod
    def string_to_number(string):
        """Статический метод, возвращающий число из числа-строки."""
        return int(float(string))

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
        self.price = int(self.price * self.pay_rate)
