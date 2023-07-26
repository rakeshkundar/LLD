from player import Player
from ball_type import BallType
from run_type import RunType

class Ball:
    ball_number: int
    bowled_by: Player
    bowled_to: Player
    runs: 0
    ball_type: BallType
    run_type: RunType


    def play_ball():
        pass