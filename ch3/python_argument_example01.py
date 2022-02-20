def function(arg):
    arg += " in function"
    print(arg)


if __name__ == '__main__':
    immutable = "hello"
    function(immutable)

    mutable = list("hello")
    print(immutable)

    function(mutable)
    print(mutable)

