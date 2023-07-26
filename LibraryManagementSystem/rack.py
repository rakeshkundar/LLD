from __future__ import annotations

class Rack:
    id: int
    row: int

    def __init__(self, id: int, row: int) -> None:
        self.id = id
        self.row = row

    def get_id(self) -> int:
        return self.id
    
    def get_row(self) -> int:
        return self.row

    def set_id(self, id: int) -> int:
        self.id = id

    def set_row(self, row: int) -> int:
        self.row = row

