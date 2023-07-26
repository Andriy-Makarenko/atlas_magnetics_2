import socket
import tkinter as tk
from datetime import datetime

from atlas_gui import settings_tk, root
from atlas_socket import connect, socket

connect()
settings_tk()


def im_about_to_lunch():
    label.config(text="Enter the message or send the default one:")
    message = entry.get()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if message:
        message = f"{message} [{date}]"
    else:
        message = f"Are you going to have a lunch? [{date}]"

    label.config(text="Message sent")
    socket.sendall(message.encode())


label = tk.Label(root, text='Enter the message or send the default one:', font=('Arial', 16))
label.pack()

entry = tk.Entry(root, width=50)
entry.pack(padx=15, pady=15)

button = tk.Button(root, text='Send', command=im_about_to_lunch)
button.pack()

root.mainloop()


if __name__ == '__main__':
    im_about_to_lunch()