from .election_type_interface import ElectionTypeInterface
from .election_type_enum import ElectionType

class CentralElection(ElectionTypeInterface):
    election_type: ElectionType

    def __init__(self) -> None:
        self.election_type = ElectionType.CENTRAL

    def no_of_seats(self):
        return 520