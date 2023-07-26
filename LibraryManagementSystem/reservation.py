from __future__ import annotations
from datetime import datetime

class Reservation:
    creation_date: datetime
    status: str
    book_item_barcode: str
    member_id: str

    def __init__(self, creation_date: datetime, status: str, book_item_barcode: str, member_id: str) -> None:
        self.creation_date = creation_date
        self.status = status
        self.book_item_barcode = book_item_barcode
        self.member_id = member_id

    def get_reservation_details(self, barcode):
        pass
    