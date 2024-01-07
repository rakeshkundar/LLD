from adaptee.weight_machine import WeightMachine
from .adapter_interface import Adapter

class WeightAdapter(Adapter):
    weight_machine: WeightMachine

    def __init__(self, weight_machine: WeightMachine) -> None:
        self.weight_machine = weight_machine

    
    def get_weight(self):
        weight_in_pounds = self.weight_machine.get_weight()

        return round(weight_in_pounds * 0.453592, 2)