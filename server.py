# standard socket library used
# already included in Python
import socket
import time

# global value for headersize
HEADERSIZE = 15

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1243))

s.listen(5)

while True:

    # endpoint is aware of the other endpoint
    clientsocket, address = s.accept()

    print(f"Connection from {address} has been established.")

    message = "Welcome to the EPICSHELTER."
    message = "You have entered the server."
    message = f"{len(message):<{HEADERSIZE}}"+message

    clientsocket.send(bytes(message,"utf-8"))

    while True:
        # sleep time
        time.sleep(3)

        # server will give us actual time
        message = f"The time is {time.time()}"
        message = f"{len(message):<{HEADERSIZE}}"+message

        print(message)

        clientsocket.send(bytes(message,"utf-8"))