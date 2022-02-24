import logging
from functools import wraps


class ControllerException(Exception):
    """
    도메인에서 발생하는 일반적인 예외
    """


def retry(operation):
    @wraps(operation)
    def wrapped(*args, **kwargs):
        last_raised = None
        RETIRES_LIMIT = 3

        for _ in range(RETIRES_LIMIT):
            try:
                return operation(*args, **kwargs)

            except ControllerException as e:
                logging.getLogger().info("retrying %s", operation.__qualname__)
                last_raised = e

        raise last_raised

    return wrapped


@retry
def run_operation(task):
    """
    실행 중 예외가 발생할 것 같은 특정 작업 실행
    :param task:
    :return:
    """
    return task.run()
