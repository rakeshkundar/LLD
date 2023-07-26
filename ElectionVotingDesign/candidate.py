from __future__ import annotations
from person import Person
from election_party.party_interface import Party
from election_contest_area_enum import ElectionContestArea

class Candidate(Person):
    person: Person
    party: Party
    total_votes: int 


    def __init__(self, person: Person, party: Party, contest_area: ElectionContestArea) -> None:
        self.person = person
        self.party = party
        self.contest_area = contest_area
        self.total_votes = 0


    def add_vote(self):
        self.total_votes += 1 

