from vehicle import Vehicle
from drive_strategy.drive_strategy_interface import DriveStrategy
from drive_strategy.normal_drive_strategy import NormalDriveStrategy
from drive_strategy.off_road_drive_strategy import OffRoadDriveStrategy
from drive_strategy.sporty_drive_strategy import SportyDriveStrategy


if __name__ == '__main__':
    strategy: DriveStrategy = SportyDriveStrategy() # NormalDriveStrategy()
    vehicle: Vehicle = Vehicle(strategy)
    vehicle.drive()