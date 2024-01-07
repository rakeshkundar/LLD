from car import Car
from null_vehicle import NullVehicle

class VehicleFactory:

    @staticmethod
    def get_vehicle_object(vehicle_type: str):
        if(vehicle_type == 'car'):
            return Car()

        return NullVehicle()