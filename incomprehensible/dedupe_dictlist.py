"""
Deduplicates a list of json blobs based on just certain keys (in this case ignoring ts)
"""

__author__ = 'willmcginnis'


def dedupe_dictlist(x_in, keys):
    return [v for _, v in {'_'.join([str(d.get(k, '')) for k in keys]): d for d in x_in}.items()]

if __name__ == '__main__':
    dl = [
        {"ts": 123, "A": "A", "B": "B"},
        {"ts": 124, "A": "B", "B": "B"},
        {"ts": 125, "A": "A", "B": "B"}
    ]
    print(dedupe_dictlist(dl, keys=['A', 'B']))