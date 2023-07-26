from __future__ import annotations
from datetime import datetime
from meeting_room import MeetingRoom
from user import User

class Meeting:
    id: str
    title: str
    start_time: datetime
    end_time: datetime
    participants: list(User) #list(R)
    meeting_room: MeetingRoom

    def __init__(self, id: str, title: str, start_time: datetime, end_time: datetime, participants: list, room: MeetingRoom) -> None:
        self.id = id
        self.title = title
        self.start_time = start_time
        self.end_time = end_time
        self.participants = participants
        self.meeting_room = room

    def get_meeting_start_time(self):
        return self.start_time

    def get_meeting_end_time(self):
        return self.end_time


    