from adaptee.weight_machine import WeightMachine
from adapter.weight_adapter import WeightAdapter


if __name__ == '__main__':
    weight_machine: WeightMachine = WeightMachine(30)
    weight_adapter: WeightAdapter = WeightAdapter(weight_machine)

    print(f"Weight in Pounds : {weight_machine.get_weight()}")
    print(f"Weight in Kilos  : {weight_adapter.get_weight()}")