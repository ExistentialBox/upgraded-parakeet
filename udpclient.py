#!/usr/bin/env

import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('LocalHost', 54000)

try:
    message = raw_input("> ")
    sent = sock.sendto(message, server_address)
    data, server = sock.recvfrom(4096)
    print data
finally:
    sock.close()
