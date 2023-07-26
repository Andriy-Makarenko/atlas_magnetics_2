import tkinter as tk
from tkinter import messagebox

from atlas_socket import socket, host, port, bind, listen

root = tk.Tk()
root.geometry("500x200")

label = tk.Label(root, text='Waiting for message:', font=('Arial', 16))
label.pack()

text = tk.Entry(root, font=('Arial', 12), width=80)
text.pack(padx=15, pady=15)


def are_you_going_to_have_lunch():
    bind()
    listen()

    while True:
        connection, address = socket.accept()

        print('Connection from:', address)

        while True:
            data = connection.recv(1024).decode()
            if not data:
                break

            print('Received:', data)
            text.delete(0, 'end')
            text.insert(0, data)
            messagebox.showinfo(title="Message from colleague", message=data)
            connection.sendall(data.encode())

        connection.close()


if __name__ == '__main__':
    are_you_going_to_have_lunch()
