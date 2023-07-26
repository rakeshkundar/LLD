from __future__ import annotations
from state_interface import State
from vending_machine import VendingMachine
from coin_enum import Coin
from selection import Selection
from idle import Idle

class InsertCoin(State):

    def __init__(self):
        print(f"Machine is in InsertCoin state")

    def insert_money_button(self, machine: VendingMachine):
        raise Exception('Invalid Operation')

    def add_money(self, machine: VendingMachine, coin: Coin):
        machine.add_coin(coin)

    def select_product_button(self, machine: VendingMachine):
        machine.change_machine_state(Selection())

    def select_product():
        raise Exception('Invalid Operation')

    def dispense_product():
        raise Exception('Invalid Operation')

    def return_change():
        raise Exception('Invalid Operation')

    def cancel_product(self, machine: VendingMachine):
        total = sum(machine.get_coins_collected())
        print(f"Order Cancelled!!! Amount Refunded is : {total}")
        machine.change_machine_state(Idle())
        print(f"Machine moved to Idle State")



