from __future__ import annotations

class StockRoom:
    __stock_number: int

    def __init__(self, stock_no: int) -> None:
        self.__stock_number = stock_no

    def get_stock_number(self):
        return self.__stock_number