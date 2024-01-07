from __future__ import annotations
from parking_spot import ParkingSpot
from datetime import datetime

class Ticket:
    ticket_id: str
    parking_spot: ParkingSpot
    entry_time: datetime

    def __init__(self, ticket_id: str, parking_spot: ParkingSpot) -> None:
        self.ticket_id = ticket_id
        self.parking_spot = parking_spot
        self.entry_time = datetime.now()

    def get_entry_time(self):
        return self.entry_time