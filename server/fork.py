import os
import socket
import sys
import time

server_socket = socket.socket()
server_socket.bind(('', 8000))
server_socket.listen(2)


while True:
    client_socket, remote_address = server_socket.accept()
    child_pid = os.fork()
    if child_pid == 0:
        request = client_socket.recv(1024)
        client_socket.send(request.upper())
        print('child_PID: {}, {} : {}'.format(os.getpid(), client_socket.getpeername(), request))
        for i in range(10):
            client_socket.send(b'sleep 1 s...\n')
            time.sleep(1)
        client_socket.send(b'connection is closed\n')
        client_socket.close()
        sys.exit()
    else:
        client_socket.close()

server_socket.close()