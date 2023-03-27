import os
import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind(('127.0.0.1', 8000))
server_socket.listen()

while True:
    connection, client_address = server_socket.accept()
    try:
        print(f'Получен запрос на подключение от {client_address};\n'
              f'Process num: {os.getpid()}')
        buffer = b''

        while buffer[-2:] != b'\t\n':
            data = connection.recv(1024)
            if data == b'\n' or not data:
                break
            else:
                print(f'Получены данные: {data}!')
                buffer = buffer + data

        connection.sendall(buffer)
        print(f"Все данные: {buffer}")

    finally:
        connection.close()

server_socket.close()