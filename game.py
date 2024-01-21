import numpy as np

# this is a 2 player game without any socket implementation

ROW = 6
COL = 7
game_over = False

def create_board():
    board = np.zeros((ROW, COL))
    return board

def drop_piece(board, row, col, piece):
    board[row][col] = piece

def is_valid_location(board, col):
    return board[0][col] == 0

def get_next_open_row(board, col):
    x = ROW -1
    while x >= 0:
        if board[x][col] == 0:
            return x
        else:
            x -= 1
    
    return -1

def winning_move(board, piece):
    # Check horozontal
    for c in range(COL -3):
        for r in range(ROW):
            if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
                return True
    
    # Check vertical
    for r in range(ROW -3):
        for c in range(COL):
            if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
                return True

    # Check digonal top left to bottom right
    for r in range(ROW -3):
        for c in range(COL -3):
            if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
                return True
    
    # Check digonal top right to bottom left
    for r in range(ROW -1, 2):
        for c in range(COL -3):
            if board[r][c] == piece and board[r+1][c-1] == piece and board[r+2][c-2] == piece and board[r+3][c-3] == piece:
                return True
    # if not winning 
    return False

board = create_board()
print(board)
turn = 0

while not game_over:
    # Ask player 1
    if turn % 2 == 0:
        while True:
            col = int(input("Player 1 choice(0-6): "))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                if row != -1:
                    drop_piece(board, row , col, 1)
                    break
            
            print("try again!")

        if winning_move(board, 1):
            print("player 1 wins")
            print(board)
            break

    else: 
        while True:
            col = int(input("Player 2 choice(0-6): "))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                if row != -1:
                    drop_piece(board, row , col, 2)
                    break
            
            print("try again!")
        
        if winning_move(board, 2):
            print("player 2 wins")
            print(board)
            break
    
    print(board)

    turn += 1