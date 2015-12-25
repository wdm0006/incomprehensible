"""
.. module:: dict_pivot
   :platform: Unix, Windows
   :synopsis: pivots a dictionary on a certain key

.. moduleauthor:: Will McGinnis <will@pedalwrencher.com>


"""

__author__ = 'willmcginnis'


def dict_pivot(x_in, key):
    """

    Before:

    >>>{"ts": 123, "A": "A", "B": "B", "sub": [{"C": 10}, {"C": 8}]}

    After:

    >>>[
    >>>     {'B': 'B', 'A': 'A', 'ts': 123, 'sub.C': 10},
    >>>     {'B': 'B', 'A': 'A', 'ts': 123, 'sub.C': 8}
    >>>]

    :param x_in:
    :param key:
    :return:
    """
    return [dict([(k, v) for k, v in x_in.items() if k != key] + ch) for ch in [[(key + '.' + k, v) for k, v in y.items()] for y in x_in[key]]]

if __name__ == '__main__':
    dl = {"ts": 123, "A": "A", "B": "B", "sub": [{"C": 10}, {"C": 8}]}
    print(dict_pivot(dl, key='sub'))