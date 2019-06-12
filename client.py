#!/usr/bin/env python3

import socket, os

try:
    os.system("clear")
except:
    os.system("cls")

host = '127.0.0.1'  # The server's hostname or IP address
port = 65432        # The port used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    message = raw_input("< ")
    s.sendall(message)
    data = s.recv(1024)
    print("> " + data)
    if message == "q":
        break

s.close()
