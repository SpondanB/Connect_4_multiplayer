import socket
import threading

HEADER = 64
PORT = 5050
# SERVER = ""  # this is the ip address of the device the server will run on 
SERVER = socket.gethostbyname(socket.gethostname())  # can be also done like this automatically
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

print("[INITIALIZING] socket is being initialized...")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket initialization for TCP connections
print("[BINDING] socket is bound to the server...")
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
            conn.send("Msg Recived".encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}...")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount()-1}")

print("[STARTING] server is starting...")
start()
