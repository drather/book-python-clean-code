import logging
import time

logger = logging.getLogger()


class DataTransport:
    """
    다른 레벨에서 예외를 처리하는 객체의 예
    """

    retry_threshold: int = 5
    retry_n_times: int = 3

    def __init__(self, connector):
        self._connector = connector
        self.connection = None

    def deliver_event(self, event):
        try:
            self.connect()
            data = event.decode()
            self.send(data)

        except ConnectionError as e:
            logger.info(f"연결 실패: {e}")
            raise

        except ValueError as e:
            logger.info(f"잘못된 데이터 포함: {event}, {e}")
            raise

    def connect(self):
        for _ in range(self.retry_n_times):
            try:
                self.connection = self._connector.connect()
            except ConnectionError as e:
                logger.info(f"새로운 연결 시도, {e}, {self.retry_threshold}")
                time.sleep(self.retry_threshold)
            else:
                return self.connection
        raise ConnectionError(f"{self.retry_n_times} 번째 재시도 연결 실패")

    def send(self, data):
        return self.connection.send(data)

    def decode(self):
        pass
