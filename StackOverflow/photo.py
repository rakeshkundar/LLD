from __future__ import annotations
from accounts.member import Member
from datetime import datetime

class Photo:
    id: str
    path: str
    name: str
    created_on: datetime
    added_by: Member

    def __init__(self, id: str, path: str, name: str, created_on: datetime, added_by: Member) -> None:
        self.id = id
        self.path = path
        self.name = name
        self.created_on = created_on
        self.added_by = added_by


    def delete_photo(self):
        pass