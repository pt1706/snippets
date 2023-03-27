import socket
import time

server_socket = socket.socket()
server_socket.bind(('', 8080))
server_socket.listen(2)


while True:
    client_socket, remote_address = server_socket.accept()
    try:
        request = client_socket.recv(1024)
        client_socket.send(request.upper())
        print('{} : {}'.format(client_socket.getpeername(), request))
        for i in range(10):
            client_socket.send(b'sleep 1 s...\n')
            time.sleep(1)
        client_socket.send(b'connection is closed\n')
        client_socket.close()
    except Exception:
        pass

server_socket.close()