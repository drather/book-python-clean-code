class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data

    @staticmethod
    def meets_condition(event_data: dict):
        return False


class UnknownEvent(Event):
    """
     식별 불가한 이벤트
    """


class LoginEvent(Event):
    """
    로그인 사용자에 의한 이벤트
    """
    @staticmethod
    def meets_condition(event_data: dict):
        return event_data["before"]["session"] == 0 and event_data["after"]["session"] == 1


class LogoutEvent(Event):
    """
    로그아웃 사용자에 의한 이벤트
    """
    @staticmethod
    def meets_condition(event_data: dict):
        return event_data["before"]["session"] == 1 and event_data["after"]["session"] == 0


class SystemMonitor:
    """
    시스템에서 발생한 이벤트 분류
    """
    def __init__(self, event_data):
        self.event_data = event_data

    def identify_data(self):
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self.event_data):
                    return event_cls(self.event_data)
            except KeyError:
                continue

        return UnknownEvent(self.event_data)
