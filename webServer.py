# import socket module
from socket import *
# In order to terminate the program
import sys

def webServer(port=13331):
    serverSocket = socket(AF_INET, SOCK_STREAM)

    # Prepare a server socket
    serverSocket.bind(("", port))
    serverSocket.listen(1)

    while True:
        #print('Ready to serve...')
        connectionSocket, addr = serverSocket.accept()

        try:
            message = connectionSocket.recv(1024).decode()
            filename = message.split()[1]

            with open(filename[1:], 'r') as f:
            #with open(filename[1:], 'r', encoding='utf-8') as f:
                # Prepare the HTTP response header
                outputdata = 'HTTP/1.1 200 OK\r\nContent-Type: text/html; charset=UTF-8\r\nConnection:Keep-Alive\r\nServer:RUI\r\n\r\n'.encode()

                for i in f:
                    #outputdata += i
                    outputdata += i.encode('utf-8')

                outputdata +="\r\n".encode()

            # Send the response (header + content)
            connectionSocket.send(outputdata)
            connectionSocket.close()

        except Exception as e:
            header = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html; charset=UTF-8\r\n\r\n'.encode()
            #message = header + b"<html><body><h1>404 Not Found</h1></body></html>"
            connectionSocket.send(header)
            connectionSocket.close()

if __name__ == "__main__":
    webServer(13331)
