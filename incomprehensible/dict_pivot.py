"""
"""

__author__ = 'willmcginnis'


def dict_pivot(x_in, key):
    return [dict([(k, v) for k, v in x_in.items() if k != key] + ch) for ch in [[(key + '.' + k, v) for k, v in y.items()] for y in x_in[key]]]

if __name__ == '__main__':
    dl = {"ts": 123, "A": "A", "B": "B", "sub": [{"C": 10}, {"C": 8}]}
    print(dict_pivot(dl, key='sub'))