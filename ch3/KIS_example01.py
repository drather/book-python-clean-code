class ComplicatedNamespace:
    """
    프로퍼티를 가진 객체를 초기화하는 복잡한 예제
    """
    ACCEPTED_VALUES= ("id_", "user", "location")

    @classmethod
    def init_with_data(cls, **data):
        instance = cls()

        for key, value in data.items():
            if key in cls.ACCEPTED_VALUES:
                setattr(instance, key, value)

            return instance
