import socket
import threading

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

print("[INITIALIZING] socket is being initialized...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket initialization for TCP connections
client.connect(ADDR)


def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

run = True

def recive():
    print(client.recv(2048).decode(FORMAT))

while run:
    choice = input("Enter your choice: ")
    if choice == "q":
        send(DISCONNECT_MESSAGE)
        run = False
        break
    send(choice)
