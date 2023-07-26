from __future__ import annotations
from product import Product

class Item:
    product: Product
    qty: int
    price: float

    def __init__(self, product: Product, qty: int, price: float) -> None:
        self.product = product
        self.qty = qty
        self.price = price

    def update_quantity(self, qty: int):
        self.qty = qty
        self.price = self.qty * self.product.get_price()

    def get_item_price(self):
        return self.price