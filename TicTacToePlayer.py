"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided

# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 25    # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    dimension = board.get_dim()
    winner = None
    
    while winner == None:
        move_row = random.randrange(dimension)
        move_col = random.randrange(dimension)
        
        if board.square(move_row, move_col) != provided.EMPTY:
            continue
        
        board.move(move_row, move_col,player)
        winner = board.check_win()
        player = provided.switch_player(player)
        
    
    return None

def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists)
    with the same dimensions as the Tic-Tac-Toe board,
    a board from a completed game, and which player the machine player is.
    The function should score the completed board and update
    the scores grid. As the function updates the scores grid directly, 
    it does not return anything,    
    """
    win_condition = board.check_win()
    dimension = board.get_dim()
    
    if win_condition == provided.DRAW:
        return None
    
    if win_condition == None:
        return None
    
    if win_condition == provided.PLAYERX or provided.PLAYERO:
        other = provided.switch_player(player)
        if player == win_condition:
            comp_score = MCMATCH
            other_score = -MCOTHER
        else:
            comp_score = -MCMATCH
            other_score = MCOTHER
            
        for row in range(dimension):
            for col in range(dimension):
                current_square = board.square(row,col)
                if current_square == player:
                    scores[row][col] += comp_score
                elif current_square == other:
                    scores[row][col] += other_score

def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. 
    The function should find all of the empty squares with
    the maximum score and randomly return one of them as a (row, column)
    tuple. It is an error to call this function with a board
    that has no empty squares (there is no possible next move),
    so your function may do whatever it wants in that case.
    The case where the board is full will not be tested.
    """
    dimension = board.get_dim()
    empty_squares = board.get_empty_squares()
    if board.check_win() != None:
        return None
    if empty_squares == []:
        return None
    
    max_score = 0
    for square in empty_squares:
        max_score = max(max_score, scores[square[0]][square[1]])
    
    available_max_score_slots = []
    for square in empty_squares:
        if scores[square[0]][square[1]] == max_score:
            available_max_score_slots.append(square)
    
    print(scores)
    print(available_max_score_slots)        
    recommended_index = random.randrange(len(available_max_score_slots))
    return available_max_score_slots[recommended_index]

def mc_move(board, player, trials):
    """
    This function takes a current board,
    which player the machine player is,
    and the number of trials to run.
    The function should use the Monte Carlo simulation described 
    above to return a move for the machine player
    in the form of a (row, column) tuple.
    Be sure to use the other functions you have written!
    """
    tallied_scores = []
    dimension = board.get_dim()
    for row in range(dimension):
        tallied_scores.append([])
        for col in range(dimension):
            tallied_scores[row].append(0)
    
    for trial in range(trials):
        board_copy = board.clone()
        mc_trial(board_copy, player)
        mc_update_scores(tallied_scores, board_copy, player)
        
    best_move = get_best_move(board, tallied_scores)
    return best_move
    
def test_run():
    test_board = provided.TTTBoard(3)
    mc_trial(test_board, provided.PLAYERX)
    print(str(test_board))
    print(test_board.check_win())
    
    score =[[0,0,0],
             [0,0,0],
             [0,0,0]]
    
    
    
    mc_update_scores(score, test_board,provided.PLAYERX)
    
    print(score)
    
    new_board = provided.TTTBoard(3)
    
    rec_tile = get_best_move(new_board, score)
    print(rec_tile)
    
    result = mc_move(new_board, provided.PLAYERX, 100)
    print(result)
    
    
          
#test_run()

    
# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)


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

