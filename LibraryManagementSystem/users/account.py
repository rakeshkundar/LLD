from __future__ import annotations
from user import User
from account_status_enum import AccountStatus

class Account:
    username: str
    password: str
    user: User
    account_status: AccountStatus

    def __init__(self, username: str, password: str, user: User, account_status: AccountStatus) -> None:
        self.username = username
        self.password = password
        self.user = user
        self.account_status = account_status

    def reset_password(self, password: str):
        self.password = password