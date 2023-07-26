from __future__ import annotations
from player_type import PlayerType
from person import Person
from batting_scorecard import BattingScorecard
from bowling_scorecard import BowlingScorecard

class Player:
    person: Person
    player_type: PlayerType
    batting_scorecard: BattingScorecard
    bowling_scorecard: BowlingScorecard