from __future__ import annotations
from account import Account
from customer import Customer


class Member(Customer):

    account: Account
    def __init__(self, username: str, password: str, email: str, phone: str, account: Account) -> None:
        super().__init__(username, password, email, phone)
        self.account = account

    
    def place_order(self):
        pass