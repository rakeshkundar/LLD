from user.user import User
from expense.expense import Expense
from expense.expense_controller import ExpenseController


class Group:
    id: int
    name: str
    users: list(User)
    expenses: list(Expense)
    expense_controller: ExpenseController

    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.users = list()
        self.expenses = list()
        self.expense_controller = ExpenseController()

    def add_member(self, user: User):
        self.users.append(user)

    def get_group_id(self):
        return self.id

    