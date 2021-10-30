"""This module provides `TCP Chat` client functions.

------------

Exports
------------

    - :py:func:`client.main` is main/entry function

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

from server import HOST, PORT


def _receive(client: socket, nickname: str):
    """Receives Message from server.

    :param client: socket connection
    :type client: :py:class:`socket.socket`
    :param nickname: user nickname
    :type nickname: str
    """
    while True:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break


def _write(client: socket, nickname: str):
    """Sends Message to server.

    :param client: socket connection
    :type client: :py:class:`socket.socket`
    :param nickname: user nickname
    :type nickname: str
    """
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('ascii'))


def main():
    """This is main/entry function.

    It will get user nickname, connect client to server and
    start receiving and sending messages.
    """
    nickname = input("Choose your nickname: ")
    client = socket(AF_INET, SOCK_STREAM)
    client.connect((HOST, PORT))

    receive_thread = Thread(target=_receive, args=(client, nickname))
    receive_thread.start()

    write_thread = Thread(target=_write, args=(client, nickname))
    write_thread.start()


if __name__ == "__main__":
    main()
