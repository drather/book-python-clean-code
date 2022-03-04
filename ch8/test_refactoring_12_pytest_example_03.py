import pytest

from ch8.test_refactoring_06_unittest_example_01 import MergeRequest, MergeRequestStatus, MergeRequestException
from ch8.test_refactoring_08_unittest_example_03 import AcceptanceThreshold


@pytest.fixture
def rejected_mr():
    merge_request = MergeRequest()

    merge_request.downvote("dev1")
    merge_request.upvote("dev2")
    merge_request.upvote("dev3")
    merge_request.downvote("dev4")

    return merge_request


def test_simple_rejected(rejected_mr):
    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_rejected_with_approvals(rejected_mr):
    rejected_mr.upvote("dev2")
    rejected_mr.downvote("dev3")

    assert rejected_mr.status == MergeRequestStatus.REJECTED


def test_rejected_to_pending(rejected_mr):
    rejected_mr.upvote("dev1")
    assert rejected_mr.status == MergeRequestStatus.PENDING


def test_rejected_to_approved(rejected_mr):
    rejected_mr.upvote("dev1")
    rejected_mr.upvote("dev2")

    assert rejected_mr.status == MergeRequestStatus.APPROVED
