import pytest

from ch8.test_refactoring_06_unittest_example_01 import MergeRequest, MergeRequestStatus, MergeRequestException


def test_simple_rejected():
    merge_request = MergeRequest()
    merge_request.downvote("maintainer")
    assert merge_request.status == MergeRequestStatus.REJECTED


def test_jest_create_is_pending():
    assert MergeRequest().status == MergeRequestStatus.PENDING


def test_pending_awaiting_review():
    merge_request = MergeRequest()
    merge_request.upvote("core-dev")
    assert merge_request.status == MergeRequestStatus.PENDING


def test_invalid_types():
    merge_request = MergeRequest()
    pytest.raises(TypeError, merge_request.upvote, {"invalid-object"})


def test_cannot_vote_on_closed_merge_request():
    merge_request = MergeRequest()
    merge_request.close()

    pytest.raises(MergeRequestException, merge_request.upvote, "dev1")
    with pytest.raises(
        MergeRequestException,
        match="",
    ):
        merge_request.downvote("dev1")


