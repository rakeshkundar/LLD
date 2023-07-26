from __future__ import annotations
from state_interface import State
from vending_machine import VendingMachine
from coin_enum import Coin
from idle import Idle
from dispense import Dispense
from item_shelf import ItemShelf


class Selection(State):

    def __init__(self):
        print(f"Machine is in ItemSelection State")

    def insert_money_button(self, machine: VendingMachine):
        raise Exception('Invalid Operation')

    def add_money(self, machine: VendingMachine, coin: Coin):
        raise Exception('Invalid Operation')

    def select_product_button(self, machine: VendingMachine):
        raise Exception('Invalid Operation')

    def select_product(self, machine: VendingMachine, item_id: int):
        try:
            item_shelf = machine.return_item(id)
            price = item_shelf.get_item().get_price()
            money_collected = sum(machine.get_coins_collected())

            if(price > money_collected):
                self.refund_full_amount(machine)
            elif(money_collected > price):
                self.return_change(money_collected - price)

        except Exception as e:
            print(e)
            machine.change_machine_state(Idle())
    
    def refund_full_amount(self, machine: VendingMachine):
        print(f"Full Amount refunded!!!")
        machine.change_machine_state(Idle())
    
    def dispense_product(self, machine: VendingMachine, item_shelf: ItemShelf):
        machine.change_machine_state(Dispense())

    def return_change(self, change: float):
        print(f"Change returned : {change}")

    def cancel_product(self, machine: VendingMachine):
        total = sum(machine.get_coins_collected())
        print(f"Order Cancelled!!! Amount Refunded is : {total}")
        machine.change_machine_state(Idle())
        print(f"Machine moved to Idle State")



