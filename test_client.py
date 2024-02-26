#Test TCP Client by Jacob Smith


import sys
import socket


def clientInput():
    """takes port number to connect to server"""
    return clientFunction()


def clientFunction() -> [bool, str]:
    """runs client function """

    while True:
        message = input("Enter a string of the letters c, w, u, b, r, and/or g separated by spaces: ")

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        address = "127.0.0.1"

        client_socket.connect((address, 54345))
    
        if message is None:
            message = "None"

        client_socket.sendall(message.encode())

        response = client_socket.recv(4096)

        if response.decode() == "ending":
            print("Server shutting down, closing client.")
            client_socket.close()
            sys.exit()

        print(f"{response.decode()}\n")

        client_socket.close()   


if __name__ == "__main__":
    clientInput()