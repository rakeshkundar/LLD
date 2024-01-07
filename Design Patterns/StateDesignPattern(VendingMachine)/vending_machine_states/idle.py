from __future__ import annotations
from state_interface import State
from vending_machine import VendingMachine
from insert_coin import InsertCoin

class Idle(State):

    def __init__(self):
        print(f"Machine is in Idle State")

    def insert_money_button(self, machine: VendingMachine):
        machine.create_coin_array()
        machine.change_state(InsertCoin())

    def add_money():
        raise Exception('Invalid Operation')

    def select_product_button():
        raise Exception('Invalid Operation')

    def select_product():
        raise Exception('Invalid Operation')

    def dispense_product():
        raise Exception('Invalid Operation')

    def return_change():
        raise Exception('Invalid Operation')

    def cancel_product():
        raise Exception('Invalid Operation')



