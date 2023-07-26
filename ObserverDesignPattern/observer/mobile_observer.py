from .observer_interface import ObserverInterface
from observable.observable_interface import ObservableInterface

class MobileObserver(ObserverInterface):
    observable: ObservableInterface

    def __init__(self, observable: ObservableInterface) -> None:
        self.observable = observable

    def update(self):
        print(f"Received mobile notification from {self.observable} ")
        print(f"Stock count is : {self.observable.get_stock_count()}")
