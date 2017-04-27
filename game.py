
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

def computer_make_move(board):
    pass

def player_make_move(board):
    print "Now it's your turn, pick a cell to place your SYMBOL 'O'. (1 ~ 16)"
    move = input()
    board[move] = 'O'
    
    drawBoard(board)
    if check_if_win(board, move):
        print "You Win!"
    else:
        print "PC next"
        computer_make_move(board)

def check_if_win(board, new_move):
    last_symbol = board[new_move]
    line_count = 0
    for num in [x for x in range(1,17) if x % 4 == new_move % 4]:
        if board[num] != last_symbol:
            line_count = 0
            break
        else:
            line_count += 1
    if line_count == 4:
        return True

    for num in [x for x in range(1,17) if (x - 1)/4 == (new_move - 1)/4]:
        if board[num] != last_symbol:
            line_count = 0
            break
        else:
            line_count += 1
    if line_count == 4:
        return True

    if new_move in [1,6,11,16]:
        for num in [1,6,11,16]:
            if board[num] != last_symbol:
                line_count = 0
                break
            else:
                line_count += 1
        if line_count == 4:
            return True

    if new_move in [4,7,10,13]:
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
    drawBoard(board)
    print "Welcome, you want to go first? y/n"
    user_input = raw_input()
    player_start_first = True if user_input == 'y' else False
    if not player_start_first:
        alpha_beta_search(board)
    else:
        player_make_move(board)
