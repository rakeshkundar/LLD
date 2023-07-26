class Item:
    id: int
    price: float

    def __init__(self, id: int, price: float) -> None:
        self.id = id
        self.price = price

    def get_price(self) -> float:
        return self.price

    def update_price(self, price: float) -> None:
        self.price = price