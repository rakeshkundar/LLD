class Balance:
    amount_owe: float
    amount_credit: float

    def __init__(self, owe: float, credit: float) -> None:
        self.amount_owe = owe
        self.amount_credit = credit

    def get_owe(self):
        return self.amount_owe

    def get_credit(self):
        return self.amount_credit

    def update_owe(self, amount):
        self.amount_owe += amount

    def update_credit(self, amount):
        self.amount_credit += amount