from __future__ import annotations
from datetime import date, datetime
from election_type.election_type_interface import ElectionTypeInterface
from candidate import Candidate
from election_party.party_interface import Party

class Election:
    year: date
    election_type: ElectionTypeInterface
    candidates: list(Candidate)
    election_date: datetime
    winner: Party

    def __init__(self, election_type: ElectionTypeInterface, candidates: list(Party), election_date: date) -> None:
        self.election_type = election_type
        self.parties = self.parties
        self.election_date = election_date

    def declare_winner(self, party: Party):
        self.winner = party
