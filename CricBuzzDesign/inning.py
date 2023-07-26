from team import Team
from over import Over

class Inning:
    batting_team: Team
    bowling_team: Team
    overs: list(Over)

    def start_innings(self) -> None:
        pass
