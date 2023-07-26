from __future__ import annotations
from .party_interface import Party
from election_candidate.candidate_interface import CandidateInterface

class AamParty(Party):
    candidates: list(CandidateInterface)

    def __init__(self) -> None:
        self.id = 3
        self.name = "Aam Aadmi Party"
        self.candidates = []

    def add_candidate(self, candidate: CandidateInterface):
        self.candidates.append(candidate)

    def list_candidates(self):
        print(f"{self.name} candidates are : ")

        for candidate in self.candidates:
            print(f"In Election Region {candidate.election_region} candidate is {candidate.name}")

    def remove_candidate(self, candidate: CandidateInterface):
        self.candidates.remove(candidate)
        