# -*- coding: UTF-8 -*-

import sys
import time

def drawBoard(board):
    print('-------------------------')
    print('|   |   |   |   |')
    print('| ' + str(board[1]) + ' | ' + str(board[2]) + ' | ' + str(board[3]) + ' | ' + str(board[4]) + ' | ')
    print('|   |   |   |   |')
    print('-----------------')
    print('|   |   |   |   |')
    print('| ' + str(board[5]) + ' | ' + str(board[6]) + ' | ' + str(board[7]) + ' | ' + str(board[8]) + ' | ')
    print('|   |   |   |   |')
    print('-----------------')
    print('|   |   |   |   |')
    print('| ' + str(board[9]) + ' | ' + str(board[10]) + ' | ' + str(board[11]) + ' | ' + str(board[12]) + ' | ')
    print('|   |   |   |   |')
    print('-----------------')
    print('|   |   |   |   |')
    print('| ' + str(board[13]) + ' | ' + str(board[14]) + ' | ' + str(board[15]) + ' | ' + str(board[16]) + ' | ')
    print('|   |   |   |   |')
    print('-----------------')



alpha = -1000
beta = 1000
node_count = 1
max_search_prunings = 0
min_search_prunings = 0
max_level = 0
def check_is_full(board):
    for cell in range(1,17):
        if type(board[cell]) is int:
            return False
    return True

def actions(board):
    available_moves = [x for x in range(1, 17) if type(board[x]) is int]
    return available_moves

def result(board, move, symbol):
    new_board = list(board)
    new_board[move] = symbol
    return new_board

def alpha_beta_search(board):
    global alpha
    global beta
    global max_search_prunings
    global min_search_prunings
    global node_count
    global max_level
    start_time = time.time()
    # reset the prunings count and node_count to be initial value for next search
    max_search_prunings = 0
    min_search_prunings = 0
    node_count = 1 # includes the root node
    max_level = 0
    alpha = -1000
    beta = 1000
    available_moves = actions(board)
    print available_moves
    max_val = -sys.maxint
    # results record all the actions and its corresponding value after α β search
    results = {}
    for move in available_moves:
        min_value = min_value_search(result(board, move, 'X'), move, 1)
        results[move] = min_value
        max_val = max(max_val, min_value)

    elapsed_time = time.time() - start_time
    print "time elapsed {}".format(elapsed_time)
    print results

    print "max_search_prunings count {} ".format(max_search_prunings)
    print "min_search_prunings count {} ".format(min_search_prunings)
    print "total nodes generated for this alpha beta search: {}".format(node_count)
    print "max depth reached: {}".format(max_level)

    for move in results.keys():
        if results.get(move) == max_val:
            print "PC choose to go " + str(move) + " with the value of {}".format(max_val)
            return move



def max_value_search(board, last_move, level):
    global alpha
    global beta
    global node_count
    global max_search_prunings
    global max_level
    # every time max search called, new node gernerated
    node_count += 1
    if_terminate = check_terminate(board, last_move)
    if if_terminate[0]:
        # print "MAX search, last move is {}, leve is {}".format(last_move, level) + " Terminated"

        return if_terminate[1]

    max_value = -sys.maxint
    available_moves = actions(board)

    for move in available_moves:
        if level + 1 > max_level:
            max_level = level + 1
        max_value = max(max_value, min_value_search(result(board, move, 'X'), move, level+1))
        if max_value >= beta:
            max_search_prunings += 1

            return max_value
        alpha = max(alpha, max_value)
    return max_value


def min_value_search(board, last_move, level):
    # print "min search, last move is {}, level is {}".format(last_move, level)
    global beta
    global alpha
    global node_count
    global min_search_prunings
    global max_level
    node_count += 1
    if_terminate = check_terminate(board, last_move)
    if if_terminate[0]:
        # print "min search, last move is {}, level is {}".format(last_move, level) + "TERMINATED"
        return if_terminate[1]
    min_value = sys.maxint
    available_moves = actions(board)
    # print available_moves

    for move in available_moves:
        if level + 1 > max_level:
            max_level = level + 1
        # print "move: {} ".format(move)
        print alpha
        print beta
        min_value = min(min_value, max_value_search(result(board, move, 'O'), move, level+1))

        if min_value <= alpha:

            # if value already less than the current max value, just return it since the min value cannot exceed either
            min_search_prunings += 1
            return min_value
        beta = min(beta, min_value)

    return min_value

def check_terminate(board, move):
    
    last_symbol = board[move]
    if_win = check_if_win(board, move)
    if last_symbol == 'X' and if_win:
        return (True, 1000)
    if last_symbol == 'O' and if_win:
        return (True, -1000)
    if check_is_full(board):
        return (True, 0)
    # print "mei wan"
    return (False, 1234)

def player_make_move(board):
    move = input("Now it's your turn, pick a cell to place your SYMBOL 'O'. (1 ~ 16) ")
    return move

# check if the player or computer has already won
def check_if_win(board, last_move):
    last_symbol = board[last_move]
    line_count = 0
    for num in [x for x in range(1,17) if x % 4 == last_move % 4]:
        if board[num] != last_symbol:
            line_count = 0
            break
        else:
            line_count += 1
    if line_count == 4:
        return True

    for num in [x for x in range(1,17) if (x - 1)/4 == (last_move - 1)/4]:
        if board[num] != last_symbol:
            line_count = 0
            break
        else:
            line_count += 1
    if line_count == 4:
        return True

    if last_move in [1,6,11,16]:
        for num in [1,6,11,16]:
            if board[num] != last_symbol:
                line_count = 0
                break
            else:
                line_count += 1
        if line_count == 4:
            return True

    if last_move in [4,7,10,13]:
        for num in [4,7,10,13]:
            if board[num] != last_symbol:
                line_count = 0
                break
            else:
                line_count += 1
        if line_count == 4:
            return True
    # in the end, return False
    return False

# program start point
if __name__ == '__main__':
    board = [x for x in range(0, 17)]
    for x in [1,3,5,7,9,11]:
        board[x] = 'O'
    for x in [2,4,6,8,13]:
        board[x] = 'X'
    drawBoard(board)
    # print "min search value " + str(min_value_search(board, 16, 8))
    user_input = raw_input("Welcome, you want to go first? (y/n) ")
    turn = 'user' if user_input == 'y' else 'pc'
    game_is_on = True
    while game_is_on:
        if turn == 'user':
            move = player_make_move(board)
            board[move] = 'O'
            drawBoard(board)
            turn = 'pc'
            if check_if_win(board, move):
                print 'You won!'
                game_is_on = False
            if check_is_full(board):
                print "It's a tie!"
                game_is_on = False
            print game_is_on
        else:
            move = alpha_beta_search(board)
            board[move] = 'X'
            drawBoard(board)
            turn = 'user'
            if check_if_win(board, move):
                print 'PC won!'
                game_is_on = False
            if check_is_full(board):
                print "It's a tie!"
                game_is_on = False
            print game_is_on
