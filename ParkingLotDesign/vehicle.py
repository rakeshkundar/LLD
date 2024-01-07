from __future__ import annotations
from vehicle_type import VehicleType

class Vehicle:
    vehicle_no: str
    vehicle_type: VehicleType

    def __init__(self, vehicle_no: str, vehicle_type: VehicleType) -> None:
        self.vehicle_no = vehicle_no
        self.vehicle_type = vehicle_type

    def get_vehicle_no(self):
        return self.vehicle_no
    
    def get_vehicle_type(self):
        return self.vehicle_type