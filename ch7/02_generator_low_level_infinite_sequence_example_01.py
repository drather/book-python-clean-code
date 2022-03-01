class NumberSequence:
    def __init__(self, start=0):
        self.current = start

    def next(self):
        current = self.current
        self.current += 1
        return current


if __name__ == '__main__':
    seq1 = NumberSequence()

    print(seq1.next())
    print(seq1.next())
    print(seq1.next())

    seq2 = NumberSequence()

    print(seq2.next())
    print(seq2.next())
    print(seq2.next())
