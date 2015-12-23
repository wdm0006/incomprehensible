"""

"""

__author__ = 'willmcginnis'


def flatten_list(x_in):
    return [y for z in [x if isinstance(x, list) else [x] for x in x_in] for y in z]

if __name__ == '__main__':
    nested = [1, 2, 3, [4, 'B', 6], {'7': 'A'}]
    print(flatten_list(nested))