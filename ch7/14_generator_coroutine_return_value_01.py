def sequence(name, start, end):
    print(f"{name}, 제너레이터 {start} 에서 시작")

    yield from range(start, end)

    print(f"{name}, 제너레이터 {end} 에서 종료")
    return end


def main():
    step1 = yield from sequence("first", 0, 5)
    step2 = yield from sequence("second", step1, 10)


if __name__ == '__main__':
    g = main()

    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))

    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
    print(next(g))
