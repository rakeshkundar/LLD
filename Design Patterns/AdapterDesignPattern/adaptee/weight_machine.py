class WeightMachine:
    weight: float  # Weight in pound

    def __init__(self, weight: float) -> None:
        self.weight = weight

    
    def get_weight(self):
        return self.weight