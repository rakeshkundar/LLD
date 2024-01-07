from drive_strategy.drive_strategy_interface import DriveStrategy

class Vehicle:
    drive_strategy: DriveStrategy

    def __init__(self, strategy: DriveStrategy) -> None:
        self.drive_strategy = strategy

    
    def drive(self):
        self.drive_strategy.drive()