def show(e, rest):
    print("요소: {0} - 나머지: {1}".format(e, rest))


if __name__ == '__main__':
    first, *rest = [1, 2, 3, 4, 5]
    show(first, rest)

    *rest, last = range(6)
    show(last, rest)

    first, *middle, last = range(6)

    print(first)

    print(last)

    first, last, *empty = (1, 2)

    print(first)

    print(last)

    print(empty)
