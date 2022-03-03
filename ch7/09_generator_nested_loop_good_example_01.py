import logging


def _iterate_array2d(array2d):
    for i, row in enumerate(array2d):
        for j, cell in enumerate(row):
            yield (i, j), cell


def search_nested(array, desired_value):
    try:
        coord = next(
            coord
            for (coord, cell) in _iterate_array2d(array) if cell == desired_value
        )
    except StopIteration as e:
        raise ValueError(f"{desired_value} not fount")

    logging.getLogger().info("[%i, %i] 에서 값 %r 발견", *coord, desired_value)
    return coord
