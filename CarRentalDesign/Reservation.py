from datetime import datetime
import Vehicle
import User
import ReservationStatus

class Reservation:
    id: int
    user: User
    vehicle: Vehicle
    booking_date: datetime
    booking_from: datetime
    status: ReservationStatus