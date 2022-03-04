from enum import Enum


class MergeRequestStatus(Enum):
    APPROVED = "approved"
    REJECTED = "rejected"
    PENDING = "pending"
    OPEN = "open"
    CLOSED = "closed"


class MergeRequestException(Exception):
    pass


class MergeRequest:
    def __init__(self):
        self._context = {
            "upvotes": set(),
            "downvotes": set(),
        }
        self._status = MergeRequestStatus.OPEN

    def close(self):
        self._status = MergeRequestStatus.CLOSED

    def _cannot_vote_if_close(self):
        if self._status == MergeRequestStatus.CLOSED:
            raise MergeRequestException("종")

    @property
    def status(self):
        if self._status == MergeRequestStatus.CLOSED:
            return self._status

        if self._context["downvotes"]:
            return MergeRequestStatus.REJECTED

        elif len(self._context["upvotes"]) >= 2:
            return MergeRequestStatus.APPROVED

        else:
            return MergeRequestStatus.PENDING

    def upvote(self, by_user):
        self._cannot_vote_if_close()

        self._context["downvotes"].discard(by_user)
        self._context["upvotes"].add(by_user)

    def downvote(self, by_user):
        self._cannot_vote_if_close()

        self._context["upvotes"].discard(by_user)
        self._context["downvotes"].add(by_user)

