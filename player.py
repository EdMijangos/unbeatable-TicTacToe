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
        if len(game.available_moves()) == 9:
            move = random.choice(game.available_moves())
        else:
            move = self.minimax(game, self.letter)['move']
        print(f'AI moved to {move}')
        return move
    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'

        if state.winner == other_player:
            score = 1 * (len(state.available_moves()) + 1) if other_player == max_player else -1 * (len(state.available_moves()) + 1)
            return {'move': None, 'score': score}
        elif len(state.available_moves()) == 0:
            return {'move': None, 'score': 0}
        
        if player == max_player:
            best = {'score': -float('inf')}
        else:
            best = {'score': float('inf')}

        for move in state.available_moves():
            # try all possible moves
            state.make_move(move, player)

            # recurse minimax with new state
            sim_score = self.minimax(state, other_player)

            # undo changes
            state.board[move] = ' '
            state.winner = None 

            # save move that was tried
            sim_score['move'] = move

            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best



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