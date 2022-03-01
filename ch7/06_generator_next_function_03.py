def sequence(start=0):
    while True:
        yield start
        start += 1


if __name__ == '__main__':
    seq = sequence(10)

    print(next(seq))
    print(next(seq))

    print(list(zip(sequence(), "abcdef")))