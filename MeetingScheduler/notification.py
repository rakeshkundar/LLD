from __future__ import annotations
from datetime import datetime
from user import User


class Notification:
    id: str
    message: str
    create_timestamp: datetime

    def __init__(self, id: str, message: str) -> None:
        self.id = id
        self.message = message
        self.create_timestamp = datetime.now()


    def send_notification(self, user: User):
        pass