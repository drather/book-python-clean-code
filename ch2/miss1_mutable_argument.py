def wrong_user_display(user_metadata: dict = {"name": "John", "age": 30}):
    name = user_metadata.pop("name")
    age = user_metadata.pop("age")
    return f"{name} {age}"


if __name__ == '__main__':
    print(wrong_user_display())

    print(wrong_user_display({"name": "jane", "age": 25}))

    wrong_user_display()


