from balance_sheet.balance_sheet import BalanceSheet

class User:
    id: int
    name: str
    balance_sheet: BalanceSheet

    def __init__(self, id) -> None:
        self.id = id
        self.name = NameError
        self.balance_sheet = BalanceSheet()
    
    def get_user_id(self):
        return self.id

    def get_user_balance_sheet(self):
        return self.balance_sheet