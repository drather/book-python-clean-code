import unittest

from unittest.mock import Mock

from ch8.test_refactoring_02_unittest_object_example_02 import WrappedClient


class TestWrapped(unittest.TestCase):
    def test_send_converts_type(self):
        wrapped_client = WrappedClient()
        wrapped_client.client = Mock()
        wrapped_client.send("value", 1)
        wrapped_client.client.send.assert_called_with("value", 1)

