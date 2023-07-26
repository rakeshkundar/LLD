from __future__ import annotations
from .election_type_interface import ElectionTypeInterface
from .election_type_enum import ElectionType
from election_region import ElectionRegion

class StateElection(ElectionTypeInterface):
    election_type: ElectionType
    election_regions: list(ElectionRegion)

    def __init__(self, election_regions: list(ElectionRegion)) -> None:
        self.election_type = ElectionType.STATE
        self.election_regions = election_regions

    def no_of_seats(self):
        return len(self.election_regions)

    def add_region(self, region: ElectionRegion) -> None:
        self.election_regions.append(region)

    def remove_region(self, region: ElectionRegion) -> None:
        self.election_regions.remove(region)