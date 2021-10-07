"""This module provides `pendulum` sample code.

It's just a simple script to illustrate use of `poetry` in project.

------------

Exports
------------

    - :py:func:`main.main` is main/entry function

-------------------------------

Related documentations/articles
-------------------------------

    - pendulum: https://pendulum.eustace.io
    - python style guide: https://www.python.org/dev/peps/pep-0008
    - python docstring conventions: https://www.python.org/dev/peps/pep-0257
    - documenting python devguide: https://devguide.python.org/documenting
    - reStructuredText docstring format: https://www.python.org/dev/peps/pep-0287
    - reStructuredText doc: https://docutils.sourceforge.io/rst.html
"""

import pendulum


def main():
    """This is main/entry function.
    """
    now = pendulum.now("Europe/Paris")
    now.in_timezone("America/Toronto")
    now.to_iso8601_string()
    print(now)


if __name__ == '__main__':
    main()
