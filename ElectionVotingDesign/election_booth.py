from __future__ import annotations
from voter import Voter

class ElectionBooth:
    booth_name: str
    voters: list(Voter)

    def __init__(self, booth_name: str) -> None:
        self.booth_name = booth_name
        self.voters = []

    def add_voter(self, voter: Voter):
        self.voters.add(voter)

    def remove_voter(self, voter: Voter):
        self.voters.remove(voter)
