from __future__ import annotations
from product_category import ProductCategory

class Product:
    id: int
    name: str
    description: str
    price: float
    category: ProductCategory
    available_item_count: int

    def __init__(self, id: int, name: str, description: str, price: float, category: ProductCategory, count: int) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.available_item_count = count

    def get_available_count(self):
        return self.available_item_count

    def update_product_price(self, price: float):
        self.price = price

    def get_price(self):
        return self.price