from __future__ import annotations
from meeting_room import MeetingRoom
from meeting import Meeting
from datetime import date, datetime
from meeting_room import MeetingRoom

class RoomCalendar:
    meeting_room: MeetingRoom
    meetings: dict[date | list(Meeting)]

    def __init__(self, room: MeetingRoom) -> None:
        self.meeting_room = room
        self.meetings = {}

    def is_room_available(self, capacity: int, start_time: datetime, end_time: datetime):
        if(capacity > self.meeting_room.get_room_capacity()):
            return False

        meeting_date = start_time.date()
        array = self.get_meetings_of_the_day(meeting_date)

        while(start <= end):
            mid = start + (end - start) // 2
            mid_start_time = array[mid].get_meeting_start_time()
            mid_end_time = array[mid].get_meeting_end_time()

            if(end_time <= mid_start_time):
                end = mid - 1
            elif(start_time >= mid_end_time):
                start = mid + 1
            else:
                return False

        return True

    def get_all_room_meetings(self):
        return self.meetings

    def get_meetings_of_the_day(self, meeting_date: date):
        return self.meetings[meeting_date]

    def add_meeting(self, meeting: Meeting):
        start_time = meeting.get_meeting_start_time()
        end_time =  meeting.get_meeting_end_time()
        meeting_date = start_time.date()

        array = self.get_meetings_of_the_day(meeting_date)
        start, end = 0, len(array) - 1

        while(start <= end):
            mid = start + (end - start) // 2
            mid_start_time = array[mid].get_meeting_start_time()
            mid_end_time = array[mid].get_meeting_end_time()

            if(end_time <= mid_start_time):
                end = mid - 1
            elif(start_time >= mid_end_time):
                start = mid + 1
            else:
                raise Exception("Overlapping Meetings encountered")

        meeting_array_index =  0 if (end < 0) else end+1
        self.meetings[meeting_date].insert(meeting_array_index, [start_time, end_time])

    def remove_meeting(self, meeting: Meeting):
        start_time = meeting.get_meeting_start_time()
        end_time =  meeting.get_meeting_end_time()
        meeting_date = start_time.date()

        array = self.get_meetings(meeting_date)
        start, end = 0, len(array) - 1

        while(start <= end):
            mid = start + (end - start) // 2
            mid_start_time = array[mid].get_meeting_start_time()
            mid_end_time = array[mid].get_meeting_end_time()

            if(end_time == mid_end_time and start_time == mid_start_time):
                self.get_meetings(meeting_date).pop(mid)
                print(f"Meeting deleted successfully!!!")
                return
            elif(end_time <= mid_start_time):
                end = mid - 1
            elif(start_time >= mid_end_time):
                start = mid + 1
            else:
                raise Exception("Overlapping Meetings encountered")

    def reschedule_meeting(self, meeting: Meeting):
        self.remove_meeting(meeting)
        self.add_meeting(meeting)

        print(f"Meeting rescheduled successfully!!!")





