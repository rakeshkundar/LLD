from __future__ import annotations
from member import Member
from account import Account

class Admin(Member):

    def __init__(self, account: Account) -> None:
        super().__init__(account)

    def block_user(self):
        pass

    def unblock_user(self):
        pass