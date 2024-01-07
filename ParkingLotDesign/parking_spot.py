from __future__ import annotations
from vehicle_type import VehicleType
from vehicle import Vehicle

class ParkingSpot:
    parking_id: str
    parking_type: VehicleType
    is_free: bool
    parked_vehicle: Vehicle

    def __init__(self, parking_id: str, parking_type: VehicleType) -> None:
        self.parking_id = parking_id
        self.parking_type = parking_type
        is_free = False
        parked_vehicle = None

    def get_parking_id(self):
        return self.parking_id
    
    def get_parking_type(self):
        return self.parking_type
    
    def is_parking_available(self):
        return self.is_free
    
    def park_vehicle(self, vehicle: Vehicle):
        self.park_vehicle = vehicle
        self.is_free = False

    def free_parking(self):
        self.park_vehicle = None
        self.is_free = True
