from __future__ import annotations
from state_interface import State
from item_shelf import ItemShelf
from vending_machine_states.idle import Idle
from coin_enum import Coin


class VendingMachine:
    machine_state: State
    inventory: list(ItemShelf)
    coins_list: None

    def __init__(self, inventory: list(ItemShelf)) -> None:
        self.machine_state = Idle()
        self.inventory = inventory
        self.coins_list = None

    def get_machine_state(self) -> State:
        return self.machine_state

    def change_machine_state(self, state: State) -> None:
        self.machine_state = state

    def create_coin_array(self):
        self.coins_list = list()

    def add_coin(self, coin: Coin):
        self.coins_list.append(coin)

    def get_coins_collected(self):
        return self.coins_list
    
    def return_item(self, id: int):
        for shelf in self.inventory:
            if(shelf.get_item().get_id() == id and not shelf.is_item_sold_out()):
                return shelf

        raise Exception(f'No Stock exits of item id : {id}')