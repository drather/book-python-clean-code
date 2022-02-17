class BaseTokenizer:
    def __init__(self, str_token):
        self.str_token = str_token

    def __iter__(self):
        yield from self.str_token.split("-")


if __name__ == '__main__':
    tk = BaseTokenizer("28a2320b-3d24-49234-2985a90")
    print(list(tk))
