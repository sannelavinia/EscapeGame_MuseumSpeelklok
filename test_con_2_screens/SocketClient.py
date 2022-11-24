# Imports library
import socket

# Creates instance of 'Socket'
s = socket.socket()

hostname = "KOKO-PC"  # Server IP/Hostname
port = 9000  # Server Port

s.connect((hostname, port))  # Connects to server

while True:

    x = input("Enter message: ")  # Gets the message to be sent
    s.send(x.encode())  # Encodes and sends message (x)
