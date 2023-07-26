from __future__ import annotations
from .party_interface import Party

class Independent(Party):

    def __init__(self) -> None:
        self.id = 1
        self.name = "Independent"
        self.candidates = []
        