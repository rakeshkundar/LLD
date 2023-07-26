from game import TicTacToeGame

if __name__ == '__main__':
    result = "Match Tied"
    board_size = 3
    game = TicTacToeGame(board_size)
    game.start_game()

    if(game.winner):
        result = f"{game.winner.get_player_name()} has won the game."

    print(result)