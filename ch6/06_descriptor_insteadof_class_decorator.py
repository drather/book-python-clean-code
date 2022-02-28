from datetime import datetime
from functools import partial
from typing import Callable


class BaseFieldTransformation:
    def __init__(self, transformation: Callable[[], str]) -> None:
        self._name = None
        self.transformation = transformation

    def __get__(self, instance, owner):
        if instance is None:
            return self

        raw_value = instance.__dict__[self._name]
        return self.transformation(raw_value)

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, instance, value):
        instance.__dict__[self._name] = value


ShowOriginal = partial(BaseFieldTransformation, transformation=lambda x: x)
HideField = partial(BaseFieldTransformation, transformation=lambda x: "민감정보 삭제")
FormatTime = partial(BaseFieldTransformation, transformation=lambda ft: ft.strftime("%Y-%m-%d %H:%M"))


class LoginEvent:
    username = ShowOriginal()
    password = HideField()
    ip = ShowOriginal()
    timestamp = FormatTime()

    def __init__(self, username, password, ip, timestamp):
        self.username = username
        self.password = password
        self.ip = ip
        self.timestamp = timestamp

    def serialize(self):
        return {
            "username": self.username,
            "password": self.password,
            "ip": self.ip,
            "timestamp": self.timestamp,
        }


if __name__ == '__main__':
    le = LoginEvent("john", "secret_password", "1.1.1.1", datetime.utcnow())
    print(vars(le))

    print(le.serialize())

    print(le.password)
