"""This module provides `TCP Chat` server functions.

------------

Exports
------------

    - :py:func:`server.main` is main/entry function

-------------------------------

Related documentations/articles
-------------------------------

    - socket module: https://docs.python.org/3/library/socket.html
    - threading module: https://docs.python.org/3/library/threading.html
    - python style guide: https://www.python.org/dev/peps/pep-0008
    - python docstring conventions: https://www.python.org/dev/peps/pep-0257
    - documenting python devguide: https://devguide.python.org/documenting
    - reStructuredText docstring format: https://www.python.org/dev/peps/pep-0287
    - reStructuredText doc: https://docutils.sourceforge.io/rst.html
"""

from socket import socket, AF_INET, SOCK_STREAM
from threading import Thread


HOST = "127.0.0.1"
PORT = 55555


def _broadcast(message, clients: list):
    for client in clients:
        client.send(message)


def _handle(client: socket, clients: list, nicknames: list):
    while True:
        try:
            message = client.recv(1024)
            _broadcast(message=message, clients=clients)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            _broadcast(message="{} left!".format(nickname).encode("ascii"), clients=clients)
            nicknames.remove(nickname)
            break


def _receive(server: socket, clients: list, nicknames: list):
    while True:
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        client.send("NICK".encode("ascii"))
        nickname = client.recv(1024).decode("ascii")
        nicknames.append(nickname)
        clients.append(client)

        print("Nickname is {}".format(nickname))
        _broadcast(message="{} joined!".format(nickname).encode("ascii"), clients=clients)
        client.send("Connected to server!".encode("ascii"))

        thread = Thread(target=_handle, args=(client, clients, nicknames))
        thread.start()


def main():
    clients = []
    nicknames = []

    server = socket(AF_INET, SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()

    _receive(server=server, clients=clients, nicknames=nicknames)


if __name__ == "__main__":
    main()
