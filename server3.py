import socket
from datetime import datetime


def get_current_date_time():
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    return dt_string



HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        username = addr[0]
        while True:
            # Assume all input will be a message
            is_a_message = True
            # Receive data and convert to string
            data = conn.recv(1024).decode()
            if not data: break

            # Handling of commands through if statements, otherwise it's a normal message
            if data == "/quit":
                print(username + " has quit")
                # Break statement keeps the server from sending input back to the user that quit
                break
            elif data == "/time":
                # make a note of a time request on the server and create a formatted message to send the desired info
                print(username + " has requested the time")
                data = "It is " + get_current_date_time() + " right now."
                # We are no longer returning messages, so set to false.
                is_a_message = False
            elif "/name " in data:
                # Store old username for notification message
                old_username = username
                username = data[6:]
                # make a note of the name change on the server and create a formatted message to send the confirmation
                print(old_username + " has changed their name to " + username)
                data = "Rejoice! " + old_username + " is now known as " + username
                # We are no longer returning messages, so set to false.
                is_a_message = False
            else:
                print(username + ": " + data)
            
            if is_a_message == True:
                # Add the address to the start of the message so we know who's talking
                data = username + ": " + data

            # Return formatted message (or command results) to user
            conn.sendall(data.encode())