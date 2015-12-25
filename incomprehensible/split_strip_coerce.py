"""
.. module:: split_strip_coerce
   :platform: Unix, Windows
   :synopsis: a questionably named function that splits a string on some delimiter, strips the resultant strings, and coerces them into int, str, or float

.. moduleauthor:: Will McGinnis <will@pedalwrencher.com>


"""

__author__ = 'willmcginnis'


def split_strip_coerce(x_in, delimiter):
    """

    Before:

    >>>'2, red, 3.2, green'

    After:

    >>>[2, 'red', 3.2, 'green']

    :param x_in:
    :param delimiter:
    :return:
    """
    return [int(y) if y.replace('-', '', 1).isdigit() else float(y) if y.replace('.', '', 1).replace('-', '', 1).isdigit() else y for y in [str(x).strip() for x in x_in.split(delimiter)]]

if __name__ == '__main__':
    line = '2, red, 3.2, green'
    print(split_strip_coerce(line, ','))