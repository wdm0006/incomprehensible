"""
.. module:: flatten list
   :platform: Unix, Windows
   :synopsis: flattens a list of mixed objects one step (only lists get flatten, other objects stay the same)

.. moduleauthor:: Will McGinnis <will@pedalwrencher.com>


"""

__author__ = 'willmcginnis'


def flatten_list(x_in):
    """

    Before:

    >>>[1, 2, 3, [4, 'B', 6], {'7': 'A'}]

    After:

    >>>[1, 2, 3, 4, 'B', 6, {'7': 'A'}]

    :param x_in:
    :return:
    """
    return [y for z in [x if isinstance(x, list) else [x] for x in x_in] for y in z]

if __name__ == '__main__':
    nested = [1, 2, 3, [4, 'B', 6], {'7': 'A'}]
    print(flatten_list(nested))