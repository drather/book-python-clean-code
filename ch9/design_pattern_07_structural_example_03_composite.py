from types import Union
from typing import Iterable


class Product:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def price(self):
        return self._price


class ProductBundle:
    def __init__(self, name, percent_discount, *products: Iterable[Union[Product, "ProductBundle"]]) -> None:
        self._name = name
        self._percent_discount = percent_discount
        self._products = products

    @property
    def price(self):
        total = sum(p.price for p in self._products)
        return total * (1 - self._percent_discount)