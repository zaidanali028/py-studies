# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 6060  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.send("Hello, world".decode('utf-8'))
    data = client.recv(1024)
    print(f"Received from server {data}")

print(f"Received {data}")