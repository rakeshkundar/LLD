from piece_type import PieceType

class PlayingPiece:
    piece_type: PieceType

    def __init__(self, piece_type: PieceType) -> None:
        self.piece_type = piece_type