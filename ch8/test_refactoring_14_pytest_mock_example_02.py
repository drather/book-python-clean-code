from unittest import mock

from test_refactoring_13_pytest_mock_example_01 import BuildStatus

STATUS_ENDPOINT = ""


@mock.patch("test_refactoring_13_pytest_mock_example_01.requests")
def test_build_notification_send(mock_requests):
    build_date = "2019-01-01-T00:00:01"
    with mock.patch("test_refactoring_13_pytest_mock_example_01.BuildStatus.build_date", return_value=build_date):
        BuildStatus.notify(123, "ok")

    expected_payload = {"id": 13, "status": "ok", "built_at": build_date}
    mock_requests.post.assert_called_with(
        STATUS_ENDPOINT, json=expected_payload
    )
