import numpy as np

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


    else: 
        while True:
            col = int(input("Player 2 choice(0-6): "))

            if is_valid_location(board, col):
                row = get_next_open_row(board, col)
                if row != -1:
                    drop_piece(board, row , col, 2)
                    break
            
            print("try again!")
    
    print(board)

    turn += 1