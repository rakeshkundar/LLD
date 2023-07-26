from __future__ import annotations
from candidate import Candidate
from election_contest_area_enum import ElectionContestArea
from election_booth import ElectionBooth

class ElectionRegion:
    region_name: ElectionContestArea
    candidates: list(Candidate)
    election_booths: list(ElectionBooth)

    def __init__(self, region: ElectionContestArea) -> None:
        self.region_name = region
        self.candidates = []
        self.election_booths = []

    def add_candidate(self, candidate: Candidate):
        self.candidates.append(candidate)

    def remove_candidate(self, candidate: Candidate):
        self.candidates.remove(candidate)

    def get_candidates(self):
        return self.candidates

    def add_booth(self, booth: ElectionBooth):
        self.candidates.append(booth)

    def remove_booth(self, booth: ElectionBooth):
        self.candidates.remove(booth)

    def get_booths(self):
        return self.candidates


