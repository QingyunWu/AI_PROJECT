import sys

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



alpha = -sys.maxint
beta = sys.maxint
count = 0

def full(board):
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

    available_moves = actions(board)
    print available_moves
    max_val = -sys.maxint
    results = {}
    for move in available_moves:
        min_value = min_value_search(result(board, move, 'X'), move, 1)
        results[move] = min_value
        max_val = max(max_val, min_value)
    print results
    for move in results.keys():
        if results.get(move) == max_val:
            print "PC choose to " + str(move) + " with the value of {}".format(max_val)
            return move



def max_value_search(board, last_move, level):
    print "MAX search, last move is {}, leve is {}".format(last_move, level)

    global alpha
    global count
    count += 1
    if_terminate = check_terminate(board, last_move)
    if if_terminate[0]:
        return if_terminate[1]

    max_value = -sys.maxint
    available_moves = actions(board)
    # print available_moves
    for move in available_moves:
        # print "min node traversed"

        max_value = max(max_value, min_value_search(result(board, move, 'X'), move, level+1))
        if max_value >= beta:
            return max_value
        alpha = max(alpha, max_value)
    return max_value


def min_value_search(board, last_move, level):
    print "min search, last move is {}, level is {}".format(last_move, level)
    global beta
    global count
    count += 1
    if_terminate = check_terminate(board, last_move)
    if if_terminate[0]:
        print "min search, last move is {}, level is {}".format(last_move, level) + "TERMINATED"
        return if_terminate[1]
    min_value = sys.maxint
    available_moves = actions(board)
    # print available_moves
    print available_moves
    for move in available_moves:
        # print "max node traversed"
        min_value = min(min_value, max_value_search(result(board, move, 'O'), move, level+1))
        if min_value <= alpha:
            return min_value
        beta = min(beta, min_value)
    return min_value

def check_terminate(board, move):
    global alpha
    global beta
    last_symbol = board[move]
    if_win = check_if_win(board, move)
    if last_symbol == 'X' and if_win:
        return (True, 1000)
    if last_symbol == 'O' and if_win:
        return (True, -1000)
    if full(board):
        return (True, 0)
    # print "mei wan"
    return (False, 1234)

def player_make_move(board):
    print "Now it's your turn, pick a cell to place your SYMBOL 'O'. (1 ~ 16)"
    move = input()
    return move


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




# program start
if __name__ == '__main__':
    board = [x for x in range(0, 17)]
    for x in [1,2,5,6,11,12,14]:
        board[x] = 'O'
    for x in [3,4,7,8,10,15,16]:
        board[x] = 'X'
    drawBoard(board)
    print "Welcome, you want to go first? y/n"
    user_input = raw_input()
    turn = 'user' if user_input == 'y' else 'pc'
    game_is_on = True
    while game_is_on:
        if turn == 'user':
            move = player_make_move(board)
            board[move] = 'O'
            drawBoard(board)
            turn = 'pc'
            print count
            count = 0
            if check_if_win(board, move):
                print 'you won!'
                game_is_on = False
            print game_is_on
        else:
            move = alpha_beta_search(board)
            board[move] = 'X'
            drawBoard(board)
            turn = 'user'
            print count
            count = 0
            if check_if_win(board, move):
                print 'pc won!'
                game_is_on = False
            print game_is_on
