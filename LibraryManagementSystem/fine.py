from __future__ import annotations
from datetime import datetime

class Fine:
    creation_date: datetime
    barcode: str
    member_id: str

    def __init__(self, creation_date: datetime, barcode: str, member_id: str) -> None:
        self.creation_date = creation_date
        self.barcode = barcode
        self.member_id = member_id

    def calculate_fine(self, member_id: str, days: int):
        pass