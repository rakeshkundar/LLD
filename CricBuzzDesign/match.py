from __future__ import annotations
from team import Team
from datetime import datetime
from match_format.match_type import MatchType
from inning import Inning

class Match:
    team1: Team
    team2: Team
    match_date: datetime
    venue: str
    toss_winner: Team
    innings: list(Inning)
    match_type: MatchType

    def start_match(self) -> None:
        pass

