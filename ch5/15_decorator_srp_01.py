import functools
import time
import logging

logger = logging.getLogger(__name__)


def log_execution(function):
    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        logger.info(f"{function} 함수 실행", function)
        return function(*args, **kwargs)
    return wrapped


def measure_time(function):
    @functools.wraps(function)
    def wrapped(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        logger.info("함수 %s 의 실행 시간: %.2f", function, time.time() - start_time)
        return result
    return wrapped


@measure_time
@log_execution
def operation():
    pass
