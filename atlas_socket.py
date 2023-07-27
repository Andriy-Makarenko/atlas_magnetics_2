import socket as sc

host = 'localhost'
port = 8080

socket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)


def bind():
    return socket.bind((host, port))


def connect():
    return socket.connect((host, port))


def listen():
    return socket.listen(5)
