"""

"""

__author__ = 'willmcginnis'


def split_strip_coerce(input, delimiter):
    return [int(y) if y.replace('-', '', 1).isdigit() else float(y) if y.replace('.', '', 1).replace('-', '', 1).isdigit() else y for y in [str(x).strip() for x in input.split(delimiter)]]

if __name__ == '__main__':
    line = '2, red, 3.2, green'
    print(split_strip_coerce(line, ','))