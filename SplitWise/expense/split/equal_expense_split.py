from .expense_split_interface import ExpenseSplitInterface
from .split import Split

class EqualExpenseSplit(ExpenseSplitInterface):

    def validate_expense_split(splits: list(Split), amount: float):
        individual_amount = amount / len(splits)

        for i in range(len(splits)):
            if(splits[i].amount != individual_amount):
                raise Exception('Invalid Equal Expense ....')