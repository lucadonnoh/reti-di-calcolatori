from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverPort = 12001
serverSocket.bind(("", ))

print("The server is ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)