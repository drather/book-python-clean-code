import unittest

from ch8.test_refactoring_06_unittest_example_01 import MergeRequestStatus
from ch8.test_refactoring_08_unittest_example_03 import AcceptanceThreshold


class TestAcceptanceThreshold(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture_data = (
            (
                {"downvotes": set(), "upvotes": set()},
                MergeRequestStatus.PENDING
            ),

            (
                {"downvotes": set(), "upvotes": {"dev1"}},
                MergeRequestStatus.PENDING
            ),

            (
                {"downvotes": {"dev1"}, "upvotes": set()},
                MergeRequestStatus.REJECTED
            ),

            (
                {"downvotes": set(), "upvotes": {"dev1", "dev2"}},
                MergeRequestStatus.APPROVED
            ),
        )

    def test_status_resolution(self):
        for context, expected in self.fixture_data:
            with self.subTest(context=context):
                status = AcceptanceThreshold(context).status()
                self.assertEqual(status, expected)
