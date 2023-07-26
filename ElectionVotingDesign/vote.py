from person import Person
from candidate import Candidate

class Vote:
    vote_by: Person
    vote_for: Candidate

    def __init__(self, vote_by: Person, vote_for: Candidate) -> None:
        self.vote_by = vote_by
        self.vote_for = vote_for