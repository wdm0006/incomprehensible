"""

"""

__author__ = 'willmcginnis'


def flatten_list(input):
    return [y for z in [x if isinstance(x, list) else [x] for x in input] for y in z]

if __name__ == '__main__':
    nested = [1, 2, [3, 4, 5], 6]
    print(flatten_list(nested))