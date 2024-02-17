# import socket module
from socket import *
# In order to terminate the program
import sys


def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    # Fill in start

    # Fill in end

    while True:
        # Establish the connection

        print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept() # Fill in start -are you accepting connections?     #Fill in end

    try:
        message = connectionSocket.recv(1024).decode()  # Fill in start - a client is sending you a message #Fill in end
        filename = message.split()[1]

        f = open(filename[1:], 'r', encoding='utf-8')  # fill in start #fill in end

        # Prepare the HTTP response header
        outputdata = 'HTTP/1.1 200 OK\nContent-Type: text/html; charset=UTF-8\n\n'.encode()

        # Fill in start - append your html file contents
        for i in f:
            outputdata += i
        # Fill in end

        f.close()

        # Send the response (header + content)
        # Fill in start
        connectionSocket.send(outputdata)
        # Fill in end

        connectionSocket.close()

    except Exception as e:
        print("Error:", e)
        # Send response message for invalid request due to the file not being found (404)
        # Fill in start
        header = 'HTTP/1.1 404 Not Found\nContent-Type: text/html; charset=UTF-8\n\n'.encode()
        errorMessage = header + b"<html><body><h1>404 Not Found</h1></body></html>"
        connectionSocket.send(errorMessage)
        # Fill in end

        # Close client socket
        # Fill in start
    connectionSocket.close()
        # Fill in end


    # Commenting out the below, as its technically not required and some students have moved it erroneously in the While loop. DO NOT DO THAT OR YOURE GONNA HAVE A BAD TIME.
    # serverSocket.close()
    # sys.exit()  # Terminate the program after sending the corresponding data


if __name__ == "__main__":
    webServer(13331)
