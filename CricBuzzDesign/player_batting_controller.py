from collections import deque
from player import Player

class PlayerBattingController:
    yet_to_bat: deque(Player)
    player_on_strike: Player
    non_striker: Player