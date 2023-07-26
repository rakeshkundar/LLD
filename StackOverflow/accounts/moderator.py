from __future__ import annotations
from member import Member
from account import Account

class Moderator(Member):

    def __init__(self, account: Account) -> None:
        super().__init__(account)

    def close_question(self):
        pass

    def undelete_question(self):
        pass