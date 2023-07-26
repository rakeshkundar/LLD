import VehicleType
import VehicleStatus

class Vehicle:
    vehicle_no: str
    vehilce_type: VehicleType
    daily_rental_cost: float
    hourly_rental_cost: float
    seats: int
    status: VehicleStatus


class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass