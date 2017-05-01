# -*- coding: UTF-8 -*-

import sys
import time
from evalfunc import evalfunc
from auxiliary import actions, check_if_win, check_is_full, check_terminate, drawBoard, draw_init_board, player_make_move, result

# define global variables for stas to show on console
node_count = 1
max_search_prunings = 0
min_search_prunings = 0
max_level = 0
cutoff_occured = False

'''
The MINIMAX ALOGORITHM with ALPHA-BETA PRUNING for the computer to compute for the next move
The initial α is -1000 and β is 1000
After computation, the max depth level to reach in 10 seconds is 7, thus the cutoff test is set to level 7
'''
def alpha_beta_search(board, difficulty):
    global max_search_prunings
    global min_search_prunings
    global node_count
    global max_level
    global cutoff_occured
    start_time = time.time()
    # reset the prunings count and node_count to be initial value for next search
    max_search_prunings = 0
    min_search_prunings = 0
    node_count = 1 # includes the root node
    max_level = 0
    cutoff_occured = False

    available_moves = actions(board)
    max_val = -sys.maxint
    # results record all the actions and its corresponding value after α β search
    results = {}
    for move in available_moves:
        min_value = min_value_search(result(board, move, 'X'), -1000, 1000, move, 1, difficulty)
        results[move] = min_value
        max_val = max(max_val, min_value)
    # get the time for the computer to compute for the move
    elapsed_time = time.time() - start_time
    # ouput stats for the current move
    print "-------------------------"
    print "If cutoff occured? {}".format(cutoff_occured)
    print "-------------------------"
    print "max depth reached: {}".format(max_level)
    print "-------------------------"
    print "total nodes generated for this alpha beta search: {}".format(node_count)
    print "-------------------------"
    print "max_search_prunings count: {} ".format(max_search_prunings)
    print "-------------------------"
    print "min_search_prunings count: {} ".format(min_search_prunings)
    print "-------------------------"
    print "Time elapsed for the PC's move: {}".format(elapsed_time)
    print "-------------------------"
    # iterate all the moves, find the move with max value as the chosen move
    print results
    for move in results.keys():
        if results.get(move) == max_val:
            print "PC chose to go sqaure: {} !".format(move)
            return move


def max_value_search(board, alpha, beta, last_move, level, difficulty):
    global node_count
    global max_search_prunings
    global max_level
    global cutoff_occured
    # every time max search called, new node gernerated
    node_count += 1
    # return a tuple (boolean if_terminate, int value)
    if_terminate = check_terminate(board, last_move)
    # if the node is terminal node, just return the value
    if if_terminate[0]:
        return if_terminate[1]

    max_value = -sys.maxint
    available_moves = actions(board)

    for move in available_moves:
        # keep track of the max depth level reached
        if level + 1 > max_level:
            max_level = level + 1
        # cutoff applies in level 5, 6, 7 in easy, medium, hard mode
        if level >= difficulty + 3:
            cutoff_occured = True
            return evalfunc(result(board, move, 'X'))
        max_value = max(max_value, min_value_search(result(board, move, 'X'), alpha, beta, move, level + 1, difficulty))
        if max_value >= beta:
            # if value already larger than the current min value, just return it since the max value cannot exceed either
            max_search_prunings += 1
            return max_value
        # update the alpha value if no prunings in the node
        alpha = max(alpha, max_value)
    return max_value


def min_value_search(board, alpha, beta, last_move, level, difficulty):
    global cutoff_occured
    global node_count
    global min_search_prunings
    global max_level
    node_count += 1
    if_terminate = check_terminate(board, last_move)
    if if_terminate[0]:
        return if_terminate[1]
    min_value = sys.maxint
    available_moves = actions(board)

    for move in available_moves:
        if level + 1 > max_level:
            max_level = level + 1
        # cutoff applies in level 5, 6, 7
        if level + 1 >= difficulty + 4:
            cutoff_occured = True
            return evalfunc(result(board, move, 'O'))
        min_value = min(min_value, max_value_search(result(board, move, 'O'), alpha, beta, move, level+1, difficulty))

        if min_value <= alpha:
            # if value already less than the current max value, just return it since the min value cannot exceed either
            min_search_prunings += 1
            return min_value
        # update the alpha value if no prunings in the node
        beta = min(beta, min_value)
    return min_value

# program start point
if __name__ == '__main__':
    while True:
        # initialize the empty board
        board = [' ' for x in range(0, 17)]
        draw_init_board()
        while True:
            try:
                difficulty = input("Welcome, what difficulty you want to challenge? (easy:1, medium:2, hard:3) ")
                if difficulty not in [1,2,3]:
                    print "You should input 1 ~ 3 to get the target difficulty!"
                    continue
                else:
                    break # if input valid, break the loop
            except NameError:
                print "You should input 1 ~ 3 to get the target difficulty!"
                continue # if name error occured, start ask again
        difficulties = {1:"EASY", 2:"MEDIUM", 3:"HARD"}
        print "The difficulty you have chosen is {}".format(difficulties.get(difficulty))
        # ask the player to choose whether to start first
        while True:
            go_first = raw_input("Welcome, you want to go first? (y/n) ")
            if go_first in ['y', 'n']:
                turn = 'user' if go_first == 'y' else 'pc'
                break
            else:
                print "You should input y or n to get started!"
                continue
        game_over = False # flag to determin whether the game is still on
        while not game_over:
            if turn == 'user':
                move = player_make_move(board)
                board[move] = 'O'
                turn = 'pc'
                if check_if_win(board, move):
                    print 'You won!'
                    game_over = True
                if check_is_full(board):
                    print "It's a tie!"
                    game_over = True
            else:
                move = alpha_beta_search(board, difficulty)
                board[move] = 'X'
                drawBoard(board)
                turn = 'user'
                if check_if_win(board, move):
                    print 'PC won!'
                    game_over = True
                if check_is_full(board):
                    print "It's a tie!"
                    game_over = True
        play_again = raw_input("Do you want to play again? (y/n) ")
        if play_again == 'n':
            print "bye bye..."
            break
        
