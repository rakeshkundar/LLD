from .drive_strategy_interface import DriveStrategy

class SportyDriveStrategy(DriveStrategy):

    def drive(self):
        print("Sport Drive Capability")