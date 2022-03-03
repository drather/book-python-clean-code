class CustomException(Exception):
    pass


def sequence(name, start, end):
    value = start
    print(f"{name}, 제너레이터 {start} 에서 시작")

    while value < end:
        try:
            received = yield value
            print(f"{name}, 제너레이터 {received} 값 수신")
        except CustomException as e:
            print(f"{name}, 제너레이터 {e} 에러 처리")
            print("Ok")


def main():
    step1 = yield from sequence("first", 0, 5)
    step2 = yield from sequence("second", step1, 10)


if __name__ == '__main__':
    g = main()
    print(next(g))
    print(next(g))
    g.send(" 첫번쨰 제너레이터 위한 값")

    g.throw(CustomException("처리가능 예외"))

    print(next(g))

    print(next(g))

    print(next(g))

    print(next(g))

    print(g.throw("두번쨰 제너레이터 향한 예외"))

