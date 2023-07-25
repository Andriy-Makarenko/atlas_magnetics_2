import socket as sc


def im_about_to_lunch(host, port):
    socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
    socket.connect((host, port))

    message = "I'm about to lunch!"
    socket.sendall(message.encode())

    data = socket.recv(1024)
    print('Sent:', data.decode())

    socket.close()


if __name__ == '__main__':
    host = 'localhost'
    port = 8080

    im_about_to_lunch(host, port)
