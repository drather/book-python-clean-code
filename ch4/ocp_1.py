class Event:
    def __init__(self, raw_data):
        self.raw_data = raw_data


class UnknownEvent(Event):
    """
     식별 불가한 이벤트
    """


class LoginEvent(Event):
    """
    로그인 사용자에 의한 이벤트
    """


class LogoutEvent(Event):
    """
    로그아웃 사용자에 의한 이벤트
    """


class SystemMonitor:
    """
    시스템에서 발생한 이벤트 분류
    """

    def __init__(self, event_data):
        self.event_data = event_data

    def identify_event(self):
        if self.event_data["before"]["session"] == 0 and \
                self.event_data["after"]["session"] == 1:
            return LoginEvent(self.event_data)

        elif self.event_data["before"]["session"] == 1 and \
                self.event_data["after"]["session"] == 0:
            return LogoutEvent(self.event_data)

        return UnknownEvent(self.event_data)


if __name__ == '__main__':
    l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    print(l1.identify_event().__class__.__name__)

    l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    print(l2.identify_event().__class__.__name__)

    l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    print(l3.identify_event().__class__.__name__)