from __future__ import annotations
from item import Item

class ShoppingCart:
    items: list(Item)

    def __init__(self) -> None:
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def remove_item(self, item: Item):
        self.items.pop(item)

    def update_item_quantity(self, item: Item, qty: int):
        item.update_quantity(qty)

    def get_items(self):
        return self.items

    def get_total_items_cost(self):
        cost = 0.0
        for item in self.items:
            cost += item.get_item_price()
        return cost