from playing_piece import PlayingPiece
from piece_type import PieceType

class PlayingPieceX(PlayingPiece):

    def __init__(self) -> None:
        super().__init__(PieceType.X)

