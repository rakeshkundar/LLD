from __future__ import annotations


class Address:
    building: str
    street: str
    city: str
    state: str
    country: str
    pincode: str

    def __init__(self, building: str, street: str, city: str, state: str, country: str, pincode: str) -> None:
        self.building = building
        self.street = street
        self.city = city
        self.state = state
        self.country = country
        self.pincode = pincode