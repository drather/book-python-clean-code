import unittest

from ch8.test_refactoring_06_unittest_example_01 import MergeRequest, MergeRequestStatus, MergeRequestException


class TestMergeRequestStatus(unittest.TestCase):

    def test_simple_rejected(self):
        merge_request = MergeRequest()
        merge_request.downvote("maintainer")
        self.assertEqual(merge_request.status, MergeRequestStatus.REJECTED)

    def test_just_create_is_pending(self):
        self.assertEqual(MergeRequest().status, MergeRequestStatus.PENDING)

    def test_pending_awaiting_review(self):
        merge_request = MergeRequest()
        merge_request.upvote("core-dev")
        self.assertEqual(merge_request.status, MergeRequestStatus.PENDING)

    def test_approved(self):
        merge_request = MergeRequest()
        merge_request.upvote("dev1")
        merge_request.upvote("dev2")

        self.assertEqual(merge_request.status, MergeRequestStatus.APPROVED)

    def test_cannot_upvote_on_close_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()

        self.assertRaises(
            BaseException,
            merge_request.downvote,
            "dev1"
        )

    def test_cannot_downvote_on_close_merge_request(self):
        merge_request = MergeRequest()
        merge_request.close()

        self.assertRaisesRegex("종료된 머지 리퀘스트에 투표 불가", merge_request.downvote, "dev1")

