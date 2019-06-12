#!/usr/bin/python

import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('LocalHost', 54000)
sock.bind(server_address)

while True:
    data, address = sock.recvfrom(4096)
    print data
    message = raw_input("> ")
    sent = sock.sendto(message, address)
