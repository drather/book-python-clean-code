import itertools


def process_purchases(purchases):
    _min, _max, _avg = itertools.tee(purchases, 3)
    return _min, _max, _avg


