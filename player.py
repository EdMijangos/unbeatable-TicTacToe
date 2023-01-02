import time
import random

class Player:
    def __init__(self, letter):
        # letter can be X or O
        self.letter = letter

    # player's turn
    def get_move(self, game):
        pass


class ComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        time.sleep(1) # break to improve UX flow
        move = random.choice(game.available_moves())
        print(f'AI moved to {move}')
        return move


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_move = False
        val = None
        while not valid_move:
            move = input('It\'s your turn. Input your move (0 - 8):')
            try:
                val = int(move)
                if val not in game.available_moves():
                    raise ValueError
                valid_move = True
            except ValueError:
                print('Invalid input. Try again')
        return val