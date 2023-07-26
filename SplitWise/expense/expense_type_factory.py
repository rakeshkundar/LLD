from .split_type_enum import SplitType
from split.equal_expense_split import EqualExpenseSplit
from split.unequal_expense_split import UnequalExpenseSplit
from split.percentage_expense_split import PercentageExpenseSplit

class ExpenseTypeFactory:

    @staticmethod
    def get_expense_type_object(split_type: SplitType):
        if(split_type == SplitType.EQUAL):
            return EqualExpenseSplit()
        elif(split_type == SplitType.UNEQUAL):
            return UnequalExpenseSplit()
        elif(split_type == SplitType.PERCENTAGE):
            return PercentageExpenseSplit()
        else:
            raise Exception('Invalid Split Type Passed to ExpenseTypeFactory...')