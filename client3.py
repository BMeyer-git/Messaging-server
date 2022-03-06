import socket

HOST = '172.24.1.186'    # The remote host
PORT = 50007              # The same port as used by the server


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print("Welcome to the chat server!")
    message = ""
    while message != "/quit":
        # Get user input
        message = input("> ")
        # Send as bytes to server
        s.sendall(message.encode())
        # Retrieve any messages from server
        data = s.recv(1024)
        # Print as string to console
        print(data.decode())