from __future__ import annotations

from collections import deque
from player import Player
from board import Board
from playing_piece_x import PlayingPieceX
from playing_piece_o import PlayingPieceO

class TicTacToeGame:
    players: deque(Player) = deque()
    board: Board
    is_game_over: bool = False
    winner: Player = None

    def __init__(self, board_size: int) -> None:
        self.initialize_game(board_size)


    def initialize_game(self, size: int):
        self.board = Board(size)

        # Creating 2 Players
        player_x  = Player(1, 'Player1', PlayingPieceX())
        player_o  = Player(1, 'Player2', PlayingPieceO())

        self.players.append(player_x)
        self.players.append(player_o)

    
    def start_game(self):
        while(not self.is_game_over):
            self.board.print_board()

            if(not self.board.check_if_free_cell_exist()):
                self.is_game_over = True
                continue

            player = self.players.popleft()

            values = input(f"Choose row, col for {player.name} : ")

            row, col = values.split(',')
            row, col = int(row), int(col)
            print(f"ROW : {row}, COL : {col}")

            if(row >= self.board.size or col >= self.board.size or not self.board.if_cell_free(row, col)):
                print(f"Invalid row, col . Please retry!")
                self.players.appendleft(player)
                continue

            self.board.update_cell(row, col, player.playing_piece)

            if(self.board.has_player_won(row, col, player.playing_piece)):
                self.is_game_over  = True
                self.winner = player
                continue
            
            self.players.append(player)




            
