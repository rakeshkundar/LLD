from __future__ import annotations

class User:
    username: str
    email: str

    def __init__(self, username: str, email: str) -> None:
        self.username = username
        self.email = email
        