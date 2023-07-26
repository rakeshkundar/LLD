from __future__ import annotations
from shopping_cart import ShoppingCart
from order import Order


class Customer:
    shopping_cart: ShoppingCart
    order: Order

    def __init__(self, shopping_cart: ShoppingCart, order: Order) -> None:
        self.shopping_cart = shopping_cart
        self.order = order

