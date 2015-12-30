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

    Before:

    >>>#root directory for this repository

    After:

    >>>[
    >>>    '~/incomprehensible/setup.py',
    >>>    '~/incomprehensible/incomprehensible/__init__.py',
    >>>    '~/incomprehensible/incomprehensible/dedupe_dictlist.py',
    >>>    '~/incomprehensible/incomprehensible/dict_pivot.py',
    >>>    '~/incomprehensible/incomprehensible/flatten_list.py',
    >>>    '~/incomprehensible/incomprehensible/get_files.py',
    >>>    '~/incomprehensible/incomprehensible/split_strip_coerce.py'
    >>>]

    :param x_in: a directory to start searching under
    :param extension: the extension to search for
    :return:
    """
    return (os.path.join(root, file) for root, _, files in os.walk(x_in) for file in files if file.endswith(extension))

if __name__ == '__main__':
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(list(get_files(dir, 'py')))