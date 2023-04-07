# Tic-tac-toe
The classic Tic-Tac-Toe game, traditional 3 X 3 grid
## Description
There are two main files in this project: runner.py and tictactoe.py. 
tictactoe.py contains all of the logic for playing the game, and for making optimal moves. 
runner.py contains all of the code to run the graphical interface for the game
## How to run
```
python runner.py 
```
## About the algorithm
The AI is implemented using Minimax algorithm. 
A type of algorithm in adversarial search, Minimax represents winning conditions as (-1) for one side and (+1) for the other side. Further actions will be driven by these conditions, with the minimizing side trying to get the lowest score, and the maximizer trying to get the highest score.
Recursively, the algorithm simulates all possible games that can take place beginning at the current state and until a terminal state is reached. 
Each terminal state is valued as either (-1), 0, or (+1).
