from __future__ import annotations
from .split import Split

class ExpenseSplitInterface:

    def validate_expense_split(splits: list(Split), amount: float):
        pass