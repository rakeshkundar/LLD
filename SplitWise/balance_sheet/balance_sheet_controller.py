from user.user import User
from expense.split.split import Split
from .balance import Balance

class BalanceSheetController:
    
    def update_user_balance_sheet(self, paid_by: User, splits: list(Split), total_amount: float):
        paid_user_balance_sheet = paid_by.get_user_balance_sheet()
        paid_user_balance_sheet.update_total_payment(total_amount)

        for split in splits:
            friend = split.user
            friend_balance_sheet = friend.get_user_balance_sheet()
            owe_amount = split.amount

            if(friend == paid_by):
                paid_user_balance_sheet.update_total_expense(owe_amount)
            else:
                if(friend not in paid_user_balance_sheet):
                    paid_user_balance_sheet[friend] = Balance(owe_amount, 0)

                paid_user_balance_sheet[friend].update_credit(owe_amount)

                paid_user_balance_sheet.update_total_get_back(owe_amount)

                if(paid_by not in friend_balance_sheet):
                    friend_balance_sheet[paid_by] = Balance(owe_amount, )

                friend_balance_sheet[paid_by].update_credit(owe_amount)
                    