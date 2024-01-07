from __future__ import annotations
from object_pool import ObjectPool
from stock_room import StockRoom
from random import randint

class StockRoomPool(ObjectPool):

    def __init__(self, size: int):
        super().__init__(size)

    
    def create(self):
        stock_no = randint(0, 1000)
        stock_room = StockRoom(stock_no)
        print(f"Creating Stock Room with id : {stock_room.get_stock_number()}")
        return stock_room
    
