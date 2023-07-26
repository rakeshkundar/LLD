from __future__ import annotations
from account import Account
from question import Question
from answer import Answer


class Member:
    account: Account
    badges: list()

    def __init__(self, account: Account) -> None:
        self.account = account
        self.badges = []

    def get_reputation(self):
        return self.account.get_reputation()

    def get_email(self):
        return self.account.get_email()

    def create_question(self, question: Question):
        pass

    def answer_question(self, question: Question, answer: Answer):
        pass

    def add_vote(self):
        pass

    def add_comment(self):
        pass
