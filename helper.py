import tictactoe as ttt

board = [['X', 'X', 'O'],
         ['X', 'O', 'O'],
         [None, None, 'X']]

print(ttt.minimax(board))
#print(ttt.player(board))
print(ttt.actions(board))
actions = (0,1)
actions_list = list(actions)
print(ttt.result(board, actions_list))

board = [['X', 'X', 'O'],
         ['X', 'O', 'X'],
         ['O', 'O', 'X']]

print(ttt.winner(board))
print(ttt.terminal(board))
print(ttt.utility(board))


