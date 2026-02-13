# Import socket module
from socket import *
import sys  # In order to terminate the program

SERVER_ADDR = "127.0.0.1"
SERVER_PORT = 8080
SOCKET_ADDR = (SERVER_ADDR, SERVER_PORT)

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a server socket
# Fill in start
serverSocket.bind(SOCKET_ADDR)
serverSocket.listen()
# Fill in end

while True:
    # Establish the connection
    print('Ready to serve...')

    # Fill in start
    connectionSocket, clientAddr =  serverSocket.accept()
    # Fill in end

    try:
        # Fill in start
        message = connectionSocket.recv(1024)
        # Fill in end

        filename = message.split()[1] # extracts the filename from the full client request
        f = open(filename[1:]) # opens the filename requested from client, but removes '\' from head

        ''' DEBUG STATEMENT
        print(f"DEBUGGING CLIENT REQUEST MESSAGE\nMessage: {message}\nFilename: {filename}\nFilename[1:]: {filename[1:]}")
        ''' 
        # Fill in start
        outputdata =  f.read() # reads the content of the html page into the outputdata var
        # Fill in end

        # Send one HTTP header line into socket
        # Fill in start
        connectionSocket.send(b"HTTP/1.1 200 OK\r\n") # Message header line + CRLF
        connectionSocket.send(b"\r\n") # CRLF seperating HTTP header from HTTP body elements
        # Fill in end

        # Send the content of the requested file to the client
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        connectionSocket.close()
        
    except IOError:
        # Send response message for file not found
        # Fill in start
        connectionSocket.send(b"HTTP/1.1 404 Not Found\r\n")
        # Fill in end

        # Close client socket
        # Fill in start
        connectionSocket.close()
        # Fill in end

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data

