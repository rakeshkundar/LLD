from __future__ import annotations
from collections import deque
from player import Player

class PlayerBowlingController:
    bowlers: deque(Player)
    player_over_bowled: dict[Player, float]
    current_bowler: Player
