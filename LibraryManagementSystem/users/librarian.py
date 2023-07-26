from __future__ import annotations
from account import Account
from user import User
from account_status_enum import AccountStatus

class Librarian(Account):

    def __init__(self, username: str, password: str, user: User) -> None:
        super().__init__(username, password, user, AccountStatus.ACTIVE)

    def add_book_item(self):
        pass

    def block_member(self):
        pass

    def unblock_member(self):
        pass
