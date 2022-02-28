class SharedDataDescriptor:
    def __init__(self, initial_value):
        self.value = initial_value

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.value

    def __set__(self, instance, value):
        self.value = value


class ClientClass:
    descriptor = SharedDataDescriptor("첫 번째 값")


if __name__ == '__main__':
    client1 = ClientClass()
    print(client1.descriptor)

    client2 = ClientClass()
    print(client2.descriptor)

    client2.descriptor = "client2 를 위한 값"
    print(client2.descriptor)

    print(client1.descriptor)
