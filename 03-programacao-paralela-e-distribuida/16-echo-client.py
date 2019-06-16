#!/usr/bin/env python3

import socket
import time

HOST = "10.199.35.238"  # The server's hostname or IP address
#HOST = "127.0.0.1"
PORT = 20000  # The port used by the server

while( True):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(b"ping")
        print("Send ping")
        time.sleep(1)
        data = s.recv(1024)
        s.close()
    #print("Received", repr(data))
    print("Receive", data.decode('utf-8'))
    time.sleep(1)
