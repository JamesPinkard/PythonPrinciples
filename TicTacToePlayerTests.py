import unittest
from TicTacToePlayer import *

# Constants
EMPTY = 1
PLAYERX = 2
PLAYERO = 3 
DRAW = 4

# Map player constants to letters for printing
STRMAP = {EMPTY: " ",
          PLAYERX: "X",
          PLAYERO: "O"}

def switch_player(player):
    """
    Convenience function to switch players.
    
    Returns other player.
    """
    if player == PLAYERX:
        return PLAYERO
    else:
        return PLAYERX
    
class TTTBoard:
    """
    Class to represent a Tic-Tac-Toe board.
    """

    def __init__(self, dim, reverse = False, board = None):
        """
        Initialize the TTTBoard object with the given dimension and 
        whether or not the game should be reversed.
        """
        self.empty_squares = []
        if board == None:
            self.board =    [["", "", ""],
                            ["", "", ""],
                            ["", "", ""]]
        self.dim = dim
        self.board = board
        self.reverse = reverse
        self.win = None
        self.DRAW = 4
        self.EMPTY = 1
        self.PLAYERO = 2
        self.PLAYERX = 3
            
    def __str__(self):
        """
        Human readable representation of the board.
        """

    def get_dim(self):
        """
        Return the dimension of the board.
        """
        return self.dim
    
    def square(self, row, col):
        """
        Return the status (EMPTY, PLAYERX, PLAYERO) of the square at
        position (row, col).
        """
        return self.board[row][col]

    def get_empty_squares(self):
        """
        Return a list of (row, col) tuples for all empty squares
        """
        return self.empty_squares 

    def move(self, row, col, player):
        """
        Place player on the board at position (row, col).

        Does nothing if board square is not empty.
        """
        self.board[row][col] = player

    def check_win(self):
        """
        If someone has won, return player.
        If game is a draw, return DRAW.
        If game is in progress, return None.
        """
        return self.win
            
    def clone(self):
        """
        Return a copy of the board.
        """
        
        return TTTBoard(self.dim, self.reverse, self.board)


class TicTacToePlayerTests(unittest.TestCase):
    def test_mcTrial_NoOneWins_ReturnNone(self):
        fake_board = TTTBoard(3)
        fake_board.win = fake_board.DRAW    
        
        result = mc_trial(fake_board.board,PLAYERO)
        
        self.assertEqual(None, result)
        
    def test_mcTrial_MakeRandomMove_