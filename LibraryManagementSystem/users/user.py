from __future__ import annotations

class User:
    id : str
    name: str
    phone_number: str
    email: str

    def __init__(self, id: str, name: name, phone_number: str, email: str, address: str) -> None:
        self.id = id
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address