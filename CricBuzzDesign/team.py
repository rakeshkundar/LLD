from __future__ import annotations
from player import Player
from player_batting_controller import PlayerBattingController
from player_bowling_contoller import PlayerBowlingController

class Team:
    id: int
    name: str
    players: list(Player)
    batting_controller: PlayerBattingController
    bowling_controller: PlayerBowlingController
