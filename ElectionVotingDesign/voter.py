from person import Person
from vote import Vote

class Voter:
    person: Person
    vote: Vote

    def __init__(self, person: Person):
        self.person = person

    def cast_vote(self, vote: Vote):
        self.vote = vote
        vote.vote_for.add_vote()