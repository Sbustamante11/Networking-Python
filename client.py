# standard socket library used
# already included in Python
import socket

# global value for headersize
HEADERSIZE = 15

# port number: 1243
# privileged port 
PORT = 1243


# TCP socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT))


while True:

    full_message = ''
    new_message = True

    while True:

        message = s.recv(16)

        if new_message:
            print("New message length:",message[:HEADERSIZE])
            message_len = int(message[:HEADERSIZE])
            new_message = False

        print(f"Full message length: {message_len}")

        full_message += message.decode("utf-8")

        print(len(full_message))


        if len(full_message)-HEADERSIZE == message_len:
            print("Full message received")

            print(full_message[HEADERSIZE:])

            new_message = True
            full_message = ""        
    

