from pizza.base_pizza_interface import BasePizzaInterface
from pizza.margerith import Margerith
from pizza.veg_delight import VegDelight
from toppings.toppings_interface import ToppingsInterface
from toppings.mushroom import Mushroom
from toppings.extra_cheese import ExtraCheese


if __name__ == '__main__':
    pizza1: ToppingsInterface = ExtraCheese(Mushroom(Margerith()))
    pizza2: ToppingsInterface = ExtraCheese(Mushroom(VegDelight()))

    print(f"Pizza 1 cost : {pizza1.cost()}")
    print(f"Pizza 2 cost : {pizza2.cost()}")