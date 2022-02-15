import logging
import time

logger = logging.getLogger()


def connect_with_retry(connector, retry_n_times, retry_threshold=5):
    """
    커넥터와 연결을 맺는다. <retry_n_times> 만큼 재시도

    연결에 성공하면 connection 객체 반환
    재시도까지 모두 실패하면 ConnectionError 발생
    :param connector:
    :param retry_n_times:
    :param retry_threshold:
    :return:
    """
    for _ in range(retry_n_times):
        try:
            return connector.connect()
        except ConnectionError as e:
            logger.info(f"새로운 연결 시도, {e}, {retry_threshold}")
            time.sleep(retry_threshold)

    exc = ConnectionError(f"{retry_n_times} 번째 재시도 연결 실패")
    logger.exception(exc)
    raise exc


class DataTransport:
    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        self.connection = connect_with_retry(self._connector, self.retry_n_times, self.retry_threshold)
        self.send(event)

    def send(self, event):
        try:
            return self.connection.send(event.decode())
        except ValueError as e:
            logger.error(f"{event} 잘못된 데이터 포함: {e}")
            raise
