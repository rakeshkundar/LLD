from __future__ import annotations
from room_manager import RoomManager
from notification import Notification
from meeting import Meeting

class MeetingScheduler:
    room_manager: RoomManager

    def __init__(self, room_manager: RoomManager) -> None:
        self.room_manager = room_manager


    def create_meeting(self):
        pass

    def cancel_meeting(self, meeting: Meeting):
        pass

    def reschedule_meeting(self, meeting: Meeting, new_start_time, new_end_time):
        pass