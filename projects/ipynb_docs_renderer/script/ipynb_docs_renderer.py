"""This module provides `ipynb` rendering functionalities.

It will load `ipynb` docs, convert them to desired format, put new converted documents
in docs directory and commit and push changes to git.

------------

Exports
------------

    - :py:func:`ipynb_docs_renderer.main` is main/entry function

-------------------------------

Related documentations/articles
-------------------------------

    - os module: https://docs.python.org/3/library/os.html
    - pathlib module: https://docs.python.org/3/library/pathlib.html
    - shutil module: https://docs.python.org/3/library/shutil.html
    - sys module: https://docs.python.org/3/library/sys.html
    - concurrent.futures module: https://docs.python.org/3/library/concurrent.futures.html
    - jupyterlab: https://jupyterlab.readthedocs.io/en/stable
    - nbconvert: https://nbconvert.readthedocs.io/en/latest/index.html
    - python style guide: https://www.python.org/dev/peps/pep-0008
    - python docstring conventions: https://www.python.org/dev/peps/pep-0257
    - documenting python devguide: https://devguide.python.org/documenting
    - reStructuredText docstring format: https://www.python.org/dev/peps/pep-0287
    - reStructuredText doc: https://docutils.sourceforge.io/rst.html
"""

import os
import pathlib
import shutil
import sys

from concurrent.futures import ThreadPoolExecutor


_DOCS_PATH = 'docs'
_PROJECTS_PATH = 'projects'
_IPYNB_GLOB = '**/*.ipynb'

_GIT_MAIN_BRANCH_NAME = 'main'
_GIT_EMAIL = 'iranipy@users.noreply.github.com'
_GIT_USERNAME = 'iranipy'
_GIT_COMMIT_MESSAGE = 'new rendered docs added by ipynb_docs_renderer action'

_CONVERTED_FILE_FORMAT = 'html'
_CONVERT_COMMAND = f'jupyter nbconvert --to {_CONVERTED_FILE_FORMAT}'
_DEPENDENCIES = [
    'jupyterlab',
    'nbconvert',
]


def _install_dependencies():
    """Installs required dependencies.
    """
    with ThreadPoolExecutor() as executer:
        executer.map(os.system, [f'pip install {d}' for d in _DEPENDENCIES])


def _render_ipynb(ipynb: pathlib.Path):
    """Converts ipynb docs to ``_CONVERTED_FILE_FORMAT``.

    It will put new converted documents in ``_DOCS_PATH`` directory.

    :param ipynb: path object
    :type ipynb: :py:class:`pathlib.Path`
    """
    directory, file = os.path.split(ipynb)

    rendered_file = f'{os.path.splitext(file)[0]}.{_CONVERTED_FILE_FORMAT}'
    rendered_file_path = os.path.join(directory, rendered_file)

    os.system(f'{_CONVERT_COMMAND} {ipynb.absolute()}')

    shutil.move(rendered_file_path, os.path.join(_DOCS_PATH, rendered_file))


def _run_rendering():
    """Executes desired processes on ipynb docs (each in separate thread).
    """
    IPYNB_DOCS = list(pathlib.Path(_PROJECTS_PATH).glob(_IPYNB_GLOB))

    with ThreadPoolExecutor() as executer:
        executer.map(_render_ipynb, IPYNB_DOCS)


def _commit_push():
    """Commits and push changes to git.
    """
    commands = [
        f'git config --global user.email "{_GIT_EMAIL}" && git config --global user.name "{_GIT_USERNAME}"',
        'git add .',
        f'git commit -m "{_GIT_COMMIT_MESSAGE}"',
        f'git fetch origin {_GIT_MAIN_BRANCH_NAME}',
        f'git push origin {_GIT_MAIN_BRANCH_NAME}',
    ]

    list(map(os.system, commands))


def main():
    """This is main/entry function.
    """
    task = {
        'install-dependencies': _install_dependencies,
        'render': _run_rendering,
        'commit-push': _commit_push,
    }[sys.argv[1]]

    task()


if __name__ == '__main__':
    main()
