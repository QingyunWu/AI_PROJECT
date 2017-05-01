# the evaluation function defined in assignment
def evalfunc(board):
    rows_X = {}
    rows_O = {}
    cols_X = {}
    cols_O = {}
    for row in range(1,5):
        row_X = 0
        row_O = 0
        col_X = 0
        col_O = 0
        for col in range(1,5):
            if board[(row - 1) * 4 + col] == 'X':
                row_X += 1
            elif board[(row - 1) * 4 + col] == 'O':
                row_O += 1
            if board[(col - 1) * 4 + row] == 'X':
                col_X += 1
            elif board[(col - 1) * 4 + row] == 'O':
                col_O += 1
        cols_X[row] = col_X
        cols_O[row] = col_O
        rows_X[row] = row_X
        rows_O[row] = row_O
    diag_X_1 = 0
    diag_X_2 = 0
    diag_O_1 = 0
    diag_O_2 = 0
    for cell in [1,6,11,16]:
        if board[cell] == 'X':
            diag_X_1 += 1
        if board[cell] == 'O':
            diag_O_1 += 1
    for cell in [4,7,10,13]:
        if board[cell] == 'X':
            diag_X_2 += 1
        if board[cell] == 'O':
            diag_O_2 += 1
    X3 = len([x for x in rows_X.values() if x == 3]) + len([x for x in cols_X.values() if x == 3]) + \
    (1 if diag_X_1 == 3 else 0) + (1 if diag_X_2 == 3 else 0)
    X2 = len([x for x in rows_X.values() if x == 2]) + len([x for x in cols_X.values() if x == 2]) + \
    (1 if diag_X_1 == 2 else 0) + (1 if diag_X_2 == 2 else 0)
    X1 = len([x for x in rows_X.values() if x == 1]) + len([x for x in cols_X.values() if x == 1]) + \
    (1 if diag_X_1 == 1 else 0) + (1 if diag_X_2 == 1 else 0)
    O3 = len([x for x in rows_O.values() if x == 3]) + len([x for x in cols_O.values() if x == 3]) + \
    (1 if diag_O_1 == 3 else 0) + (1 if diag_O_2 == 3 else 0)
    O2 = len([x for x in rows_O.values() if x == 2]) + len([x for x in cols_O.values() if x == 2]) + \
    (1 if diag_O_1 == 2 else 0) + (1 if diag_O_2 == 2 else 0)
    O1 = len([x for x in rows_O.values() if x == 1]) + len([x for x in cols_O.values() if x == 1]) + \
    (1 if diag_O_1 == 1 else 0) + (1 if diag_O_2 == 1 else 0)

    return 6 * X3 + 3 * X2 + X1 - (6 * O3 + 3 * O2 + O1)
