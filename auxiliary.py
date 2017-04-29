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
