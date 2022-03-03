import logging


def search_nested_bad(array, desired_value):
    coords = None

    for i, row in enumerate(array):
        for j, cell in enumerate(row):
            if cell == desired_value:
                coords = (i, j)
                break

        if coords is not None:
            break
    if coords is None:
        raise ValueError(f"{desired_value} not fount")

    logging.getLogger().info("[%i, %i] 에서 값 %r 발견", *coords, desired_value)
    return coords

