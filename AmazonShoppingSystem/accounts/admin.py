from __future__ import annotations
from account import Account


class Admin(Account):
    
    def __init__(self, username: str, password: str, email: str, phone: str) -> None:
        super().__init__(username, password, email, phone)

    def block_user(self):
        pass

    def add_product_category(self):
        pass

    def modify_product_category(self):
        pass