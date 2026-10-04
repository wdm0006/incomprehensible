"""
.. module:: get_files
   :platform: Unix, Windows
   :synopsis: a generator comprehension that returns a generator of filenames with an extension downstream of a directory

.. moduleauthor:: Will McGinnis <will@pedalwrencher.com>


"""

import os

__author__ = 'willmcginnis'


def get_files(x_in, extension):
    """

    >>> import os, tempfile
    >>> with tempfile.TemporaryDirectory() as root:
    ...     os.makedirs(os.path.join(root, 'pkg'))
    ...     for name in ['a.py', 'notes.txt', os.path.join('pkg', 'b.py')]:
    ...         open(os.path.join(root, name), 'w').close()
    ...     sorted(os.path.relpath(p, root) for p in get_files(root, 'py'))
    ['a.py', 'pkg/b.py']

    :param x_in: a directory to start searching under
    :param extension: the extension to search for
    :return:
    """
    return (os.path.join(root, file) for root, _, files in os.walk(x_in) for file in files if file.endswith(extension and '.' + extension.lstrip('.')))

if __name__ == '__main__':
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(list(get_files(dir, 'py')))
