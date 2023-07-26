from __future__ import annotations
from observer.observer_interface import ObserverInterface
from .observable_interface import ObservableInterface

class IphoneObservable(ObservableInterface):
    observers: list(ObserverInterface)
    stock: int

    def __init__(self, observers: list(ObserverInterface), qty: int) -> None:
        self.observers = observers
        self.stock = qty

    def register(self, observer: ObserverInterface):
        self.observers.append(observer)

    def unregister(self,  observer: ObserverInterface):
        self.observers.remove(observer)

    def notify(self):
        # print(f"Came to notify method")
        for observer in self.observers:
            observer.update()

    def increase_stock(self, qty: int):
        # print(f"Stock currently is : {self.stock} and qty received : {qty}")
        send_notification = False
        
        if(self.stock == 0 and qty > 0):
            send_notification = True
        self.stock += qty

        if(send_notification):
            self.notify()

    def decrease_stock(self, qty: int):
        self.stock -= qty

    def get_stock_count(self):
        return self.stock