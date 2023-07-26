from __future__ import annotations

class MeetingRoom:
    id: int
    name: str
    capacity: int

    def __init__(self, id: int, name: str, capacity: int) -> None:
        self.id = id
        self.name = name
        self.capacity = capacity

    def get_room_name(self):
        return self.name

    def get_room_capacity(self):
        return self.capacity

    def get_room_id(self):
        return self.id