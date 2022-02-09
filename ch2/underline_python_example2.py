class Connector:
    def __init__(self, source):
        self.source = source
        self.__timeout = 60

    def connect(self):
        print("connecting with {0}s".format(self.__timeout))


if __name__ == '__main__':
    conn = Connector("postgresql://localhost")
    conn.connect()

    print(conn.source)
    print(conn._timeout)
