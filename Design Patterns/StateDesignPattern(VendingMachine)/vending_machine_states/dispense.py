from __future__ import annotations
from state_interface import State
from vending_machine import VendingMachine
from coin_enum import Coin
from idle import Idle


class Dispense(State):

    def __init__(self):
        print(f"Machine is in Dispensation State")

    def insert_money_button(self, machine: VendingMachine):
        raise Exception('Invalid Operation')

    def add_money(self, machine: VendingMachine, coin: Coin):
        raise Exception('Invalid Operation')

    def select_product_button(self, machine: VendingMachine):
        raise Exception('Invalid Operation')

    def select_product(self, item_id: int):
        raise Exception('Invalid Operation')

    def dispense_product(self, machine: VendingMachine, itemshelf: ItemShelf):
        print(f"Item shelf : {itemshelf} is Dispensed")
        machine.change_state(Idle())

    def return_change():
        raise Exception('Invalid Operation')

    def cancel_product(self, machine: VendingMachine):
        total = sum(machine.get_coins_collected())
        print(f"Order Cancelled!!! Amount Refunded is : {total}")

        machine.change_machine_state(Idle())
        print(f"Machine moved to Idle State")



