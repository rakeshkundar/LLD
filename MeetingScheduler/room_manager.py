from __future__ import annotations
from meeting_room import MeetingRoom
from room_calendar import RoomCalendar

class RoomManager:
    rooms: list(MeetingRoom)
    room_calendars: dict[str | RoomCalendar] # {room_id: RoomCalendar}

    def create_meeting(self):
        pass

    def check_all_rooms_available_for_meeting(self, start_time, end_time, capacity):
        available_rooms = []

        for room in self.rooms:
            room_id = room.get_room_id()

            if(self.room_calendars[room_id].is_room_available(capacity, start_time, end_time)):
                available_rooms.append(room)

        return available_rooms

    