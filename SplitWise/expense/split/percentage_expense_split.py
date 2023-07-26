from .expense_split_interface import ExpenseSplitInterface
from .split import Split

class PercentageExpenseSplit(ExpenseSplitInterface):

    def validate_expense_split(splits: list(Split), amount: float):
        pass