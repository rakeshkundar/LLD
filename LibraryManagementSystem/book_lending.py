from __future__ import annotations
from datetime import datetime

class BookLending:
    creation_date: datetime
    due_date: datetime
    return_date: datetime
    barcode: str
    member_id: str

    def __init__(self, creation_date: datetime, due_date: datetime, return_date: datetime, barcode: str, member_id: str) -> None:
        self.creation_date = creation_date
        self.due_date = due_date
        self.return_date = return_date
        self.barcode = barcode
        self.member_id = member_id

    def lend_book(self):
        pass
    
    def get_lending_details(self, barcode: str):
        pass