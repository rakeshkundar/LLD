from __future__ import annotations
from .user import User

class UserController:
    users: list(User)

    def __init__(self) -> None:
        self.users = list()

    def add_user(self, user: User):
        self.users.append(user)

    def get_user(self, user_id: int):
        for index, user in enumerate(self.users):
            if(user.id == user_id):
                return user

        raise Exception('No User exists ....')

    def get_all_users(self):
        return self.users

    