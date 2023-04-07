"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]
    
    
def helper_count(board, value):
    """
    The helper function counts the total number of given values on the given board
    """
    if value == X:
        num_of_x = 0
        for b in board:
            num_of_x += b.count(X)
        return num_of_x
    elif value == O:
        num_of_o = 0
        for b in board:
            num_of_o += b.count(O)
        return num_of_o
    else:
        count_empty = 0
        for b in board:
            count_empty += b.count(EMPTY)
        return count_empty


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    numb_x = helper_count(board, X)
    numb_o = helper_count(board, O)
    
    if numb_x == 0 and numb_o == 0:
        return X
    elif numb_x < numb_o:
        return X
    elif numb_x == numb_o:
        return X
    # This case should not happen!!!
    elif numb_x - numb_o > 1 or numb_o - numb_x > 1:
        return (-1)
    else:
        return(O)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = set()
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                available_actions.add((i, j))
    
    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    actions_list = list(action)
    new_board_state = copy.deepcopy(board)
    new_board_state[actions_list[0]][actions_list[1]] = player(board)
    
    return new_board_state


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # If there is a winner
    for b in board:
        if b.count(X) == 3:
            return X
        elif b.count(O) == 3:
            return O
    
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
            return X
        if board[0][i] == board[1][i] == board[2][i] == O:
            return O

    if board[0][0] == board[1][1] == board[2][2] == X or board[0][2] == board[1][1] == board[2][0] == X:
        return X
    if board[0][0] == board[1][1] == board[2][2] == O or board[0][2] == board[1][1] == board[2][0] == O:
        return O

    # In case of a tie or the game is in progress
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    elif winner(board) is None and helper_count(board, EMPTY) == 0:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    if winner(board) is None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    temp_max = -1
    temp_min = 1
    the_best_action = None
    
    if player(board) == X:
        for action in actions(board):
            max_minimum = min_value(result(board, action))
            if max_minimum > temp_max:
            #if max_minimum > max_value(result(board,action)):
                temp_max = max_minimum
                the_best_action = action
        return the_best_action
    
    else:
        for action in actions(board):
            min_maximum = max_value(result(board, action))
            if min_maximum < temp_min:
                temp_max = min_maximum
                the_best_action = action
        return the_best_action
    

def max_value(board):
    
    if terminal(board):
        return utility(board)
    
    # Setting variable for a negative infinite integer
    v = float('-inf')
    
    for a in actions(board):
        v = max(v, min_value(result(board, a)))
        
    return v

def min_value(board):
    
    if terminal(board):
        return utility(board)
    
    # Setting variable for a positive infinite integer
    v = float('inf')
    
    for a in actions(board):
        v = min(v, max_value(result(board, a)))
        
    return v