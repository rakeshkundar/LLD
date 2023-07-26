from __future__ import annotations
from system_enums import AccountStatus
from address import Address
from product import Product
from product_review import ProductReview

class Account:
    username: str
    password: str
    email: str
    phone: str
    name: str
    shipping_address: Address
    account_status: AccountStatus

    def __init__(self, username: str, password: str, email: str, phone: str, name: str, shipping_address: Address, status: AccountStatus) -> None:
        self.username = username
        self.password = password
        self.email = email
        self.phone = phone
        self.name = name
        self.shipping_address = shipping_address
        self.account_status = status

    def get_shipping_address(self) -> Address:
        return self.shipping_address


    def add_product_review(self, review: ProductReview):
        pass

    def add_prodcuct(self, product: Product):
        pass

    def reset_passoword(self):
        pass

