import socket as sc


def are_you_going_to_have_lunch(host, port):
    socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    socket.bind((host, port))
    socket.listen(1)

    while True:
        connection, address = socket.accept()

        print('Connection from:', address)

        while True:
            data = connection.recv(1024)
            if not data:
                break

            print('Received:', data.decode())

            connection.sendall(data)

        connection.close()


if __name__ == '__main__':
    host = 'localhost'
    port = 8080

    are_you_going_to_have_lunch(host, port)
