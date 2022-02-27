EVENTS_REGISTRY = {}


def register_event(event_cls):
    """
    모듈에서 접근 가능하도록 이벤트 클래스를 레지스트리에 등록
    :param event_cls:
    :return:
    """
    EVENTS_REGISTRY[event_cls.__name__] = event_cls
    return event_cls


class Event:
    """

    """


class UserEvent:
    TYPE = "user"


@register_event
class UserLoginEvent(UserEvent):
    """
    사용자가 시스템 접근 시 발생하는 이벤트
    """


@register_event
class UserLogoutEvent(UserEvent):
    """
     사용자가 시스템 로그아웃 시 발생하는 이벤트
     """