from split.split import Split
from .split_type_enum import SplitType
from expense_type_factory import ExpenseTypeFactory
from expense import Expense
from user.user import User

class ExpenseController():

    def createExpense(self, id: str, desc: str, amount: float, splits: list(Split), split_type: SplitType, paid_by: User):
        expense_split = ExpenseTypeFactory.get_expense_type_object(split_type)
        expense_split.validate_expense_split(splits, amount)

        expense = Expense(id, desc, amount, paid_by, split_type, splits)

        return expense