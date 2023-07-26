from playing_piece import PlayingPiece

class Player:
    id: int
    name: str
    playing_piece: PlayingPiece

    def __init__(self, id: int, name: str, playing_piece: PlayingPiece) -> None:
        self.id = id
        self.name = name
        self.playing_piece = playing_piece

    def get_player_id(self) -> int:
        return self.id

    def get_player_name(self) -> str:
        return self.name

    def get_player_piece(self) -> PlayingPiece:
        return self.playing_piece