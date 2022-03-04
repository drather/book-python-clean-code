import pytest

from ch8.test_refactoring_06_unittest_example_01 import MergeRequest, MergeRequestStatus, MergeRequestException
from ch8.test_refactoring_08_unittest_example_03 import AcceptanceThreshold


@pytest.mark.parametrize("context,expected_status", (
        (
            { "downvotes": set(), "upvotes": set()},
            MergeRequestStatus.PENDING
        ),

        (
            { "downvotes": set(), "upvotes": {"dev1"}},
            MergeRequestStatus.PENDING
        ),

        (
            { "downvotes": {"dev1"}, "upvotes": set()},
            MergeRequestStatus.REJECTED
        ),

        (
            { "downvotes": set(), "upvotes": set()},
            MergeRequestStatus.PENDING
        ),
))
def test_acceptance_threshold_status_resolution(context, expected_status):
    assert AcceptanceThreshold(context).status() == expected_status
