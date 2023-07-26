from .expense_split_interface import ExpenseSplitInterface
from .split import Split

class UnequalExpenseSplit(ExpenseSplitInterface):

    def validate_expense_split(splits: list(Split), amount: float):
        total_amount = 0

        for i in range(len(splits)):
            total_amount += splits[i].amount
        
        if(total_amount != amount):
            raise Exception("Invalid Unequal Expense ...")