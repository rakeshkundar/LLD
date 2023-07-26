from .drive_strategy_interface import DriveStrategy

class NormalDriveStrategy(DriveStrategy):

    def drive(self):
        print("Normal Drive Capability")