class SequenceOfNumbers:
    def __init__(self, start=0):
        self.current = start

    def __next__(self):
        current = self.current
        self.current += 1
        return current

    def __iter__(self):
        return self


if __name__ == '__main__':
    my_list = list(zip(SequenceOfNumbers(), "abcdef"))

    print(my_list)

    seq = SequenceOfNumbers(100)
    print(next(seq))
    print(next(seq))
