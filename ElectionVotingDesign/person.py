from __future__ import annotations
from datetime import date

class Person:
    id: int
    name: str
    dob: date
    city: str
    address: str

    def __init__(self, id: int, name: str, dob: date, city: str, address: str) -> None:
        self.id = id
        self.name = name
        self.dob = dob
        self.city = city
        self.address = address

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name

    def get_dob(self) -> date:
        return self.dob

    def set_dob(self, dob) -> None:
        self.dob = dob

    def get_city(self) -> str:
        return self.city

    def set_city(self, city) -> None:
        self.city = city

    def get_address(self) -> str:
        return self.address

    def set_address(self, address) -> None:
        self.city = address