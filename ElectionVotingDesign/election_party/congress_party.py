from __future__ import annotations
from .party_interface import Party

class CongressParty(Party):

    def __init__(self) -> None:
        self.id = 1
        self.name = "Congress Party"
        