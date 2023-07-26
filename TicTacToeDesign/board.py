from piece_type import PieceType

class Board:
    size: int
    board: list(list(PieceType))

    def __init__(self, size: int) -> None:
        self.size = size
        self.board = [[None for i in range(size)] for j in range(size)]


    def check_if_free_cell_exist(self) -> bool:
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] is None:
                    return True
        return False


    def if_cell_free(self, row: int, col: int) -> bool:
        return self.board[row][col] == None


    def update_cell(self, row: int, col: int, piece_type: PieceType) -> None:
        self.board[row][col] = piece_type


    def has_player_won(self, row, col, piece_type: PieceType):
        row_check, col_check, left_diagonal_check, right_diagonal_check = True, True, True, True

        for i in range(self.size):
            if(self.board[row][i] != piece_type):
                row_check = False
                break
        
        for i in range(self.size):
            if(self.board[i][col] != piece_type):
                col_check = False
                break
        
        for i in range(self.size):
            if(self.board[i][i] != piece_type):
                left_diagonal_check =  False
                break

        for i in range(self.size):
            if(self.board[i][self.size - 1 - i] != piece_type):
                right_diagonal_check = False
                break

        return row_check or col_check or left_diagonal_check or right_diagonal_check


    def print_board(self):
        print("Board \n")

        for i in range(self.size):
            for j in range(self.size):
                if(not self.board[i][j]):
                    print('', end="\t|")
                else:
                    print(self.board[i][j].piece_type.name, end="\t|")
            print()
