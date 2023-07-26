from __future__ import annotations
from .party_interface import Party

class BjpParty(Party):

    def __init__(self) -> None:
        self.id = 2
        self.name = "BJP Party"
        