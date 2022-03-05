from datetime import datetime
from unittest.mock import Mock

import pytest

ENDPOINT = ""


class BuildStatus:
    endpoint = ENDPOINT

    def __init__(self, transport):
        self.transport = transport

    @staticmethod
    def build_date() -> str:
        return datetime.utcnow().isoformat()

    def compose_payload(self, merge_request_id, status) -> dict:
        return {
            "id": merge_request_id,
            "status": status,
            "built_at": self.build_date()
        }

    def deliver(self, payload):
        response = self.transport.post(self.endpoint, json=payload)
        response.raise_for_status()
        return response

    def notify(self, merge_request_id, status):
        return self.deliver(self.compose_payload(merge_request_id, status))


@pytest.fixture
def build_status():
    bstatus = BuildStatus(Mock())
    bstatus.build_date = Mock(return_value="2018-01-01T00:00:01")
    return bstatus


def test_build_notification_sent(build_status):
    build_status.notify(1234, "ok")

    expected_payload = {
        "id": 1234,
        "status": "ok",
        "built_at": build_status.build_date(),
    }

    build_status.trasport.assert_called_with(
        build_status.endpoint, json=expected_payload
    )

