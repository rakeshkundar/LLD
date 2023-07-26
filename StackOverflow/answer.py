from __future__ import annotations
from datetime import datetime
from photo import Photo
from accounts.member import Member

class Answer:
    answer_text: str
    is_accepted: bool
    vote_count: int
    flag_count: int
    creation_time: datetime
    created_by: Member
    photos: list(Photo)


    def __init__(self, text: str, member: Member):
        self.answer_text = text
        self.is_accepted = False
        self.vote_count = 0
        self.flag_count = 0
        self.creation_time = datetime.now()
        self.creating_member = member
        self.photos = []

    def increment_vote_count(self):
        None