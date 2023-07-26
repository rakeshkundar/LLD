from datetime import datetime

class Notification:
    id: str
    created_on: datetime
    message: str

    def __init__(self, id: str, created_on: datetime, message: str) -> None:
        self.id = id
        self.created_on = created_on
        self.message = message


    def send_notification(self):
        pass