import socket
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

HEADER = 64
PORT = 5050
# SERVER = ""  # this is the ip address of the device the server will run on 
SERVER = socket.gethostbyname(socket.gethostname())  # can be also done like this automatically
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

print("[INITIALIZING] socket is being initialized...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket initialization for TCP connections
server.bind(ADDR)  # binding the socket

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[{addr}] {msg}")
            return msg
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}...")
    conn1, addr1 = server.accept()
    conn2, addr2 = server.accept()
    board = create_board()
    print(board)
    turn = 0
    while not game_over:
        if turn == 0:
            while True:
                col = int(handle_client(conn1, addr1))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    conn2.send(str(col).encode(FORMAT))
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
                col = int(handle_client(conn2, addr2))

                if is_valid_location(board, col):
                    row = get_next_open_row(board, col)
                    conn1.send(str(col).encode(FORMAT))
                    if row != -1:
                        drop_piece(board, row , col, 2)
                        break
                
                print("try again!")
            
            if winning_move(board, 2):
                print("player 2 wins")
                print(board)
                break
        
        print(board)
        turn = (turn + 1) % 2
    
    conn2.close()
    conn1.close()

        

print("[STARTING] server is starting...")
start()
