from __future__ import annotations
from item import Item

class ItemShelf:
    item: Item
    is_sold_out: bool

    def __init__(self, item: Item) -> None:
        self.item = item
        self.is_sold_out = False

    def get_item(self):
        return self.item

    def is_item_sold_out(self):
        return self.is_sold_out

    def update_item(self, item):
        self.item = item