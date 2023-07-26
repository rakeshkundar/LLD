import Vehicle

class VehicleInventoryManagement:
    vehicles_list: list(Vehicle)

class BikeInventoryManagement(VehicleInventoryManagement):
    vehicles_list: list(Vehicle)

class CarInventoryManagement(VehicleInventoryManagement):
    vehicles_list: list(Vehicle)