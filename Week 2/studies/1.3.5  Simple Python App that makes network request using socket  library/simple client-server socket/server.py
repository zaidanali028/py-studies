# echo-server.py

import socket

HOST = "127.0.0.1"  
PORT = 12345 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))
    server.listen(5)

    print(f'Server listening on  {HOST}:{PORT}')

    client_socket, client_address = s.accept()
    print(f'Connection established with {client_address}')

    data=client_socket.recv(1024).decode('utf-8')
    print(f'Received: {data} from client')

  