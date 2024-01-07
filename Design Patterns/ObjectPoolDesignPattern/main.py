from __future__ import annotations
from stock_room_pool import StockRoomPool

if __name__ == '__main__':
    pool = StockRoomPool(5)
    print(f"Pool size : {pool.get_size()}")

    stock1 = pool.borrow_object()
    print(f"Stock id : {stock1.get_stock_number()}")

    stock2 = pool.borrow_object()
    print(f"Stock id : {stock2.get_stock_number()}")

    print(f"Pool size : {pool.get_size()}")

    pool.return_object(stock1)

    print(f"Pool size : {pool.get_size()}")

    