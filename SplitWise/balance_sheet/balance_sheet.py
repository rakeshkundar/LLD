from __future__ import annotations
from user.user import User
from .balance import Balance


class BalanceSheet:
    user_balance_sheet: dict[User, Balance]
    total_expense: float
    total_payment: float
    total_owe: float
    total_get_back: float

    def __init__(self) -> None:
        self.user_balance_sheet = dict()
        self.total_expense = 0
        self.total_payment = 0
        self.total_owe = 0
        self.total_get_back = 0

    def get_user_balance_sheet(self):
        return self.user_balance_sheet

    def get_total_expense(self):
        return self.total_expense

    def get_total_payment(self):
        return self.total_payment

    def get_total_owe(self):
        return self.total_owe

    def get_total_get_back(self):
        return self.total_get_back

    def update_total_expense(self, amount):
        self.total_expense += amount

    def update_total_payment(self, amount):
        self.total_payment += amount

    def update_total_owe(self, amount):
        self.total_owe += amount

    def update_total_get_back(self, amount):
        self.total_get_back += amount

        