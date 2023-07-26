from __future__ import annotations
from customer import Customer
from shopping_cart import ShoppingCart
from order import Order

class Guest(Customer):

    def __init__(self, shopping_cart: ShoppingCart, order: Order) -> None:
        super().__init__(shopping_cart, order)

    
    def register(self):
        pass