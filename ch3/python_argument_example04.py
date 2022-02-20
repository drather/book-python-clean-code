USERS = [(i, f"first_name_{i}", f"last_name_{i}") for i in range(1000)]


class User:
    def __init__(self, user_id, first_name, last_name):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name


def bad_users_from_rows(dbrows) -> list:
    """
    파이썬스럽지 않은 예
    :param dbrows:
    :return:
    """
    return [User(row[0], row[1], row[2]) for row in dbrows]


def users_from_rows(dbrows) -> list:
    """
    DB 레코드에서 사용자 생성
    :param dbrows:
    :return:
    """
    return [
        User(user_id, first_name, last_name)
        for (user_id, first_name, last_name) in dbrows
    ]
