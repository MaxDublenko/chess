board = [
    ['br', 'bh', 'bb', 'bq', 'bk', 'bb', 'bh', 'br'], # 8
    ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'], # 7
    ['--', '--', '--', '--', '--', '--', '--', '--'], # 6
    ['--', '--', '--', '--', '--', '--', '--', '--'], # 5
    ['--', '--', '--', '--', '--', '--', '--', '--'], # 4
    ['--', '--', '--', '--', '--', '--', '--', '--'], # 3
    ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'], # 2
    ['wr', 'wh', 'wb', 'wq', 'wk', 'wb', 'wh', 'wr']  # 1
    # a     b     c     d     e     f     g     h
]

#print(board[int(row1)*-1+8][letters[col1]], board[int(row2)*-1+8][letters[col2]])

#for i in range(len(board)):
#    print(board[i])


# function for each piece that moves, and then when a square is selected with that piece,
# the function that moves that piece is called, and then rules are checked less than all
# once. Will make functions to check castling availabiltiy to, etc...

def moveRook(row, col):
    pass

def moveHorse(row, col):
    pass

def moveBishop(row, col):
    pass

def moveQueen(row, col):
    pass

def moveKing(row, col):
    pass

def movePawn(row, col):
    # If all is good:
    board[int(row2)*-1+8][letters[col2]] = board[row][col]
    board[row][col] = '--'

def game():
    move = input('Your Move: ')
    #e2-e4
    letters = {
        'a': 0,
        'b': 1,
        'c': 2,
        'd': 3,
        'e': 4,
        'f': 5,
        'g': 6,
        'h': 7
    }

    row1 = move[1]
    col1 = move[0]
    row2 = move[4]
    col2 = move[3]

    #piece checker:
    if board[int(row1)*-1+8][letters[col1]] in ['wp', 'bp']:
        movePawn(int(row1)*-1+8, letters[col1])
    elif board[int(row1)*-1+8][letters[col1]] == '--':
        print('Error: targetted empty square')

    for i in range(len(board)):
        print(board[i])
