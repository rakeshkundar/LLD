from __future__ import annotations
from election_party.party_interface import Party
from election_party.bjp_party import BjpParty
from election_party.congress_party import CongressParty
from election_party.independent import Independent
from election_type.election_type_interface import ElectionTypeInterface
from election_type.state_election import StateElection
from election import Election
from datetime import date
from person import Person
from voter import Voter
from election_booth import ElectionBooth
from election_region import ElectionRegion
from election_contest_area_enum import ElectionContestArea
from candidate import Candidate


class ElectionSetup:

    def __init__(self) -> None:
        # Election Parties contesting
        bjp_party: Party = BjpParty()
        congress_party: Party = CongressParty()
        independent_party = Independent()
        parties = [bjp_party, congress_party, independent_party]

        # Persons
        person1 = Person(1, 'Rakesh', date(1999-6-9), 'saralebettu', 'udupi')
        person2 = Person(2, 'Harsha', date(1999-4-28), 'budnar', 'udupi')
        person3 = Person(3, 'Shamanth', date(1999-10-2), 'badagabettu', 'udupi')
        person4 = Person(4, 'Sagar', date(1999-7-2), 'eshwarnagar', 'mangalore')
        person5 = Person(5, 'Abhinav', date(1999-7-30), 'laxmindra nagar', 'mangalore')

        candidate1 = Candidate()

        # Voters
        voter1 = Voter(person1)
        voter2 = Voter(person2)
        voter3 = Voter(person3)
        voter4 = Voter(person4)
        voter5 = Voter(person5)

        # Election Booths
        booth1 = ElectionBooth('Saralebettu')
        booth2 = ElectionBooth('eshwarnagar')
        booth3 = ElectionBooth('bolar')

        # Add Voters to the booth
        booth1.add_voter(voter1)
        booth1.add_voter(voter2)
        booth2.add_voter(voter3)
        booth3.add_voter(voter4)
        booth3.add_voter(voter5)

        # Election Regions
        region1 = ElectionRegion(ElectionContestArea.UDUPI)
        region2 = ElectionRegion(ElectionContestArea.MANGALORE)
        # Election Type
        election_type: ElectionTypeInterface = StateElection()

        election: Election = Election(election_type, parties, date(2023, 5, 10))

