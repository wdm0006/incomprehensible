"""
.. module:: split_strip_coerce
   :platform: Unix, Windows
   :synopsis: a questionably named function that splits a string on some delimiter, strips the resultant strings, and coerces them into int, str, or float

.. moduleauthor:: Will McGinnis <will@pedalwrencher.com>


"""

__author__ = 'willmcginnis'


def _coerce(y):
    if y.isdigit() or (y[:1] == '-' and y[1:].isdigit()):
        try:
            return int(y)
        except ValueError:
            pass
    body = y[1:] if y[:1] == '-' else y
    if body.replace('.', '', 1).isdigit():
        try:
            return float(y)
        except ValueError:
            pass
    return y


def split_strip_coerce(x_in, delimiter):
    """

    >>> split_strip_coerce('2, red, 3.2, green', ',')
    [2, 'red', 3.2, 'green']

    :param x_in:
    :param delimiter:
    :return:
    """
    return [_coerce(y) for y in [str(x).strip() for x in x_in.split(delimiter)]]

if __name__ == '__main__':
    line = '2, red, 3.2, green'
    print(split_strip_coerce(line, ','))