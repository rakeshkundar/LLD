from __future__ import annotations
from datetime import datetime
from accounts.member import Member

class Comment:
    id: str
    text: str
    creation_time: datetime
    flag_count: int
    vote_count: int
    added_by: Member

    def __init__(self, id: str, text: str, added_by: Member) -> None:
        self.id = id
        self.text = text
        self.creation_time = datetime.now()
        self.flag_count = 0
        self.added_by = added_by

    def increment_vote_count(self):
        pass

