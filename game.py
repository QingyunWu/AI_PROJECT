# -*- coding: UTF-8 -*-

import sys
import time
import random
from evalfunc import evalfunc
from auxiliary import actions, check_if_win, check_is_full, check_terminate, drawBoard, player_make_move, result




node_count = 1
max_search_prunings = 0
min_search_prunings = 0
max_level = 0
cutoff_occured = False




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

    elapsed_time = time.time() - start_time

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

    for move in results.keys():
        if results.get(move) == max_val:
            print "PC chose to go sqaure: " + str(move)
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
    if if_terminate[0]:
        return if_terminate[1]

    max_value = -sys.maxint
    available_moves = actions(board)

    for move in available_moves:
        if level + 1 > max_level:
            max_level = level + 1
        # cutoff applies in level 5, 6, 7
        if level >= difficulty + 3:
            cutoff_occured = True
            return evalfunc(result(board, move, 'X'))
        max_value = max(max_value, min_value_search(result(board, move, 'X'), alpha, beta, move, level+1, difficulty))
        if max_value >= beta:
            max_search_prunings += 1
            return max_value
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
        if level >= difficulty + 3:
            cutoff_occured = True
            return evalfunc(result(board, move, 'O'))
        min_value = min(min_value, max_value_search(result(board, move, 'O'), alpha, beta, move, level+1, difficulty))

        if min_value <= alpha:
            # if value already less than the current max value, just return it since the min value cannot exceed either
            min_search_prunings += 1
            return min_value
        beta = min(beta, min_value)

    return min_value


# program start point
if __name__ == '__main__':
    while True:
        board = [' ' for x in range(0, 17)]
        drawBoard(board)
        difficulty = input("Welcome, what difficulty you want to challenge? (easy:1, medium:2, hard:3) ")
        difficulties = {1:"EASY", 2:"MEDIUM", 3:"HARD"}
        print "The difficulty you have chosen is {}".format(difficulties.get(difficulty))
        go_first = raw_input("Welcome, you want to go first? (y/n) ")
        turn = 'user' if go_first == 'y' else 'pc'
        game_is_on = True
        while game_is_on:
            if turn == 'user':
                move = player_make_move(board)
                board[move] = 'O'
                turn = 'pc'
                if check_if_win(board, move):
                    print 'You won!'
                    game_is_on = False
                if check_is_full(board):
                    print "It's a tie!"
                    game_is_on = False
            else:
                move = alpha_beta_search(board, difficulty)
                board[move] = 'X'
                drawBoard(board)
                turn = 'user'
                if check_if_win(board, move):
                    print 'PC won!'
                    game_is_on = False
                if check_is_full(board):
                    print "It's a tie!"
                    game_is_on = False
        play_again = raw_input("Do you want to play again? (y/n) ")
        if play_again == 'n':
            print "bye bye..."
            break
