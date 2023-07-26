from __future__ import annotations
from split_type_enum import SplitType
from split import Split
from user.user import User

class Expense:
    expense_id: int
    description: str
    amount: float
    paid_by: User
    split_type: SplitType
    splits: list(Split)

    def __init__(self, id: int, desc: str, amount: float, paid_by: User, split_type: SplitType, splits: list(Split)) -> None:
        self.expense_id = id
        self.description = desc
        self.amount = amount
        self.paid_by - paid_by
        self.split_type = split_type
        self.splits = splits
