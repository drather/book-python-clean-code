import abc
from abc import ABC


class InvalidTransitionError(Exception):
    """
    도달 불가한 상태에서 전이할 때 발생하는 예외
    """


class MergeRequestState(abc.ABC):
    def __init__(self, merge_request):
        self._merge_request = merge_request

    @abc.abstractmethod
    def open(self):
        ...

    @abc.abstractmethod
    def close(self):
        ...

    @abc.abstractmethod
    def merge(self):
        ...

    def __str__(self):
        return self.__class__.__name__


class Open(MergeRequestState, ABC):
    def open(self):
        self._merge_request.approvals = 0

    def close(self):
        self._merge_request.approvals = 0
        self._merge_request.state = Closed

    def merge(self):
        print(f"{self._merge_request} 에서 머지")
        print(f"{self._merge_request.source_branch} 브랜치 삭제")
        self._merge_request.state = Merged


class Closed(MergeRequestState, ABC):
    def open(self):
        print(f"종료된 머지 리퀘스트 {self._merge_request} 재오푼")
        self._merge_request.state = Open

    def close(self):
        pass

    def merge(self):
        raise InvalidTransitionError("종료된 요청을 머지할 수 없음")


class Merged(MergeRequestState, ABC):
    def open(self):
        raise InvalidTransitionError("이미 머지 완료됨")

    def close(self):
        raise InvalidTransitionError("이미 머지 완료됨")

    def merge(self):
        pass


class MergeRequest:
    def __init__(self, source_branch: str, target_branch: str) -> None:
        self.source_branch = source_branch
        self.target_branch = target_branch
        self._state = None
        self.approvals = 0
        self.state = Open

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state_cls):
        self._state = new_state_cls(self)

    def open(self):
        return self.state.open()

    def close(self):
        return self.state.close()

    def merge(self):
        return self.state.merge()

    def __str__(self):
        return f"{self.target_branch}: {self.source_branch}"


if __name__ == '__main__':
    mr = MergeRequest("develop", "master")

    mr.open()

    print(mr.approvals)

    mr.approvals = 3

    mr.close()

    print(mr.approvals)

    mr.open()

    mr.merge()

    mr.close()
