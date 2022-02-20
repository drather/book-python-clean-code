def function1(key1, key2):
    print(key1)
    print(key2)


def function2(**kwargs):
    print(kwargs)


if __name__ == '__main__':
    my_parameter_dict = {
        "key1": "value1",
        "key2": "value2"
    }
    function1(**my_parameter_dict)

    function2(key="value")