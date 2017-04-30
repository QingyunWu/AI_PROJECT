# AI_PROJECT
### Instructions on the program execution:
The folder contains 3 files: **game.py**, **auxiliary.py** and **evalfunc.py**, the first file contains main algorithm part and program start point (main function), the second one is to store auxiliary functions to support the main algorithm, the evalfunc.py contains the evaluation function when cutoff occurred.

To start the program, in terminal, change to the path where the folder is, then run as `python game.py`

The game has three difficulty levels for the user to choose, after the choice of difficulty, it will then ask the player to choose whether to start first or not.
The player’s symbol is ‘O’ and the PC’s symbol is ‘X’. The player is asked to pick a square number to place his or her symbol ‘O’, the number is from 1 to 16 and represents all the square starting from the left top corner. After every step of PC, the console will output the new board configuration and all the statistics for the PC’s computation. If one side wins the game or a draw happens, the player will be asked if he or she wants to start again.

### Game design description:
The algorithm for the PC to pick a move is **MINIMAX** algorithm with **ALPHA-BETA PRUNINGS**, the decrease the total search time below 10 seconds, **EVALUATION** will be applied if **CUTOFF-TEST** (max depth can be reached based on difficulties, easy: 5, medium: 6, hard: 7) passed. The algorithm and evaluation function are mainly the same as the project assignment description and here I introduced the *last_mvoe* parameter to help to test if the game is over (if one side wins or a draw happens) in a relative efficient way.

Note that after test in my own MAC OS, the max depth the search can reach is level 7 if we want to limit the computation time for the PC side below 10 seconds. And every time the total search time will be shown after a PC’ move.

### Program Demonstration
![demo1](https://github.com/QingyunWu/AI_PROJECT/blob/master/demo1.png)
![demo2](https://github.com/QingyunWu/AI_PROJECT/blob/master/demo2.png)
