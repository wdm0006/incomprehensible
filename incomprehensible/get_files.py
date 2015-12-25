"""
.. module:: get_files
   :platform: Unix, Windows
   :synopsis: a generator comprehension that returns a generator of filenames with an extension downstream of a directory

.. moduleauthor:: Will McGinnis <will@pedalwrencher.com>


"""

import os

__author__ = 'willmcginnis'


def get_files(x_in, extension):
    return (os.path.join(root, file) for root, dir, files in os.walk(x_in) for file in files if file.endswith(extension))

if __name__ == '__main__':
    dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print(list(get_files(dir, 'py')))