from player import HumanPlayer, ComputerPlayer

class TicTacToe:
    def __init__(self):
        self.board = [' ' for i in range(9)] # creates list with 9 empty indexes to rep 3x3 board
        self.winner = None

    def print_board(self):
        cells_per_row = 3
        # prints the indexes in batches of 3 to represent the rows
        for row_number in range(3):
            current_row = ''
            for cell in self.board[row_number*cells_per_row : (row_number+1)*cells_per_row]: # 0-2, 3-5, 6-8
                current_row += f'|{cell}|'
            print(current_row)
        print('') # print empty line for space
            
    @staticmethod
    def print_board_nums():
        print('Guide to play')
        current_index = 0
        # prints the indexes in batches of 3 to represent the rows
        for row_number in range(3):
            current_row = ''
            for cell in range(3):
                current_row += f'|{current_index}|'
                current_index += 1
            print(current_row)

    def available_moves(self):
        moves = []
        for index, cell in enumerate(self.board):
            if cell == ' ':
                moves.append(index)
        return moves

    def make_move(self, move, letter):
        if self.board[move] == ' ':
            self.board[move] = letter
            self.check_winner(move, letter)
            return True
        return False

    def check_winner(self, move, letter):
        # check horizontal win
        row_index = move // 3
        row = self.board[row_index*3 : (row_index+1)*3]
        if all(cell == letter for cell in row):
            self.winner = letter
            return
        # check vertical win
        col_index = move % 3
        column = []
        for index in range(3):
            column.append(self.board[col_index + index * 3])
        if all(cell == letter for cell in column):
            self.winner = letter
            return
        # check diag win
        # only check if the move was an even number
        if move % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all(cell == letter for cell in diagonal_1):
                self.winner = letter
                return
            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all(cell == letter for cell in diagonal_2):
                self.winner = letter
                return

def play(game, x_player, o_player):
    game.print_board_nums()
    letter = 'X' # starting player
    while len(game.available_moves()) > 0:
        # get the player's moves
        if letter == 'O':
            move = o_player.get_move(game)
        else:
            move = x_player.get_move(game)
        # make move and update board
        if game.make_move(move, letter):
            game.print_board()
        # end game if there's a winner
        if game.winner:
            print(f'{letter} player won')
            return
        # switch players
        if letter == 'X':
            letter = 'O'
        else:
            letter = 'X'
    print('It\'s a tie')

# initialize the game
if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = ComputerPlayer('O')
    game = TicTacToe()
    play(game, x_player, o_player)
