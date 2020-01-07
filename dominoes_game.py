import random
import copy
import numpy as np


def create_dominoes_game(rows, cols):
    row = [False for _ in range(cols)]
    board = [row.copy() for _ in range(rows)]
    return DominoesGame(board.copy())


class DominoesGame(object):

    # Required
    def __init__(self, board):
        self._board = board
        self.num_rows = len(board)
        self.num_cols = len(board[0])

    def get_board(self):
        return self._board

    def print_board(self):
        for row in self._board:
            print(row)
        print()

    def reset(self):
        row = [False for _ in range(self.num_cols)]
        board = [row.copy() for _ in range(self.num_rows)]
        self._board = board.copy()

    def is_legal_move(self, row, col, vertical):
        if vertical:
            domino = ((row, col), (row+1, col))
        else:
            domino = ((row, col), (row, col+1))

        if not self.move_on_board(domino):
            return False

        if not self.move_on_free_space(domino):
            return False

        return True

    def move_on_board(self, domino):
        for square in domino:
            row = square[0]
            col = square[1]
            if row < 0 or row >= self.num_rows:
                return False
            if col < 0 or col >= self.num_cols:
                return False

        return True

    def move_on_free_space(self, domino):
        for square in domino:
            row = square[0]
            col = square[1]

            if self._board[row][col] == True:
                return False

        return True

    def legal_moves(self, vertical):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if self.is_legal_move(row, col, vertical):
                    yield (row, col)

    def perform_move(self, row, col, vertical):
        if vertical:
            domino = ((row, col), (row+1, col))
        else:
            domino = ((row, col), (row, col+1))

        for square in domino:
            row = square[0]
            col = square[1]
            self._board[row][col] = True

    def game_over(self, vertical):
        moves = list(self.legal_moves(vertical))
        if len(moves) == 0:
            return True

        return False

    def copy(self):
        return DominoesGame(copy.deepcopy(self._board))

    def successors(self, vertical):
        for move in self.legal_moves(vertical):
            new_game = self.copy()
            new_game.perform_move(move[0], move[1], vertical)
            yield (move, new_game)

    def get_random_move(self, vertical):
        return random.choice(list(self.legal_moves(vertical)))

    def get_best_move(self, vertical, limit):
        # print(vertical, limit)
        # print(self.num_rows, self.num_cols)
        # print(self._board)
        self.first_move = vertical
        self.max_limit = limit
        self.leaf_counter = 0
        self.best_move = ()

        v = self.alpha_beta_search(self.copy(), vertical)
        return (self.best_move, int(v), self.leaf_counter)

    def alpha_beta_search(self, state, vertical):
        v = self.max_value(state, vertical,  -np.inf, np.inf, 1)
        return v

    def max_value(self, state, vertical, alpha, beta, depth):
        if depth > self.max_limit or state.game_over(vertical):
            self.leaf_counter += 1
            return state.evaluate_board(state, vertical)

        v = -np.inf
        self.best_move = next(state.legal_moves(vertical))
        for new_move, new_state in state.successors(vertical):
            new_vertical = not vertical
            new_v = np.max(
                [v, self.min_value(new_state, new_vertical, alpha, beta, depth+1)])

            if new_v > v:
                self.best_move = new_move

            v = new_v

            if v >= beta:
                return v
            alpha = np.max([alpha, v])

        return v

    def min_value(self, state, vertical, alpha, beta, depth):
        if depth > self.max_limit or state.game_over(vertical):
            self.leaf_counter += 1
            return state.evaluate_board(state, not vertical)

        v = np.inf
        for _, new_state in state.successors(vertical):
            new_vertical = not vertical
            v = np.min([v, self.max_value(
                new_state, new_vertical, alpha, beta, depth+1)])

            if v <= alpha:
                return v
            beta = np.min([beta, v])

        return v

    def evaluate_board(self, state, vertical):
        max_moves = list(state.legal_moves(vertical))
        min_moves = list(state.legal_moves(not vertical))

        return len(max_moves) - len(min_moves)
