from .drive_strategy_interface import DriveStrategy

class OffRoadDriveStrategy(DriveStrategy):

    def drive(self):
        print("Off Road Drive Capability")