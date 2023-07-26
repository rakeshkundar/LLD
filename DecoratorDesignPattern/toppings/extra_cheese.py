from .toppings_interface import ToppingsInterface
from pizza.base_pizza_interface import BasePizzaInterface

class ExtraCheese(ToppingsInterface):
    base_pizza: BasePizzaInterface

    def __init__(self, base_pizza: BasePizzaInterface) -> None:
        self.base_pizza = base_pizza

    def cost(self):
        return self.base_pizza.cost() + 20